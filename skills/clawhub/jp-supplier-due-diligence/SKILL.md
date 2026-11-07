---
name: jp-supplier-due-diligence
description: >-
  Run a pre-payment supplier and counterparty check with JPVerify: combine Japanese corporate-number,
  qualified-invoice (T-number) and address evidence for a supplier, add FSA licence and EDINET checks
  when relevant, and for foreign counterparties check UK Companies House, EU VAT (VIES), Peppol
  participant IDs and SEC EDGAR filings. Use when a task involves onboarding a vendor, approving an
  invoice for payment, checking a vendor master in bulk, or deciding whether a counterparty needs
  manual review. Paid per call.
license: MIT
---

# Supplier and counterparty pre-check / 取引先の事前確認

Version 1.0.1 · JPVerify · https://www.jpverify.com

A workflow skill: it chains several JPVerify checks into one evidence summary for a human decision. It does **not** approve payments or vendors by itself.

## When to use / いつ使うか

- Onboarding a Japanese supplier, or approving a Japanese invoice for payment.
- Checking a foreign counterparty (UK company, EU VAT-registered business, Peppol participant, US SEC registrant).
- Preparing an evidence summary for accounts payable, procurement or compliance review.

## Connect / 接続

JPVerify is a paid, per-call API. Pick the first option that applies; never guess credentials.

1. **API key (recommended).** If the environment has `JPVERIFY_API_KEY` (a `jpv_live_…` key the user created), send it on every call:
   - HTTP: header `Authorization: Bearer $JPVERIFY_API_KEY` (or `X-API-Key`).
   - MCP: if the JPVerify Claude Code plugin is installed, the `jpverify` MCP server is already configured (it reads `JPVERIFY_API_KEY`). Otherwise: `claude mcp add --transport http jpverify https://api.jpverify.com/mcp --header "Authorization: Bearer $JPVERIFY_API_KEY" --header "X-JPVerify-Client: jp-supplier-due-diligence/1.0.1"`
   Each successful call is deducted from the user's prepaid USD credits; failed or invalid calls are refunded automatically.
2. **x402 wallet.** If you have an x402 client with USDC on Base (`eip155:8453`) and the user approved a budget, call without a key: the API answers HTTP 402 with the exact price; sign and retry with `PAYMENT-SIGNATURE`. Pay only within the approved budget.
3. **Neither.** Do not pay and do not invent a key. The MCP server also works without a key for the free tool `jpverify_guide` (`claude mcp add --transport http jpverify https://api.jpverify.com/mcp`); use it to confirm which call fits, then tell the user they can create a free account with starter credit at https://www.jpverify.com/signup?ref=jp-supplier-due-diligence and set `JPVERIFY_API_KEY`.

Always send `X-JPVerify-Client: jp-supplier-due-diligence/1.0.1` on HTTP calls. Never print, log or share the API key.

## Workflow / 手順

Collect what you know first: legal name, address, corporate number (法人番号), T-number, and for foreign parties the country, company number, VAT ID, Peppol ID or SEC CIK. Ask the user for missing identifiers rather than guessing them.

**Japanese supplier** (typical cost $0.01–$0.10):
1. `POST /v1/suppliers/resolve` (MCP `jp_supplier_resolve`) with every identifier you have — one call combines corporate-number, T-number and address evidence. Stop here if `decision` is `verified` and the user only needs identity.
2. If an invoice is involved and its issuer details differ from the supplier record: `POST /jp-invoice/check`.
3. Only when relevant to the business: `POST /jp-regulated-entity/verify` (licensed financial businesses) and `GET /jp-company/filings` (listed companies).

**Foreign counterparty** (typical cost $0.04–$0.15):
1. UK company: `POST /v1/entities/resolve-cross-border` with `country_code: "GB"` and `identifiers.company_number` (or a name).
2. EU VAT / Peppol: `POST /v1/invoices/counterparty-check` (MCP `jp_counterparty_check`) with `vat_id` (with country prefix) and/or `participant_id` (`scheme::value`), plus `name` to compare.
3. US listed company: `GET /v1/entities/{cik}/filing-risk-snapshot`.

**Many suppliers:** up to 10 per call with the `*-batch` endpoints, or up to 1,000 in one x402 batch job (`/v1/batch-jobs`, operation `supplier_resolve`). State the count and total price and get approval first.

