---
name: jp-business-document-ocr
description: >-
  Read Japanese business documents with JPVerify: billing invoice (請求書) OCR, receipt (領収書・レシート)
  OCR and business card (名刺) OCR into structured JSON, with local checks of dates, tax, totals and
  T-numbers, and optional verification of the issuer against National Tax Agency registries. Use when a
  task involves extracting fields from a Japanese invoice, receipt or business card image, PDF or text.
  Paid per call (API key credits or x402).
license: MIT
---

# Japanese invoice, receipt and business-card OCR / 請求書・領収書・名刺のOCR

Version 1.0.9 · JPVerify · https://www.jpverify.com

## When to use / いつ使うか

- Extract fields from a Japanese **billing invoice** (請求書), **receipt** (領収書・レシート) or **business card** (名刺).
- Check an invoice's arithmetic, consumption tax and T-number format, and optionally confirm the issuer in the NTA registry.

Inputs: plain text (`text`), an HTTPS file URL (`file_url`; business cards: `front_image_url` / `back_image_url`), or a small Base64 file (`image_base64`; cards: `front_image_base64`). Prefer a URL for large files. `mime_type` is optional (inferred when omitted); accepted types are `application/pdf`, `image/jpeg`, `image/png`, `image/heif`, `image/tiff` and `image/webp`.

## Connect / 接続

JPVerify is a paid, per-call API. Pick the first option that applies; never guess credentials.

1. **API key (recommended).** If the environment has `JPVERIFY_API_KEY` (a `jpv_live_…` key the user created), send it on every call:
   - HTTP: header `Authorization: Bearer $JPVERIFY_API_KEY` (or `X-API-Key`).
   - MCP: if the JPVerify Claude Code plugin is installed, the `jpverify` MCP server is already configured and uses the key saved in the plugin's settings (`/plugin` → JPVerify → Configure), not `JPVERIFY_API_KEY`. Otherwise: `claude mcp add --transport http jpverify https://api.jpverify.com/mcp --header "Authorization: Bearer $JPVERIFY_API_KEY" --header "X-JPVerify-Client: jp-business-document-ocr/1.0.9"`
   Each successful call is deducted from the user's prepaid USD credits; failed or invalid calls are refunded automatically.
2. **x402 wallet.** If you have an x402 client with USDC on Base (`eip155:8453`) and the user approved a budget, call without a key: the API answers HTTP 402 with the exact price; sign and retry with `PAYMENT-SIGNATURE`. Pay only within the approved budget.
3. **Neither.** Do not pay and do not invent a key. The MCP server also works without a key for the free tool `jpverify_guide` (`claude mcp add --transport http jpverify https://api.jpverify.com/mcp`); use it to confirm which call fits, then tell the user they can create a free account with starter credit at https://www.jpverify.com/signup?ref=jp-business-document-ocr and set `JPVERIFY_API_KEY`.

Always send `X-JPVerify-Client: jp-business-document-ocr/1.0.9` on HTTP calls. Never print, log or share the API key.

## Workflow / 手順

1. **Confirm the document type** (invoice vs receipt vs business card) and that the user may share it. Business cards contain personal data.
2. **Choose the call.**
   - Invoice, fields and local checks only → `POST /jp-invoice/extract` (MCP `jp_invoice_extract`).
   - Invoice + issuer verification in the NTA registry, or the question "can we deduct the input consumption tax on this invoice?" → `POST /jp-invoice/extract-and-verify` (one call; do not also call `/jp-invoice/check`).
   - Receipt → `POST /jp-receipt/extract` (a T-number found on the receipt is verified).
   - Business card → `POST /jp-business-card/extract`; add company registry enrichment with `POST /jp-business-card/extract-and-enrich` only if the user needs the corporate number or invoice registration.
3. **Report** the extracted fields together with their status, and list anything that needs review.

