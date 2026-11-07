---
name: jpverify
description: >-
  JPVerify: Japan business data for AI agents — verify Japanese companies (法人番号), qualified-invoice
  T-numbers (インボイス), invoice issuers and suppliers; OCR Japanese invoices, receipts and business cards;
  normalize and validate Japanese addresses; plus JP PINT e-invoice validation, EU VAT/Peppol, UK and
  SEC cross-border checks. Use when a task involves Japanese business documents or data and you need to
  pick the right check. Paid per call (API key credits or x402); a free guide tool is available.
license: MIT
---

# JPVerify — pick the right Japan business check

Version 1.0.1 · JPVerify · https://www.jpverify.com

Use this skill to route a task to the right JPVerify endpoint. For the common tasks, the focused skills have detailed workflows:

| Task | Skill |
|---|---|
| T-number / qualified-invoice issuer checks | `jp-invoice-number-check` |
| Japanese company, corporate number, filings, FSA licences | `jp-company-verify` |
| Invoice / receipt / business-card OCR | `jp-business-document-ocr` |
| Japanese address normalization, validation, geocoding, postal codes | `jp-address` |
| Supplier / counterparty pre-check before onboarding or payment (JP + UK, EU VAT, Peppol, SEC) | `jp-supplier-due-diligence` |
| JP PINT (Peppol) e-invoice XML validation | `jp-pint-invoice-validation` |

If they are not installed, follow the routing below directly.

## Connect / 接続

JPVerify is a paid, per-call API. Pick the first option that applies; never guess credentials.

1. **API key (recommended).** If the environment has `JPVERIFY_API_KEY` (a `jpv_live_…` key the user created), send it on every call:
   - HTTP: header `Authorization: Bearer $JPVERIFY_API_KEY` (or `X-API-Key`).
   - MCP: if the JPVerify Claude Code plugin is installed, the `jpverify` MCP server is already configured (it reads `JPVERIFY_API_KEY`). Otherwise: `claude mcp add --transport http jpverify https://api.jpverify.com/mcp --header "Authorization: Bearer $JPVERIFY_API_KEY" --header "X-JPVerify-Client: jpverify/1.0.1"`
   Each successful call is deducted from the user's prepaid USD credits; failed or invalid calls are refunded automatically.
2. **x402 wallet.** If you have an x402 client with USDC on Base (`eip155:8453`) and the user approved a budget, call without a key: the API answers HTTP 402 with the exact price; sign and retry with `PAYMENT-SIGNATURE`. Pay only within the approved budget.
3. **Neither.** Do not pay and do not invent a key. The MCP server also works without a key for the free tool `jpverify_guide` (`claude mcp add --transport http jpverify https://api.jpverify.com/mcp`); use it to confirm which call fits, then tell the user they can create a free account with starter credit at https://www.jpverify.com/signup?ref=jpverify and set `JPVERIFY_API_KEY`.

Always send `X-JPVerify-Client: jpverify/1.0.1` on HTTP calls. Never print, log or share the API key.

## Routing / 使い分け

1. **Unsure which call fits?** Ask the free MCP tool `jpverify_guide` with the task in plain words, or use the table below.
2. **Prefer one composite call over several small ones** when it answers the question (e.g. `/jp-invoice/extract-and-verify` instead of OCR + check; `/v1/suppliers/resolve` for a supplier with several identifiers).
3. **Batches:** up to 10 items use the `*-batch` endpoints; larger jobs (up to 1,000) use `/v1/batch-jobs`, which is x402-only and needs a caller-chosen capability token and an `Idempotency-Key` header. Always confirm the total cost with the user first.

## Endpoints and prices / エンドポイントと料金

