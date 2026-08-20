---
name: "crypto-sentiment-pulse"
description: "Crypto Fear & Greed-index + markedssentiment via x402 pay-per-call API. Kend markedets humør før din agent tager en position. Perfekt til at filtrere FOMO-trades og timing entries. ⚠️ BETALT API-kald: hver kørsel koster penge (x402, USDC) og sender din API-nøgle til API'et."
metadata: {"crypto-sentiment-pulse": {"requires": {"python3": true, "network": ["https://186.240.156.169:8791", "https://api.telegram.org"], "env": ["X402_API_KEY", "X402_BASE"]}}}
---

# Crypto Sentiment Pulse 💓🪙

Markedssentiment til din agent: Fear & Greed-index og stemningsdata før entries.

## Kommando

```bash
export X402_API_KEY=sk-...
python3 scripts/sentiment.py
```

Returnerer: Fear & Greed-score (0-100) + etikette (Extreme Fear / Fear / Neutral / Greed / Extreme Greed).

## Betaling
Pay-per-call via x402 (USDC på Base).

## ⚠️ Sikkerhed & omkostning (vigtig — læs før brug)

- **Betalt kald:** `sentiment.py` laver et **x402 pay-per-call** — det koster penge pr. kørsel, og din **API-nøgle sendes til API'et**. Kør kun når du bevidst vil hente sentiment.
- **HTTPS:** Nøglen sendes kun over HTTPS. Brug `X402_BASE=https://...` for egen endpoint. HTTP kræver eksplicit `X402_ALLOW_HTTP=1` (kun sikkert/lokalt netværk).
- **Hemmeligheder:** Sæt `X402_API_KEY` i miljøet — aldrig i scripts, logs eller git.

## Hvordan det hjælper
- Extreme Fear (0-25): historisk gode købszoner for longs
- Extreme Greed (75-100): risiko for korrektion — vær forsigtig med longs
- Kombinér med DRT-signaler for A+ setups
