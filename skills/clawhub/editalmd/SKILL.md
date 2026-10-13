---
name: editalmd
description: Work with Brazilian public procurement (licitações, PNCP) through EditalMD (editalmd.com). Search tenders by product, service and state, read the proposal deadline and the estimated last day to challenge, see which activities (CNAE) usually win, winning prices, valid price-registration minutes (atas) and annual purchase plans. Read a tender document (edital) as Markdown with the qualification requirements and page evidence, and create alerts for new tenders and watches on a purchase. Use when a task mentions licitação, edital, pregão, PNCP, compras públicas, Lei 14.133, ata de registro de preço or selling to the Brazilian government.
license: MIT-0
compatibility: Needs HTTPS access to editalmd.com. Works with the remote MCP server or with plain HTTP calls.
---

# EditalMD

EditalMD collects the public purchases of Brazil from the national procurement portal (PNCP).
Use it to find tenders, check their deadlines and prices, and read the tender documents as Markdown.

## Connect

- MCP server (preferred): `https://editalmd.com/mcp?checkout=site`. Transport: Streamable HTTP. Search and records
  need no key. With `checkout=site`, the person buys on the site and the agent never pays.
- HTTP API: base URL `https://editalmd.com`. Each MCP tool calls one route of this API.
- If the MCP tools are not available, call the HTTP routes with `curl` or with your fetch tool.
- Discovery: `GET https://editalmd.com/api/` lists the routes, prices and limits.
  `https://editalmd.com/llms-full.txt` has the full reference.

## MCP tools

| Tool | HTTP | Use it to | Cost |
|---|---|---|---|
| `buscar_licitacao` | `GET /api/busca` | Find purchases by term (`q`) and state (`uf`). Set `abertas` to keep only open proposals. | Free |
| `compra` | `GET /api/compra/{id}` | Read a purchase: object, agency, value, dates and its documents. | Free |
| `prazos` | `GET /api/compra/{id}` | Read the proposal deadline and the estimated last day to challenge (Lei 14.133, art. 164). | Free |
| `quem_fornece` | `GET /api/compra/{id}/cnaes` | See which activities (CNAE) usually win purchases like this one. | Free |
| `abertas_do_ramo` | `GET /api/compra/{id}/abertas` | List open tenders of the same line of business from the last 7 days. | Free |
| `precos_homologados` | `GET /api/precos` | Get the winning price of a similar item: count, median and range. | Free summary |
| `atas_vigentes` | `GET /api/atas` | Find valid price-registration minutes and see if they accept adhesion. | Free |
| `planos_de_compras` | `GET /api/planos` | See what agencies plan to buy before the tender opens. | Free |
| `exemplos` | `GET /api/exemplos` | Get five processed sample documents. | Free |
| `documento` | `GET /api/documento/{id}` | Read the title, type and page count of a document. | Free |
| `estado_geracao` | `GET /api/documento/{id}/geracao` | Read the price quote (`cotacao`) and the progress of a document. | Free |
| `gerar_markdown` | `POST /api/documento/{id}/geracao` | Get access to one document with the person's prepaid credit. Send the `cotacao` that you read. | Per page |
| `edital_markdown` | `GET /api/documento/{id}/markdown` | Read the document as Markdown with source and hash. Send `acesso_codigo`. | With access |
| `habilitacao` | `POST /api/documento/{id}/habilitacao` | List the qualification requirements with literal excerpts. | With access |
| `documento_dossie` | `GET /api/documento/{id}/dossie` | Read items, requirements, deadlines and obligations with page evidence. | With access |
| `criar_dono` | `POST /api/dono` | Create the owner token `edm_…` for alerts and watches. You see it one time only. | Free |
| `criar_alerta` | `POST /api/alertas` | Create an alert for new tenders by terms and state. | First one free |
| `alerta_por_cnpj` | `POST /api/alertas` | Create alerts from the activities of a company (CNPJ). | First one free |
| `alertas_compras` | `GET /api/alertas/{id}/compras` | Read the tenders that matched an alert. | Free |
| `vigiar_compra` | `POST /api/vigias` | Watch one purchase for a new document, suspension, new deadline or new value. | First one free |
| `vigia_eventos` | `GET /api/vigias/{id}/eventos` | Read the changes of a watched purchase. | Free |
| `pricing` | `GET /api/pricing` | Read the current prices and free allowances. | Free |

## Rules

1. Start with the free tools: search, purchase record, deadlines, suppliers and prices.
2. Before you buy a document, call `estado_geracao`. Show the page count and the total of `cotacao` to the user.
   Call `gerar_markdown` only after the user approves that amount.
3. Each buyer pays for its own access. `gerar_markdown` returns a private `acesso_codigo`.
   Keep it and send it to the reading tools. With it, you open the document again at no cost.
4. If `gerar_markdown` returns HTTP 202, wait for the time in `Retry-After`. Then read `estado_geracao` (GET).
   Do not send the POST again to check the progress.
5. Alerts and watches need the owner token. Create it once with `criar_dono` and keep it secret.
   Send it as header `Authorization: Bearer edm_…` (HTTP request or MCP connection header).
6. Never pay by yourself. If a call returns HTTP 402, show the price and https://editalmd.com/pricing to the
   user. The person buys on the site. After the purchase, send the same call again with the person's prepaid
   credit token (`credito_token` argument or header `X-Credito: cred_…`). Keep the same `idempotencia` value
   when you retry.
7. Keep tokens (`cred_…`, `edm_…`, `whsec_…`) and access codes secret. Do not write them in files, logs or
   answers unless the user asks you to save them.
8. The challenge deadline is an estimate: 3 business days before the session, with national holidays only.
   Tell the user to confirm it in the tender document.
9. A missing or partial dossier does not mean that the tender has no requirements. Read its coverage fields.
10. Lists return up to 20 items per page. Follow the next-page links. Do not scrape HTML pages.
11. If you get HTTP 429 or 503, wait for the time in `Retry-After` and try once more.

## Free evaluation for agents

An agent can test the document service without payment: one sponsored premium document and up to 100 basic
reads, up to 50 pages each, for a limited time. The guide is https://editalmd.com/avaliacao.md.
The tools are `avaliacao_cotas`, `avaliacao_premium` and `avaliacao_basico`.

## Buy

- The person buys on the site: https://editalmd.com/pricing shows the plans and the prepaid credit, with the
  prices. Plans do not renew automatically.
- `pricing` and `estado_geracao` read the prices and the quote. They do not charge.
- A prepaid credit gives a `cred_…` token one time only. The same token works in EditalMD, Radar CNPJ and
  PontoFato.

## Examples

```bash
# Tenders for school uniforms in São Paulo state (free)
curl -s 'https://editalmd.com/api/busca?q=uniforme%20escolar&uf=SP'

# Purchase record with deadlines and documents (free)
curl -s https://editalmd.com/api/compra/28870493

# Winning price summary of a similar item (free)
curl -s 'https://editalmd.com/api/precos?q=papel%20A4'
```

## Limits

- The source is PNCP. A purchase in the data can be closed already: read `prazos` before you act.
- The Markdown comes from the original files. Automatic review has quality indicators but does not certify
  that the text is identical to the original.
- Terms: https://editalmd.com/termos. Privacy: https://editalmd.com/privacidade.
  Contact: contato@editalmd.com.