## Endpoints and prices / エンドポイントと料金

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-invoice/extract` | `jp_invoice_extract` | $0.03 | You need Japanese billing-invoice OCR and deterministic quality checks without registry lookup. | OCR-derived invoice fields plus format, arithmetic, tax, completeness, and review status. |
| `POST /jp-invoice/extract-and-verify` | `jp_invoice_extract_and_verify` | $0.10 | You need invoice OCR and issuer name/address comparison or completion using NTA public data. | OCR values, registry values, resolved issuer values, validation, an explicit review signal, and invoice_eligibility (eligible / not_eligible / needs_review for input tax credit, with the seven qualified-invoice items and registration on the transaction date). |
| `POST /jp-receipt/extract` | `jp_receipt_extract` | $0.03 | You need Japanese receipt or 領収書 OCR with local tax, amount, T-number, and format checks. | Structured receipt fields, deterministic validation, field status, and review signals. |
| `POST /jp-business-card/extract` | `jp_business_card_extract` (enrich=false) | $0.03 | You need only the person, role, department, company, phone, email, or address printed on a Japanese business card. | Card-printed contact fields only; no corporate-number or NTA issuer verification. |
| `POST /jp-business-card/extract-and-enrich` | `jp_business_card_extract` (enrich=true) | $0.10 | You need business-card OCR plus Japanese corporate-number and qualified-invoice enrichment. | Separate card OCR values and registry-resolved company values; registry pre-check, not full KYB. |

### Request fields / リクエスト項目

| Endpoint | Required fields | Optional fields |
|---|---|---|
| `POST /jp-invoice/extract` | — | `text`, `image_base64`, `file_url`, `mime_type`, `max_pages`, `response_language`, `fields` |
| `POST /jp-invoice/extract-and-verify` | — | `text`, `image_base64`, `file_url`, `mime_type`, `max_pages`, `response_language`, `fields`, `supplier_name`, `address` |
| `POST /jp-receipt/extract` | — | `text`, `image_base64`, `file_url`, `mime_type`, `max_pages`, `response_language`, `fields` |
| `POST /jp-business-card/extract` | — | `front_image_base64`, `back_image_base64`, `front_image_url`, `back_image_url`, `mime_type`, `max_pages`, `output_format`, `include_raw_text`, `response_language` |
| `POST /jp-business-card/extract-and-enrich` | — | `front_image_base64`, `back_image_base64`, `front_image_url`, `back_image_url`, `mime_type`, `max_pages`, `output_format`, `include_raw_text`, `response_language` |

Where no field is required, send at least one identifier or input (for OCR: `text`, `file_url` or `image_base64`; for business cards: `front_image_url` or `front_image_base64`). `response_language` is `ja`, `en` or `both` (default `both`).

Japanese descriptions and request examples for every endpoint: [references/endpoints.md](references/endpoints.md), [references/examples.md](references/examples.md).

## Reading results / 結果の読み方

- `validation.status` is the overall result (`passed`, or a status needing attention); `validation.checks` lists each check (required fields, T-number format, date, arithmetic, tax).
- `field_status` says how each field is supported: `ocr_only` (read but not cross-checked), `format_valid`, `corroborated` (consistent with other fields), etc. Treat `ocr_only` values as unconfirmed.
- If `manual_review_required` is true, show the fields and the failing checks to the user; do not "fix" amounts or numbers yourself.
- `invoice_eligibility` (extract-and-verify) answers input-tax-credit eligibility: `eligible`, `not_eligible` (the issuer was not registered on the transaction date, or the T-number is invalid) or `needs_review` (an item was not read). `requirements` lists the seven qualified-invoice items; `summary_en` is a one-line conclusion for the user. It is an evidence check, not tax advice — a missing item may be printed but unread, and transitional deductions for non-registered suppliers are not evaluated.
- With business cards, printed values (`card`) and registry values (enrichment) are kept separate; do not merge them silently.

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

## Example / 呼び出し例 (`POST /jp-invoice/extract`)

API key:

```bash
curl -X POST https://api.jpverify.com/jp-invoice/extract \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-business-document-ocr/1.0.9" \
  -H "Content-Type: application/json" \
  -d '{"text": "請求書 株式会社ABC 登録番号 T1013301046627 請求日 2026年8月15日 支払期日 2026年9月30日 合計110000円 消費税10000円", "fields": ["supplier_name", "registration_number", "invoice_date", "due_date", "total", "tax_amount", "payment_terms"], "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/extract",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-business-document-ocr/1.0.9"},
    json={"text": "請求書 株式会社ABC 登録番号 T1013301046627 請求日 2026年8月15日 支払期日 2026年9月30日 合計110000円 消費税10000円", "fields": ["supplier_name", "registration_number", "invoice_date", "due_date", "total", "tax_amount", "payment_terms"], "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

x402 (no account):

```bash
# No key: shows the HTTP 402 x402 price; pay with an x402 client and retry with PAYMENT-SIGNATURE.
curl -i -X POST https://api.jpverify.com/jp-invoice/extract \
  -H "X-JPVerify-Client: jp-business-document-ocr/1.0.9" \
  -H "Content-Type: application/json" \
  -d '{"text": "請求書 株式会社ABC 登録番号 T1013301046627 請求日 2026年8月15日 支払期日 2026年9月30日 合計110000円 消費税10000円", "fields": ["supplier_name", "registration_number", "invoice_date", "due_date", "total", "tax_amount", "payment_terms"], "response_language": "both"}'
```

Full SDK examples (Python `x402`, JavaScript `@x402/fetch`): https://api.jpverify.com/docs/x402

## Limits and privacy / 制限とプライバシー

- Results are a **public-registry pre-check** with the source and as-of date of the data. They are not KYB, AML or sanctions screening, and not legal, tax or accounting advice. A "not found" does not mean the entity does not exist or is risky.
- If `manual_review_required` is true or a status is ambiguous, show the evidence to the user and let them decide; do not decide on their behalf.
- Only send documents, images and personal data the user is entitled to process. Do not repeat full personal details (names, phone numbers, e-mail addresses on business cards) back unless the user asked for them.
- Docs: API key https://api.jpverify.com/docs/api-key · x402 https://api.jpverify.com/docs/x402 · terms https://api.jpverify.com/en/terms · privacy https://api.jpverify.com/en/privacy
