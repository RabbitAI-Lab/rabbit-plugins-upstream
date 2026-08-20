---
name: "drt-self-improving-agent"
description: "Self-improving DRT/ICT trading agent — journals every trade (setup type, bias, R:R, outcome), analyzes its own win/loss patterns, and builds a personal trading memory that makes the agent smarter over time."
---

# DRT Self-Improving Trading Agent 🤖📈

En trading-agent der **lærer af sine egne trades**. Hver handel journaliseres → analyseres → mønstre opdages → agenten justerer sine egne regler. Jo flere trades, jo skarpere bliver den.

## Hvad skill'en gør

1. **Journaliserer** hver trade (DRT-type, bias, entry/SL/TP, R:R, udfald, killzone)
2. **Analyserer mønstre** — hvilke setups vinder, hvilke taber, hvornår på dagen
3. **Opbygger hukommelse** — `trades.json` vokser med hver handel
4. **Lærer og justerer** — udskriver ændrede regler baseret på data (ikke mavefornemmelse)
5. **Proaktiv** — minder om killzones og A+ setups
6. **Premium** — kan kalde x402-API for live signaler (valgfrit)

## Filer

```
drt-self-improving-agent/
├── SKILL.md
├── scripts/
│   ├── journal.py      # Tilføj trade til trades.json (CLI)
│   ├── analyze.py      # Analysér mønstre + udskriv læringer
│   └── x402_signal.py  # Hent live signal fra x402-API (premium)
└── data/
    └── trades.json     # Trade-hukommelse (auto-oprettes)
```

## Hurtig start

```bash
# Journaliser en trade (efter hver handel!)
python3 scripts/journal.py --symbol SP500 --bias LONG --type 2 \
  --entry 7741 --sl 7681 --tp 7802 --rr 2.5 --result win --killzone NY

# Se hvad agenten har lært
python3 scripts/analyze.py

# Live signal (premium — kræver x402 API-nøgle)
python3 scripts/x402_signal.py --symbol BTCUSD
```

## Journal-felter

| Felt | Værdi | Forklaring |
|------|-------|-----------|
| `symbol` | SP500, BTCUSD… | Instrument |
| `bias` | LONG / SHORT | Retning |
| `type` | 1, 2, 3 | DRT-type (continuation/reversal/consolidation) |
| `entry` / `sl` / `tp` | pris | Trade-niveauer |
| `rr` | 1.5, 2.0, 3.0 | R:R ved entry |
| `result` | win / loss / be | Udfald |
| `killzone` | London, NY, SB-AM, SB-PM | Hvor handlen blev taget |
| `notes` | tekst | Fri note (fx "sweep 12 barer gammel") |

## Lærings-logik (analyze.py)

Agenten udskriver konkrete læringer, fx:
- "Type 2 LONG vinder 92% — fortsæt med at tage dem"
- "Trades i SB-PM taber 60% — undgå eller skærp filter"
- "R:R < 1.5 giver 40% WR — spring over, vent på 2R+"
- "Når sweep er ældre end 12 barer: 0 vindere — sæt alders-gate"

## Killzone-reminder (proaktiv)

Brug agenten til at minde om handelsvinduer (dansk tid):
- London 09:00-11:00 · NY 14:30-17:00 · SB AM 09:00-10:00 · SB PM 19:30-21:30
- ⛔ Aldrig NY open 15:30-16:00 · max 3 trades/dag · SL ALTID

## Premium (x402-API)

Gratis basis = journal + analyse + læring. Premium-kommandoer kalder
`http://186.240.156.169:8791` (x402 pay-per-call) for live signaler/bias/news.
API-nøgle sættes i miljøvariabel `X402_API_KEY` (se `x402_signal.py --help`).

## Regler der aldrig ændres (også selvom data siger andet)
- Stop loss ALTID · Max 3 trades/dag · Aldrig revenge trade
- Kun A+ setups — 90% WR kræver at man siger nej til 80% af setups
