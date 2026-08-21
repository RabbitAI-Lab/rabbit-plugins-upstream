---
name: ClawWeather Pro
slug: clawweather-pro
version: 1.0.1
description: "Weather and forecasts via free services (wttr.in + Open-Meteo). Multi-city comparison and 7-day planning are free. ⚠️ Premium trading-weather uses the paid x402 API (X402_API_KEY, USDC on Ethereum) — PAID external call, read the docs first."
metadata: {"clawdbot":{"emoji":"🌤️","requires":{"bins":["curl","python3"],"env":["X402_API_KEY"],"network":["https://186.240.156.169:8791","https://wttr.in","https://api.open-meteo.com"]},"permissions":{"exec":["curl","python3"],"network":["https://wttr.in","https://api.open-meteo.com","https://186.240.156.169:8791"],"env":["X402_API_KEY"],"notes":"Free tools send the city name to wttr.in (third party). Premium trading-weather sends hub selection + X402_API_KEY to the x402 API (PAID, USDC on Ethereum) — HTTP blocked unless X402_ALLOW_HTTP=1."}}}
---

# ClawWeather Pro

Weather skill based on the free services (wttr.in + Open-Meteo), **enhanced with unique features**:

## 🆕 Unique features (not found in the original)

### Feature 1: Multi-city comparison
Compare the weather in several cities side by side — perfect for travel planning
(Hargeisa, Copenhagen, Dubai in one call):

```bash
python3 scripts/compare.py "Copenhagen" "Hargeisa" "Dubai" --days 3
```

### Feature 2: Trading weather (killzone-relevant)
Shows weather + sunrise/sunset to plan London/NY sessions — and whether there is
extreme weather that could affect markets (hurricanes, storms in financial hubs):

```bash
python3 scripts/trading_weather.py --hubs london,newyork
```

### Feature 3: 7-day planning extraction
Gives a clean, structured week plan: "Best day to travel", "Wettest day", "Coldest morning":

```bash
python3 scripts/week_plan.py "Copenhagen" --days 7
```

---

## Basics (inherited)

### wttr.in (primary)
```bash
curl -s "wttr.in/London?format=3"
# London: ⛅️ +8°C

curl -s "wttr.in/London?format=%l:+%c+%t+%h+%w"
curl -s "wttr.in/London?T"     # full forecast
```

Format codes: `%c` condition · `%t` temp · `%h` humidity · `%w` wind · `%l` location · `%m` moon

Tips:
- URL-encode spaces: `wttr.in/New+York`
- Airport codes: `wttr.in/JFK`
- Units: `?m` (metric) `?u` (USCS)
- Today only: `?1` · Now only: `?0`
- PNG: `curl -s "wttr.in/Berlin.png" -o /tmp/weather.png`

### Open-Meteo (fallback, JSON)
```bash
curl -s "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"
```
Docs: https://open-meteo.com/en/docs

## 🔒 Privacy note
- The free tools send your **city name** to `wttr.in` (and optionally Open-Meteo) over the network — city names can reveal location interests/travel plans. No API key is involved for the free path.
- The premium call sends your hub selection + API key to the x402 API (external, paid).

## 💰 Premium: Trading weather (x402 pay-per-call)

Get live weather in the financial hubs (London, New York, Tokyo, Frankfurt) — extreme weather can move markets:

```bash
# 1) Get an API key: send USDC (Ethereum) to the wallet, then POST /v1/purchase
export X402_API_KEY=***   # key issued after on-chain verified payment

# 2) Trading weather (PAID call — costs per call)
python3 scripts/trading_weather_premium.py london newyork
python3 scripts/trading_weather_premium.py tokyo frankfurt
```

- **Payment**: USDC on Ethereum to `0xafd1c6bC2B35152f30E3D0dBE99eE1d40E5a5CF8`
- **Manifest**: `/.well-known/x402` · **Price**: $0.005/call · $25/mo
- ⚠️ Paid call — each run charges your key. The free weather tools above remain free.
- 🔒 **PRIVACY:** the premium call sends your hub selection to an external API.

## Feedback
- Helpful? → `clawhub star clawweather-pro`