### Registry verification / 公的データ照合

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-invoice/verify` | `jp_invoice_registration_verify` | $0.01 | You already have a Japanese T+13-digit qualified-invoice registration number. | NTA registration status, corporate number, registered name, and relevant dates. |
| `POST /jp-invoice/check` | `jp_invoice_issuer_check` | $0.03 | You have extracted issuer fields and need T-number, company-name, and address comparison. | OCR issuer fields, NTA registry fields, comparison results, and resolved values; phone is not registry-compared. |
| `POST /jp-invoice/verify-batch` | — | $0.05 | You need up to 10 Japanese T-number checks in one request. | One NTA registration result per T-number. |
| `POST /jp-company/verify` | `jp_company_verify` | $0.005 | You need a Japanese company or corporate-number lookup. | Corporate number, registered legal name/address, active or closed status, and match evidence. |
| `POST /jp-company/report` | — | $0.05 | You need a Japan company registry pre-check with risk flags. | Registry identity, status, evidence, and risk flags; not full KYC/KYB. |
| `POST /jp-company/verify-batch` | — | $0.05 | You need up to 10 Japanese company or corporate-number lookups in one request. | One result per input with match status and registry evidence. |
| `POST /v1/suppliers/resolve` | `jp_supplier_resolve` | $0.01 | You need one coverage-aware supplier check combining company, qualified-invoice, and address evidence; optionally includes projected gBizINFO activity evidence when the internal feature flag is enabled. | Independent evidence checks, source versions, and a resolved/ambiguous/not-found/insufficient-coverage status; optional gBizINFO is projected enrichment inside this response, not a standalone source or raw-response resale. Not a legal or KYB determination. |
| `POST /jp-regulated-entity/verify` | — | $0.03 | You need to verify an entity against the covered Japanese FSA financial instruments, funds transfer, or crypto-asset exchange datasets. | Coverage-aware licensing decision, freshness, identity match, license evidence, and review warnings; not a legal unlicensed determination. |
| `GET /jp-company/filings` | — | $0.01 | You need EDINET filing metadata for a Japanese company by corporate number, EDINET code, or security code. | Filing metadata, correction/withdrawal relationships, freshness, and official evidence references; raw files remain internal. |

### Document OCR / 書類OCR

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-invoice/extract` | `jp_invoice_extract` | $0.01 | You need Japanese billing-invoice OCR and deterministic quality checks without registry lookup. | OCR-derived invoice fields plus format, arithmetic, tax, completeness, and review status. |
| `POST /jp-invoice/extract-and-verify` | `jp_invoice_extract_and_verify` | $0.05 | You need invoice OCR and issuer name/address comparison or completion using NTA public data. | OCR values, registry values, resolved issuer values, validation, and an explicit review signal. |
| `POST /jp-receipt/extract` | `jp_receipt_extract` | $0.03 | You need Japanese receipt or 領収書 OCR with local tax, amount, T-number, and format checks. | Structured receipt fields, deterministic validation, field status, and review signals. |
| `POST /jp-business-card/extract` | `jp_business_card_extract` (enrich=false) | $0.03 | You need only the person, role, department, company, phone, email, or address printed on a Japanese business card. | Card-printed contact fields only; no corporate-number or NTA issuer verification. |
| `POST /jp-business-card/extract-and-enrich` | `jp_business_card_extract` (enrich=true) | $0.10 | You need business-card OCR plus Japanese corporate-number and qualified-invoice enrichment. | Separate card OCR values and registry-resolved company values; registry pre-check, not full KYB. |

