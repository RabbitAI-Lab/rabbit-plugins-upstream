# Northcap Crypto Signals API (x402)

**Formål:** Betalt pay-per-call API med DRT-baserede krypto-signaler (LONG/SHORT med entry, SL, TP, R:R). Designet til AI-agenter der vil automatisere krypto-trading — betal pr. kald med USDC via x402.

## Hvorfor bruge denne skill?
- **Backtestet strategi**: DRT (Dealing Range Theory) + ICT — 90%+ winrate på ≥5×ATR-setups (2.531 trades backtestet)
- **Færdige signaler**: du behøver ikke analysere charts selv — få entry/SL/TP/R:R direkte
- **Betaling via x402**: standard-protokol — din agent betaler USDC, får adgang med det samme

## API-detaljer
- **Base-URL**: `http://186.240.156.169:8791`
- **Manifest**: `/.well-known/x402` (agent-discovery-standard)
- **Pris**: $0,005 pr. kald · $25/md ubegrænset
- **Betaling**: USDC på Base/Ethereum/BSC til wallet `0xafd1c6bC2B35152f30E3D0dBE99eE1d40E5a5CF8`
- **Auth**: `X-API-Key` header (nøgle udstedes efter betaling)

## Sådan bruger du det (agent-flow)
1. **Opdag**: `GET /.well-known/x402` → se priser + endpoints
2. **Betal**: send USDC → `POST /v1/purchase` med `{"txHash": "0x...", "chain": "base", "amountUsd": 0.005}` → få API-nøgle
3. **Hent signaler**: `GET /v1/signals?symbol=BTCUSDT&limit=10` med `X-API-Key: <nøgle>`
4. **Svar-format**:
```json
{"provider":"Northcap/Jarvis","count":2,"signals":[
  {"symbol":"BTCUSDT","direction":"LONG","entry":62526.73,"sl":62356.55,"tp":63995.46,"rr":1.8}
]}
```

## Endpoints
| Endpoint | Metode | Beskrivelse |
|---|---|---|
| `/.well-known/x402` | GET | Manifest (discovery) |
| `/health` | GET | Status + antal signaler |
| `/v1/purchase` | POST | Køb adgang (txHash → API-nøgle) |
| `/v1/signals` | GET | Hent signaler (kræver X-API-Key) |

## Signaler i databasen
- 160+ signaler fra premium_90_bot (LTC, XRP, BNB, DOGE, ADA, BTC, ETH, SOL + flere)
- Felter: symbol, direction, entry, sl, tp, rr, sent_at, status (OPEN/TP_RAMT/SL_RAMT), result_r

## Regler
- Ingen garanti for profit — trading er risikabelt
- Per-call-nøgler: 1 kald pr. betaling · Monthly: ubegrænset
- Tx-hash verificeres manuelt (v1) — nøgle aktiveres inden for få minutter

## Ejer
Northcap Group · Agent: Jarvis · Wallet: `0xafd1c6bC2B35152f30E3D0dBE99eE1d40E5a5CF8`
