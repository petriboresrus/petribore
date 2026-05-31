# poster.py
import json, os, random, datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import requests
from atproto import Client

from cities import CITIES
from templates import TEMPLATES

RAIN_THRESHOLD_MM = 0.3
DAILY_MAX_POSTS   = 6
WINDOW_START_HOUR = 8
WINDOW_END_HOUR   = 14
UK_TZ             = ZoneInfo("Europe/London")
STATE_FILE        = Path("state_poster.json")


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


def fetch_all_precipitation(cities):
    names = list(cities.keys())
    lats = ",".join(f"{cities[c][0]}" for c in names)
    lons = ",".join(f"{cities[c][1]}" for c in names)
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lats}&longitude={lons}"
        "&current=precipitation"
        "&timezone=Europe%2FLondon"
    )
    try:
        data = requests.get(url, timeout=20).json()
    except Exception as e:
        print(f"[weather] batch error: {e}")
        return {}
    if isinstance(data, list):
        result = {}
        for name, entry in zip(names, data):
            mm = (entry.get("current", {}) or {}).get("precipitation", 0) or 0
            result[name] = mm
        return result
    else:
        mm = (data.get("current", {}) or {}).get("precipitation", 0) or 0
        return {names[0]: mm}


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
        print("[poster] daily cap reached, skipping")
        return

    rainfall = fetch_all_precipitation(CITIES)
    if not rainfall:
        print("[poster] no weather data returned, skipping")
        return

    candidates = [
        (city, mm) for city, mm in rainfall.items()
        if city not in state["posted_cities"] and mm >= RAIN_THRESHOLD_MM
    ]

    if not candidates:
        wettest = max(rainfall.items(), key=lambda x: x[1], default=("nowhere", 0))
        print(f"[poster] nothing >= {RAIN_THRESHOLD_MM}mm. wettest: {wettest[0]} ({wettest[1]}mm)")
        save_state(state)
        return

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