### Japanese addresses / 住所

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-address/normalize` | `jp_address_normalize` | $0.005 | You need Japanese address normalization or standardization, whether or not the input contains a postal code. | Normalized prefecture/city/town/chome/block/lot/house components, parser confidence, match hierarchy, geocoder evidence, and postal-code evidence when a postal code is supplied. It does not infer a missing postal code. |
| `POST /jp-address/parse` | — | $0.005 | You need Japanese address components such as prefecture, city, town, chome, block, lot, or house without postal lookup or geocoding. | Parser-only components, normalized value, chome/block/lot/house fields, normalization changes, unparsed fragments, parser status, and parser confidence. Postal and geocoder evidence are not returned. |
| `POST /jp-address/postal-lookup` | — | $0.001 | You need a Japan Post postal-code lookup or reverse lookup from a postal code or administrative address. | Japan Post local-snapshot matches with postal code, prefecture, city, town, kana, confidence, source, data version, and candidate count. |
| `POST /jp-address/geocode` | — | $0.005 | You need Japanese forward-geocoding candidates, coordinates, address IDs, or hierarchy levels. The required hierarchy is inferred from the input. | Provider-neutral Jageocoder candidates with normalized address, coordinates, address ID, match level, granularity, confidence, reasons, unmatched tails, and dictionary status. Level 5/6 is oaza/aza, 7 is block, and 8 is building or house node when covered. City-level or town-prefix candidates remain partial; town-level results are not door-number or coordinate accuracy claims. |
| `POST /jp-address/validate` | `jp_address_validate` | $0.005 | You need one evidence-based Japanese address quality decision combining parsed address, postal evidence, and geocoder evidence. | Exact, partial, ambiguous, conflict, or unverified status with accepted hierarchy, confidence signals, validation scope, and reasons. |

### Cross-border & e-invoicing / 越境・電子インボイス

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /v1/invoices/validate-jp-pint` | — | $0.02 | You need offline validation of a JP PINT 1.1.3 UBL Invoice before accounting or payment workflow acceptance. | Official document_valid from pinned OASIS UBL 2.1 XSD and OpenPeppol JP PINT 1.1.3 Schematron, plus separate decision/trusted fields and optional NTA registry evidence. |
| `POST /v1/invoices/counterparty-check` | `jp_counterparty_check` | $0.05 | You need separate EU VAT validity, returned-name entity matching, and Peppol participant discoverability evidence. | Projected VIES and Peppol evidence only; VIES is known-ID validation and member-state outages are insufficient coverage. |
| `POST /v1/entities/resolve-cross-border` | — | $0.04 | You need a JP or GB entity identity pre-check from one country-routed API; the first release uses NTA/gBizINFO for JP and Companies House for GB. | Projected entity identity, evidence checks, source freshness, coverage, conflicts, and a conservative confidence band; raw upstream responses are never returned. |
| `GET /v1/entities/{cik}/filing-risk-snapshot` | — | $0.05 | You need objective recent SEC EDGAR filing and XBRL availability metadata for a known CIK. | Recent filing metadata and objective disclosure signals; never a credit rating or investment recommendation. |

