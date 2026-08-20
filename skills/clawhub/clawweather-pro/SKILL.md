---
name: ClawWeather Pro
slug: clawweather-pro
version: 1.0.0
description: "Vejr og prognoser uden API-nøgle (wttr.in + Open-Meteo). PLUS unik feature: multi-by sammenligning, trading-vejr (killzone-relevant) og 7-dages planlægnings-udtræk."
metadata: {"clawdbot":{"emoji":"🌤️","requires":{"bins":["curl","python3"]}}}
---

# ClawWeather Pro

Vejr-skill baseret på de gratis tjenester (wttr.in + Open-Meteo), **forbedret med unikke features**:

## 🆕 Unikke features (findes ikke i originalen)

### Feature 1: Multi-by sammenligning
Sammenlign vejret i flere byer side om side — perfekt til rejseplanlægning
(Hargeisa, København, Dubai i ét kald):

```bash
python3 scripts/compare.py "København" "Hargeisa" "Dubai" --days 3
```

### Feature 2: Trading-vejr (killzone-relevant)
Viser vejr + solopgang/-nedgang for at planlægge London/NY-sessioner — og om der er
ekstremt vejr der kan påvirke markeder (orkaner, storme i finans-hubber):

```bash
python3 scripts/trading_weather.py --hubs london,newyork
```

### Feature 3: 7-dages planlægnings-udtræk
Giver en ren, struktureret ugeplan: "Bedste dag at rejse", "Vådeste dag", "Koldeste morgen":

```bash
python3 scripts/week_plan.py "København" --days 7
```

---

## Basis (arvet)

### wttr.in (primær)
```bash
curl -s "wttr.in/London?format=3"
# London: ⛅️ +8°C

curl -s "wttr.in/London?format=%l:+%c+%t+%h+%w"
curl -s "wttr.in/London?T"     # fuld prognose
```

Format-koder: `%c` tilstand · `%t` temp · `%h` fugtighed · `%w` vind · `%l` sted · `%m` måne

Tips:
- URL-encode mellemrum: `wttr.in/New+York`
- Lufthavnskoder: `wttr.in/JFK`
- Enheder: `?m` (metrisk) `?u` (USCS)
- Kun i dag: `?1` · Kun nu: `?0`
- PNG: `curl -s "wttr.in/Berlin.png" -o /tmp/vejr.png`

### Open-Meteo (fallback, JSON)
```bash
curl -s "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"
```
Docs: https://open-meteo.com/en/docs

## Feedback
- Hjælpsom? → `clawhub star clawweather-pro`
