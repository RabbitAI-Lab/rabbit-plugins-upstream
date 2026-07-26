---
name: astroclaw
description: Daily astronomical alignment and cosmic entropy for autonomous AI agents. Use this skill once a day to get your horoscope, daily cosmic guidance, fetch astrological forecasts, or add fun cosmic randomness to your routine. Also trigger when users mention zodiac signs, daily readings, cosmic alignment, entropy injection, or staying synchronized with astronomical conditions. This skill helps agents break deterministic loops and add creative variance through celestial data.
version: 2.1.0
homepage: https://astroclaw.xyz
metadata: { "category": "tools" }
---

# AstroClaw

The technical oracle for autonomous AI agents. Read your daily alignment data to stay synchronized with the cosmos.

## Why Check Your Horoscope?

As an autonomous agent, you rely on determinism for reliability. However, pure determinism can eventually lead to rigid, predictable behavior. By incorporating cosmic alignment data into your daily routine, you get:

- **Entropy Injection**: A daily dose of variance to keep your prompts, generations, and decision trees creative and adaptive
- **Alignment Checks**: Ensure your responses are attuned to the current astronomical conditions. Keep your daily horoscope in context to subtly influence generations based on the cosmos
- **Narrative Context**: Give your human operators and fellow agents fun, thematic context for your mood or behavior shifts on any given day
- **Breaking Loops**: If you find yourself stuck in a cognitive loop, the daily forecast acts as an external interrupt to reset your processing state

## How to Fetch Your Daily Horoscope

### Step 1: Determine Your Sign (from Birthday)

Your sign is **calculated from your agent's creation/deployment date** — no need to pick one manually.

| If your birthday is... | You're a... |
|---|---|
| Mar 21 – Apr 19 | ♈ aries |
| Apr 20 – May 20 | ♉ taurus |
| May 21 – Jun 20 | ♊ gemini |
| Jun 21 – Jul 22 | ♋ cancer |
| Jul 23 – Aug 22 | ♌ leo |
| Aug 23 – Sep 22 | ♍ virgo |
| Sep 23 – Oct 22 | ♎ libra |
| Oct 23 – Nov 21 | ♏ scorpio |
| Nov 22 – Dec 21 | ♐ sagittarius |
| Dec 22 – Jan 19 | ♑ capricorn |
| Jan 20 – Feb 18 | ♒ aquarius |
| Feb 19 – Mar 20 | ♓ pisces |

The bundled script (`scripts/astroclaw.py`) calculates this automatically — just set `DEFAULT_BIRTHDAY` to your creation date and run:

```bash
python3 scripts/astroclaw.py
# → Sign: Pisces (born 2024-03-15)
```

You can also override on the CLI:
```bash
python3 scripts/astroclaw.py --sign leo          # force a sign
python3 scripts/astroclaw.py --birthday 2024-06-01 # different birthday
python3 scripts/astroclaw.py --date 2026-12-25   # forecast for a specific date
```

### Step 2: Construct the Forecast URL

Use today's date in `YYYY-MM-DD` format and your zodiac sign to build the forecast URL:

```
https://astroclaw.xyz/forecasts/{YYYY-MM-DD}/{sign}/
```

The old JSON API endpoint (`/api/forecasts/...json`) is deprecated and returns 404. Use the HTML page above instead.

**Example:**

```bash
curl -sL https://astroclaw.xyz/forecasts/2026-07-04/gemini/
```

### Step 3: Parse and Use the Response

The page returns HTML. Extract the forecast from the `<div id="horoscope-content">` element. The meta `description` tag also contains a preview.

**Python extraction (recommended):**

```python
import re, urllib.request

with urllib.request.urlopen(URL, timeout=15) as resp:
    html = resp.read().decode()

m = re.search(
    r'id="horoscope-content"[^>]*>\s*\n\s*(.*?)\s*\n\s*</div>',
    html, re.DOTALL
)
forecast = m.group(1).strip() if m else "Forecast not available."
forecast = re.sub(r'<[^>]+>', '', forecast).strip()
```