### Batch / バッチ

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /v1/batch-jobs` | — | per item (x402 only) | You need up to 1,000 structured company, invoice, supplier, or Japanese address operations as one durable paid job with progress and downloadable per-item results. | An owner-scoped job ID, exact operation-based price, payment and execution state, progress counts, and stable per-item results with retry metadata; results are released only after settlement. |

### Request fields / リクエスト項目

| Endpoint | Required fields | Optional fields |
|---|---|---|
| `POST /jp-invoice/verify` | `registration_number` | `response_language` |
| `POST /jp-invoice/check` | `registration_number` | `supplier_name`, `address`, `response_language` |
| `POST /jp-invoice/verify-batch` | `registration_numbers` | `response_language` |
| `POST /jp-company/verify` | — | `name`, `corporate_number`, `address`, `response_language` |
| `POST /jp-company/report` | — | `name`, `corporate_number`, `address`, `response_language` |
| `POST /jp-company/verify-batch` | `items` | `response_language` |
| `POST /v1/suppliers/resolve` | — | `name`, `corporate_number`, `address`, `registration_number`, `t_number`, `country_code`, `identifiers`, `response_language` |
| `POST /jp-regulated-entity/verify` | — | `corporate_number`, `name`, `address`, `phone`, `categories`, `response_language` |
| `GET /jp-company/filings` | — | `corporate_number`, `edinet_code`, `security_code`, `date_from`, `date_to`, `doc_type_code`, `form_code`, `include_withdrawn`, `limit`, `cursor`, `response_language` |
| `POST /jp-invoice/extract` | — | `text`, `image_base64`, `file_url`, `mime_type`, `max_pages`, `response_language`, `fields` |
| `POST /jp-invoice/extract-and-verify` | — | `text`, `image_base64`, `file_url`, `mime_type`, `max_pages`, `response_language`, `fields`, `supplier_name`, `address` |
| `POST /jp-receipt/extract` | — | `text`, `image_base64`, `file_url`, `mime_type`, `max_pages`, `response_language`, `fields` |
| `POST /jp-business-card/extract` | — | `front_image_base64`, `back_image_base64`, `front_image_url`, `back_image_url`, `mime_type`, `max_pages`, `output_format`, `include_raw_text`, `response_language` |
| `POST /jp-business-card/extract-and-enrich` | — | `front_image_base64`, `back_image_base64`, `front_image_url`, `back_image_url`, `mime_type`, `max_pages`, `output_format`, `include_raw_text`, `response_language` |
| `POST /jp-address/normalize` | `address` | `response_language` |
| `POST /jp-address/parse` | `address` | `postal_code`, `response_language`, `parser_profile` |
| `POST /jp-address/postal-lookup` | — | `postal_code`, `prefecture`, `county`, `city`, `ward`, `town`, `max_results` |
| `POST /jp-address/geocode` | — | `address`, `components`, `postal_code`, `max_candidates`, `minimum_acceptable_level`, `provider` |
| `POST /jp-address/validate` | — | `address`, `parsed`, `postal_evidence`, `geocode_evidence`, `required_level`, `strict` |
| `POST /v1/invoices/validate-jp-pint` | `xml` | `registry_enhance` |
| `POST /v1/invoices/counterparty-check` | — | `vat_id`, `participant_id`, `name`, `country_code`, `response_language` |
| `POST /v1/entities/resolve-cross-border` | `country_code` | `name`, `address`, `identifiers`, `response_language` |
| `GET /v1/entities/{cik}/filing-risk-snapshot` | `entity_id` | — |
| `POST /v1/batch-jobs` | `operation` | `items`, `csv_data`, `response_language` |

Where no field is required, send at least one identifier or input (for OCR: `text`, `file_url` or `image_base64`; for business cards: `front_image_url` or `front_image_base64`). `response_language` is `ja`, `en` or `both` (default `both`).

Japanese descriptions and request examples for every endpoint: [references/endpoints.md](references/endpoints.md), [references/examples.md](references/examples.md).

## Reading results / 結果の読み方

- Every registry result names its `source` and the as-of date of the data. Quote them when you report.
- Check `status` / `decision`, `risk_flags` and `manual_review_required` before acting. Ambiguous or multiple matches go back to the user.
- English names and addresses come only from official sources; empty means "not officially available", not an error.

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

## Example / 呼び出し例 (`POST /jp-invoice/verify`)

API key:

```bash
curl -X POST https://api.jpverify.com/jp-invoice/verify \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"registration_number": "T1013301046627", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/verify",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"registration_number": "T1013301046627", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

x402 (no account):

```bash
# No key: shows the HTTP 402 x402 price; pay with an x402 client and retry with PAYMENT-SIGNATURE.
curl -i -X POST https://api.jpverify.com/jp-invoice/verify \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"registration_number": "T1013301046627", "response_language": "both"}'
```

Full SDK examples (Python `x402`, JavaScript `@x402/fetch`): https://api.jpverify.com/docs/x402

## Limits and privacy / 制限とプライバシー

- Results are a **public-registry pre-check** with the source and as-of date of the data. They are not KYB, AML or sanctions screening, and not legal, tax or accounting advice. A "not found" does not mean the entity does not exist or is risky.
- If `manual_review_required` is true or a status is ambiguous, show the evidence to the user and let them decide; do not decide on their behalf.
- Only send documents, images and personal data the user is entitled to process. Do not repeat full personal details (names, phone numbers, e-mail addresses on business cards) back unless the user asked for them.
- Docs: API key https://api.jpverify.com/docs/api-key · x402 https://api.jpverify.com/docs/x402 · terms https://api.jpverify.com/en/terms · privacy https://api.jpverify.com/en/privacy
