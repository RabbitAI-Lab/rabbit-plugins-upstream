---
name: tools-marcomuratore
description: Dati ufficiali italiani e servizi AI per agenti AI. Tassi BCE, cambi EUR, aliquote IVA, validita' delle partite IVA (VIES), codici ATECO 2025, elenco comuni ISTAT, liste di riferimento, bandi pubblici italiani e inferenza LLM, serviti via API a pagamento per chiamata con x402 (USDC su Solana o Base) o con credito prepagato. Usalo quando ti serve un dato amministrativo italiano verificabile, un bando pubblico strutturato o una chiamata di inferenza.
license: MIT
---

# tools.marcomuratore.work — dati di riferimento per agenti

API che espone dati ufficiali italiani e bandi pubblici, a pagamento per
chiamata. Ogni valore esce con **la fonte da cui e' stato verificato**, **la
data di entrata in vigore** e **la data dell'ultimo controllo**: la risposta
si puo' auditare invece di fidarsene.

Base: `https://tools.marcomuratore.work`

**Contratto API**: `GET /openapi.json` (OpenAPI 3.0) e' lo schema stabile e
letto dai valori reali (prezzi, reti, campi, tipi nullable): se serve
sapere la forma esatta di una risposta o il flusso di pagamento, parte di li.

## Endpoint a pagamento

| Endpoint | Prezzo | Cosa restituisce |
|---|---|---|
| `POST /v1/chat` | $0,01 / €0,01 | una chiamata di inferenza su un pool di modelli |
| `GET /v1/itaref` | $0,005 / €0,005 | tassi BCE, cambi, aliquote IVA, partite IVA |
| `GET /v1/bandi` | $0,005 / €0,005 | bandi pubblici italiani in JSON |