## Endpoints and prices / エンドポイントと料金

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /v1/suppliers/resolve` | `jp_supplier_resolve` | $0.01 | You need one coverage-aware supplier check combining company, qualified-invoice, and address evidence; optionally includes projected gBizINFO activity evidence when the internal feature flag is enabled. | Independent evidence checks, source versions, and a resolved/ambiguous/not-found/insufficient-coverage status; optional gBizINFO is projected enrichment inside this response, not a standalone source or raw-response resale. Not a legal or KYB determination. |
| `POST /jp-invoice/check` | `jp_invoice_issuer_check` | $0.03 | You have extracted issuer fields and need T-number, company-name, and address comparison. | OCR issuer fields, NTA registry fields, comparison results, and resolved values; phone is not registry-compared. |
| `POST /jp-regulated-entity/verify` | — | $0.03 | You need to verify an entity against the covered Japanese FSA financial instruments, funds transfer, or crypto-asset exchange datasets. | Coverage-aware licensing decision, freshness, identity match, license evidence, and review warnings; not a legal unlicensed determination. |
| `GET /jp-company/filings` | — | $0.01 | You need EDINET filing metadata for a Japanese company by corporate number, EDINET code, or security code. | Filing metadata, correction/withdrawal relationships, freshness, and official evidence references; raw files remain internal. |
| `POST /v1/entities/resolve-cross-border` | — | $0.04 | You need a JP or GB entity identity pre-check from one country-routed API; the first release uses NTA/gBizINFO for JP and Companies House for GB. | Projected entity identity, evidence checks, source freshness, coverage, conflicts, and a conservative confidence band; raw upstream responses are never returned. |
| `POST /v1/invoices/counterparty-check` | `jp_counterparty_check` | $0.05 | You need separate EU VAT validity, returned-name entity matching, and Peppol participant discoverability evidence. | Projected VIES and Peppol evidence only; VIES is known-ID validation and member-state outages are insufficient coverage. |
| `GET /v1/entities/{cik}/filing-risk-snapshot` | — | $0.05 | You need objective recent SEC EDGAR filing and XBRL availability metadata for a known CIK. | Recent filing metadata and objective disclosure signals; never a credit rating or investment recommendation. |

### Request fields / リクエスト項目

| Endpoint | Required fields | Optional fields |
|---|---|---|
| `POST /v1/suppliers/resolve` | — | `name`, `corporate_number`, `address`, `registration_number`, `t_number`, `country_code`, `identifiers`, `response_language` |
| `POST /jp-invoice/check` | `registration_number` | `supplier_name`, `address`, `response_language` |
| `POST /jp-regulated-entity/verify` | — | `corporate_number`, `name`, `address`, `phone`, `categories`, `response_language` |
| `GET /jp-company/filings` | — | `corporate_number`, `edinet_code`, `security_code`, `date_from`, `date_to`, `doc_type_code`, `form_code`, `include_withdrawn`, `limit`, `cursor`, `response_language` |
| `POST /v1/entities/resolve-cross-border` | `country_code` | `name`, `address`, `identifiers`, `response_language` |
| `POST /v1/invoices/counterparty-check` | — | `vat_id`, `participant_id`, `name`, `country_code`, `response_language` |
| `GET /v1/entities/{cik}/filing-risk-snapshot` | `entity_id` | — |

Where no field is required, send at least one identifier or input (for OCR: `text`, `file_url` or `image_base64`; for business cards: `front_image_url` or `front_image_base64`). `response_language` is `ja`, `en` or `both` (default `both`).

Japanese descriptions and request examples for every endpoint: [references/endpoints.md](references/endpoints.md), [references/examples.md](references/examples.md).

## Summarize for the user / 報告のしかた

Report one block per counterparty:
- **Decision signal**: `verified` / `likely_match` → identity confirmed by public data; `ambiguous`, `manual_review`, `not_found_within_coverage`, `insufficient_coverage` → needs a human.
- **Evidence**: which identifiers matched, the registry names and addresses, `risk_flags` / `conflicts`, and each source with its as-of date (`source_versions`, `source_freshness`).
- **Next actions**: use the response's `next_actions` when present (e.g. ask the supplier for a T-number).

Never state that a supplier is "safe", "approved" or "fraudulent". Say what the public data shows and what is missing.

## Errors and spending / エラーと費用

| Response | What to do |
|---|---|
| `200` | Use the result (see "Reading results"). With an API key, `X-JPVerify-Credits-Charged` and `X-JPVerify-Credits-Remaining` show the cost and balance. |
| `401 invalid_api_key` | The key is missing, wrong or revoked. Ask the user to check `JPVERIFY_API_KEY`; do not retry with guesses. |
| `402 insufficient_credits` (API key) | Stop. Nothing was charged. Tell the user to top up at https://www.jpverify.com/account/billing. Do not retry. |
| `402` with x402 payment requirements (no key) | Pay only within the approved budget, using the exact amount in the response. |
| `422` | Invalid input; nothing was charged. Fix the input (the error says which field) and call again once. |
| `5xx` / timeout | Not charged (credits are refunded). Retry once later; then report the failure. |

Spending rules:
- Before a batch call, or any plan that will cost more than **$0.50** in total, state the number of calls and the total price and get the user's go-ahead.
- Do not call the same paid endpoint repeatedly for the same input; reuse the result you already have.
- Prices in the endpoint table are per successful call in USD (the same with an API key or x402).

## Example / 呼び出し例 (`POST /v1/suppliers/resolve`)

API key:

```bash
curl -X POST https://api.jpverify.com/v1/suppliers/resolve \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-supplier-due-diligence/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"name": "株式会社ABC", "registration_number": "T1013301046627", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/v1/suppliers/resolve",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-supplier-due-diligence/1.0.1"},
    json={"name": "株式会社ABC", "registration_number": "T1013301046627", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

x402 (no account):

```bash
# No key: shows the HTTP 402 x402 price; pay with an x402 client and retry with PAYMENT-SIGNATURE.
curl -i -X POST https://api.jpverify.com/v1/suppliers/resolve \
  -H "X-JPVerify-Client: jp-supplier-due-diligence/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"name": "株式会社ABC", "registration_number": "T1013301046627", "response_language": "both"}'
```

Full SDK examples (Python `x402`, JavaScript `@x402/fetch`): https://api.jpverify.com/docs/x402

## Limits and privacy / 制限とプライバシー

- Results are a **public-registry pre-check** with the source and as-of date of the data. They are not KYB, AML or sanctions screening, and not legal, tax or accounting advice. A "not found" does not mean the entity does not exist or is risky.
- If `manual_review_required` is true or a status is ambiguous, show the evidence to the user and let them decide; do not decide on their behalf.
- Only send documents, images and personal data the user is entitled to process. Do not repeat full personal details (names, phone numbers, e-mail addresses on business cards) back unless the user asked for them.
- Docs: API key https://api.jpverify.com/docs/api-key · x402 https://api.jpverify.com/docs/x402 · terms https://api.jpverify.com/en/terms · privacy https://api.jpverify.com/en/privacy
