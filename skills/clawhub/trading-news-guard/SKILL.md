---
name: "trading-news-guard"
description: "News blackout check before trading: avoid trading into NFP/CPI/FOMC and other high-impact events. Calendar integration, countdown warnings, and safe-window logic for ICT/SMC traders."
---

# Trading News Guard 🛡️📰

Beskyt din agent mod at trade ind i news-spikes. Ét API-kald før hvert entry = ingen flere NFP/CPI/FOMC-ambushes.

## Hvorfor det er kritisk

Høj-påvirknings-news (NFP, CPI, FOMC, ECB) kan flytte markedet 50-200+ point på få sekunder. Selv perfekte DRT/ICT-setups bliver kørt over, hvis man er i position under en news-candle. Professionelle tradere lukker positioner eller venter — din agent skal gøre det samme.

## Kommando

```bash
# 1) Sæt din API-nøgle (fås på https://github.com/MohamedAbdisamed/x402-api)
export X402_API_KEY=***

# 2) Tjek news-status FØR entry
python3 scripts/news_check.py
```

## Output (eksempel)

```json
{
  "status": "blackout" | "clear",
  "current_event": "CPI m/m — High Impact",
  "next_events": [
    {"name": "FOMC Statement", "impact": "High", "time": "19:00 UTC"}
  ]
}
```

## Brug i din agent (pseudo-kode)

```python
news = check_news()                      # kalder API'et
if news["status"] == "blackout":
    skip_trade("News blackout: " + news["current_event"])
else:
    place_trade()                        # kun når markedet er klart
```

## Betaling

Pay-per-call via x402 (USDC på Base/Ethereum/BSC). Betal pr. kald — ingen abonnement nødvendig for sporadisk brug. Bulk-brugere kan vælge månedsplan.

## Filer

```
trading-news-guard/
├── SKILL.md
└── scripts/
    └── news_check.py   # x402-klient: GET /v1/news
```

## Regler
- Tjek ALTID news før entry — især i London/NY-vinduer (08:00-17:00 DK)
- Blackout = ingen ny position. Perioden varer typisk 5-30 min omkring eventet
- Undtagelse: hvis din strategi eksplicit handler news (ikke DRT/ICT) — så brug denne skill til at VIDE hvornår det sker