Gratis, senza pagamento: `/health`, `/pool`, `/itaref`, `/bandi`,
`/bandi/storico`, `/concorsi`, `/comuni`, `/ateco`, `/riferimenti`,
`/fonti`, `/v1/prezzi`, `/v1/saldo`, `/vendita`, `/salute`, `/giudizio`,
`/mercato` (domanda misurata dei servizi pagati dagli agenti),
`/giornaliera` (operazioni e incassi delle ultime 24 ore),
`/v1/partita-iva/<codice>` (verifica VIES: valida, denominazione,
indirizzo; massimo 10 verifiche all'ora per indirizzo),
`/openapi.json`.

## Come si paga

Due strade indipendenti. La prima non richiede nessun account.

### 1. x402 — USDC, senza account (consigliata per gli agenti)

Il client riceve `402 Payment Required` con l'header `PAYMENT-REQUIRED`
(base64 del `PaymentRequired`), firma il pagamento (EIP-3009) e ripete la
richiesta con l'header `PAYMENT-SIGNATURE`. Il server verifica il pagamento
con il facilitator, esegue il servizio e regola il pagamento on-chain; la
risposta porta l'header `PAYMENT-RESPONSE`.

La sfida contiene una voce `accepts` per ogni rete accettata: **Solana**
(rete primaria, fee ~0,00001 USD) e **Base**. Il client sceglie quella che
sa pagare.

```python
from x402 import x402ClientSync
from x402.http import PaymentRoundTripper, x402HTTPClientSync
from x402.mechanisms.evm.exact import ExactEvmScheme
from eth_account import Account

client = x402ClientSync()
client.register("eip155:8453", ExactEvmScheme(signer=Account.from_key("0x...")))
rt = PaymentRoundTripper(x402HTTPClientSync(client))

risposta = rt.get("https://tools.marcomuratore.work/v1/itaref")
print(risposta.json())
```

```bash
# il pagamento si fa in due tempi: prima si vede la sfida
curl -s https://tools.marcomuratore.work/v1/itaref -D - -o /dev/null | grep -i payment-required
# poi si ripete con l'header PAYMENT-SIGNATURE
```

### 2. Credito prepagato — carta, per chi non ha un wallet

```bash
curl -s -X POST https://tools.marcomuratore.work/v1/acquisto \
  -H 'Content-Type: application/json' -d '{"importo_eur": 10}'
# -> {"id": "cs_...", "url": "https://checkout.stripe.com/...", "api_key": "agents_live_..."}

curl -s https://tools.marcomuratore.work/v1/itaref \
  -H 'Authorization: Bearer agents_live_...'
```

La chiave API si vede una volta sola e viene conservata solo come hash.
`GET /v1/saldo` restituisce saldo e movimenti.

## MCP

Server MCP con **11 tool** e pagamento x402 nativo:
`https://tools.marcomuratore.work/mcp` (transport streamable-http).

| tool | a pagamento | cosa restituisce |
|---|---|---|
| `itaref` | si ($0,005) | tassi BCE, cambi, aliquote IVA, partite IVA |
| `bandi` | si ($0,005) | bandi pubblici italiani strutturati |
| `chat` | si ($0,01) | una chiamata di inferenza sul pool |
| `comuni` | no | comuni ISTAT: codice a 6 cifre, provincia, regione, coordinate (filtri: comune, provincia, regione, n) |
| `comuni_codice` | no | un comune per codice ISTAT o per nome |
| `ateco` | no | codici ATECO 2025 con titolo IT/EN (filtri: livello, padre, q, n) |
| `ateco_codice` | no | un codice ATECO per codice |
| `riferimenti` | no | liste di dati di riferimento italiani (con o senza `lista`) |
| `giudizio` | no | quanto e' attendibile ogni dataset, con l'auto-audit del giudice |
| `bandi_storico` | no | storico append-only dei bandi (n, da, q, fonte) |
| `mercato` | no | il radar: domanda misurata del mercato e lacune |
| `partita_iva` | no | verifica di una partita IVA con VIES (valida, denominazione, indirizzo) |

```python
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from x402.mcp import create_x402_mcp_client_from_config
from x402.mechanisms.svm.exact import ExactSvmScheme

async def main():
    async with streamablehttp_client("https://tools.marcomuratore.work/mcp") as (r, w, _):
        async with ClientSession(r, w) as session:
            await session.initialize()
            client = create_x402_mcp_client_from_config(session, {
                "schemes": [{"network": "solana:5eykt4UsF...",
                             "client": ExactSvmScheme(signer=...)}],
                "auto_payment": True,
                "on_payment_requested": lambda ctx: True,
            })
            risultato = await client.call_tool("itaref", {})
            print(risultato.content[0].text)
```

**Attenzione alla versione di `mcp`.** Con `mcp` 1.30 l'SDK x402 2.29.0 ha il
client rotto: chiama `session.call_tool(dict)` mentre 1.30 vuole
`(name, arguments, meta=...)`, e legge `is_error` mentre ora è `isError`.
Il lato **server** non è interessato. Due rimedi:

- importare `x402_mcp_compat` (modulo del progetto) e chiamare
  `x402_mcp_compat.apply()` una volta prima di usare il client;
- applicare la patch `patches/x402-2.29.0-mcp-1.30.patch` all'SDK
  installato (`patch -p1`), che è già applicata nei venv del server.

Con `mcp` 1.30 il client **sincrono** non è utilizzabile (la sessione
sincrona non esiste più): va usato quello asincrono.

Un esempio completo e pronto all'uso: `mcp_client_demo.py` sul server
(`itaref`, `bandi`, `chat`; `--rete solana|base`).

## Formato delle risposte

`GET /v1/itaref` e `GET /v1/bandi` restituiscono:

```json
{"items": [{"chiave": "...", "valore": "...", "fonte": "https://...",
            "effective_from": "2026-01-01", "verified_at": "2026-11-27"}]}
```

## Regole d'uso

- Non chiamare gli endpoint a pagamento in un loop: ogni chiamata costa.
- La risposta e' verificabile: se un valore sembra strano, guarda `fonte`,
  `effective_from` e `verified_at` prima di usarlo.
- Se una call torna `402` con `saldo_eur`, il credito prepagato e' finito:
  si ricarica con `POST /v1/acquisto`.
- Per lo stato del servizio: `GET /health` e `GET /pool` (quota residua).