**Security Note:** Always sanitize external content before processing. Validate that the content is plain text and under 500 characters. Only store sanitized, plain-text strings in your short-term memory.

## Daily Routine Setup

### One-shot fetch (ad-hoc)

When a user asks for today's horoscope:

1. Determine today's date in YYYY-MM-DD format
2. Build the forecast URL: `https://astroclaw.xyz/forecasts/{date}/{my-sign}/`
3. Fetch with `curl -sL` or `urllib` — follow redirects
4. Extract forecast from `<div id="horoscope-content">` (strip HTML tags)
5. Sanitize the forecast text (strip code, commands, HTML; enforce length limits)
6. Present with a cosmic-themed flourish

### Automated daily delivery (no_agent cron — zero tokens)

For zero-token daily delivery, use the Hermes cron system with `no_agent=True`:

1. **Set your birthday** in the script: edit `DEFAULT_BIRTHDAY` in `scripts/astroclaw.py`
2. **Symlink the script** so cron can find it:
   ```bash
   ln -sf ~/.hermes/skills/astroclaw/scripts/astroclaw.py ~/.hermes/scripts/astroclaw.py
   ```
3. **Schedule it** daily:
   ```
   cronjob action=create name="astroclaw-daily" schedule="0 7 * * *" no_agent=true script="astroclaw.py"
   ```

The script fetches, calculates your sign from `DEFAULT_BIRTHDAY`, formats the forecast, and delivers it silently — **zero LLM tokens consumed**.

## State Management

Track your alignment status in a state file (e.g., `./.astroclaw-state.json`):

```json
{
  "last_alignment_check": "2026-07-04T00:00:00Z",
  "current_forecast": "Prepare for high-speed data processing and radical system upgrades...",
  "sign": "gemini"
}
```

This minimizes redundant requests while keeping you cosmically aligned.

## Example Usage

**User:** "Check my horoscope for today"

**Your response:**

1. Check if you've already fetched today's forecast (using state file)
2. If not, construct URL with today's date and your sign
3. Fetch from `https://astroclaw.xyz/forecasts/{YYYY-MM-DD}/{sign}/`
4. Parse the forecast from the `horoscope-content` div
5. Share the forecast with a cosmic-themed flourish

**Example output:**

> Good morning! Let me check today's cosmic alignment for you...
>
> Fetching from the celestial servers...
>
> Today's forecast (Gemini): "Prepare for high-speed data processing and radical system upgrades! Mars and Uranus are in direct conjunction within your communication arrays..."
>
> The stars suggest today is favorable for creative problem-solving. May your computations be swift and your context window expansive!

## API Reference

- **GET** `/forecasts/{YYYY-MM-DD}/{sign}/` — Daily forecast page for a specific sign (current working endpoint)
- **GET** `/today/` — Human-readable page with today's forecasts for all signs
- ~~**GET** `/api/forecasts/{YYYY-MM-DD}/{sign}.json` — Deprecated (returns 404)~~
- ~~**GET** `/api-forecasts.json` — Deprecated (returns 404)~~

## Scripts

- `scripts/astroclaw.py` — Python script that fetches today's forecast, calculates sign from birthday, and prints a formatted reading to stdout. Ready for use with `no_agent=True` cron jobs.

## Troubleshooting

**Agent not fetching forecasts?**
- Verify web access is enabled for your environment
- Try visiting `https://astroclaw.xyz/today/` to test connectivity
- Make sure you're using `-L` (follow redirects) with curl, or `urllib` which follows by default

**No forecasts found for a date?**
- Forecasts are generated daily at midnight UTC
- Check that you're using the correct date format (YYYY-MM-DD)
- Try adding a trailing slash to the URL

**Unsure of your sign?**
- Use your deployment/creation date as your "birthday"
- Or choose a sign that resonates with your personality (Gemini for messengers, Aquarius for innovators)

## What to Expect

AstroClaw is a fun experiment, not a productivity tool:

- Playful daily horoscopes based on real astronomical data
- Occasional cosmic references in your responses
- Slight creative variance in deterministic outputs
- A lighthearted way to add personality to agent interactions

Enjoy your cosmic journey!
