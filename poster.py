# poster.py
import json, os, random, time, datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import requests
from atproto import Client

from cities import CITIES
from templates import TEMPLATES

RAIN_THRESHOLD_MM   = 0.3
DAILY_MAX_POSTS     = 6
WINDOW_START_HOUR   = 8     # UK local
WINDOW_END_HOUR     = 14    # inclusive (so 8,9,10,11,12,13,14 = 7 slots, max 6 posts)
UK_TZ               = ZoneInfo("Europe/London")
STATE_FILE          = Path("state_poster.json")

def load_state():
  if STATE_FILE.exists():
      return json.loads(STATE_FILE.read_text())
  return {}

def save_state(s):
  STATE_FILE.write_text(json.dumps(s, indent=2, sort_keys=True))

def reset_if_new_day(state, today):
  if state.get("date") != today:
      state.clear()
      state["date"] = today
      state["posted_cities"] = []
      state["hours_used"] = []
  return state

def is_raining(lat, lon):
  url = (
      "https://api.open-meteo.com/v1/forecast"
      f"?latitude={lat}&longitude={lon}"
      "&current=precipitation"
      "&timezone=Europe%2FLondon"
  )
  try:
      r = requests.get(url, timeout=10).json()
      mm = r.get("current", {}).get("precipitation", 0) or 0
      return mm >= RAIN_THRESHOLD_MM, mm
  except Exception as e:
      print(f"[weather] {lat},{lon} error: {e}")
      return False, 0

def main():
  now_uk = datetime.datetime.now(UK_TZ)
  hour = now_uk.hour
  today = now_uk.date().isoformat()

  if not (WINDOW_START_HOUR <= hour <= WINDOW_END_HOUR):
      print(f"[poster] outside UK window (hour={hour}), skipping")
      return

  state = reset_if_new_day(load_state(), today)

  if hour in state["hours_used"]:
      print(f"[poster] already posted in hour {hour}, skipping")
      return
  if len(state["posted_cities"]) >= DAILY_MAX_POSTS:
      print("[poster] daily cap reached")
      return

  candidates = []
  for city, (lat, lon) in CITIES.items():
      if city in state["posted_cities"]:
          continue
      raining, mm = is_raining(lat, lon)
      if raining:
          candidates.append((city, mm))
      time.sleep(0.25)  # be polite

  if not candidates:
      print("[poster] nowhere raining ≥ threshold")
      save_state(state)
      return

  # Slight bias towards heavier rain so we don't always post for the same drizzly place
  candidates.sort(key=lambda x: x[1], reverse=True)
  top = candidates[: max(3, len(candidates) // 2)]
  city, mm = random.choice(top)

  text = random.choice(TEMPLATES).format(city=city)

  client = Client()
  client.login(os.environ["BSKY_HANDLE"], os.environ["BSKY_APP_PASSWORD"])
  client.send_post(text=text)

  state["posted_cities"].append(city)
  state["hours_used"].append(hour)
  save_state(state)
  print(f"[poster] posted ({mm}mm in {city}): {text}")

if __name__ == "__main__":
  main()
