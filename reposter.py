# reposter.py
import json, os, time, datetime
from pathlib import Path
from atproto import Client

PHRASE              = "it's called petrichor"
DAILY_MAX_REPOSTS   = 10
STATE_FILE          = Path("state_reposter.json")
SEEN_CAP            = 1000

def load_state():
  if STATE_FILE.exists():
      return json.loads(STATE_FILE.read_text())
  return {"date": "", "count": 0, "seen": []}

def save_state(s):
  s["seen"] = s["seen"][-SEEN_CAP:]
  STATE_FILE.write_text(json.dumps(s, indent=2))

def reset_if_new_day(state):
  today = datetime.date.today().isoformat()
  if state["date"] != today:
      state["date"] = today
      state["count"] = 0
  return state

def is_quote_post(post):
  """A quote post embeds another record. We want to skip these."""
  embed = getattr(post, "embed", None)
  if not embed:
      return False
  t = (getattr(embed, "py_type", "") or "").lower()
  # app.bsky.embed.record#view  or  app.bsky.embed.recordWithMedia#view
  return "embed.record" in t

def main():
  client = Client()
  client.login(os.environ["BSKY_HANDLE"], os.environ["BSKY_APP_PASSWORD"])
  my_did = client.me.did

  state = reset_if_new_day(load_state())
  if state["count"] >= DAILY_MAX_REPOSTS:
      print("[reposter] daily cap reached")
      save_state(state)
      return

  try:
      results = client.app.bsky.feed.search_posts({"q": PHRASE, "limit": 25})
  except Exception as e:
      print(f"[reposter] search error: {e}")
      return

  seen = set(state["seen"])

  # Process oldest first so we catch in chronological order
  posts = list(results.posts)
  posts.sort(key=lambda p: getattr(p.record, "created_at", ""))

  for post in posts:
      if state["count"] >= DAILY_MAX_REPOSTS:
          break
      if post.uri in seen:
          continue
      if post.author.did == my_did:
          seen.add(post.uri); continue
      if is_quote_post(post):
          seen.add(post.uri); continue
      text = (getattr(post.record, "text", "") or "").lower()
      if PHRASE not in text:
          seen.add(post.uri); continue

      try:
          client.repost(uri=post.uri, cid=post.cid)
          state["count"] += 1
          seen.add(post.uri)
          print(f"[reposter] reposted: {post.uri}")
          time.sleep(2)
      except Exception as e:
          print(f"[reposter] repost error on {post.uri}: {e}")
          seen.add(post.uri)

  state["seen"] = list(seen)
  save_state(state)
  print(f"[reposter] done. count today = {state['count']}")

if __name__ == "__main__":
  main()
