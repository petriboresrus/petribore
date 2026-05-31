# petribore

A Bluesky bot posting variations on "I love the smell of [UK city] when it rains"
when it's actually raining there, and reposting people who reply "it's called
petrichor".

## Setup

1. Create the Bluesky account (suggested handle: `sarahclarke94.bsky.social`).
 Add a profile photo, banner, and bio.
2. In Bluesky settings → **Privacy and security → App passwords** → generate one.
3. Fork/clone this repo, push it to your GitHub. Make it **public** (free
 unlimited Action minutes).
4. In the repo: **Settings → Secrets and variables → Actions → New repository
 secret**:
 - `BSKY_HANDLE` = your handle (e.g. `sarahclarke94.bsky.social`)
 - `BSKY_APP_PASSWORD` = the app password from step 2
5. Go to **Actions** tab, enable workflows, then **Run workflow** manually with
 `job=poster` to test (won't post unless somewhere is actually raining).

## How it runs

- **Poster** runs at 2 minutes past every hour 07:00–14:00 UTC. The script
checks UK local time and only posts in the 08:00–14:59 window. Max 6
posts/day, max 1 per clock hour, max 1 per city per day, requires ≥0.3 mm
precipitation.
- **Reposter** runs every 20 minutes. Searches for "it's called petrichor",
skips quote posts and self-posts, max 10 reposts/day.
- Both write small JSON state files which are committed back to the repo so
state survives between runs.

## Tweaking

- Edit `cities.py` to add/remove locations.
- Edit `templates.py` to add new sentence variants.
- Adjust thresholds and caps at the top of `poster.py` / `reposter.py`.

## Notes

- GitHub Actions cron is best-effort and may be delayed several minutes.
- Scheduled workflows pause after 60 days of repo inactivity, but the
state-file commits keep activity fresh.
- All weather data: [Open-Meteo](https://open-meteo.com), free, no key.
