---
name: jp-invoice-number-check
description: >-
  Check Japanese qualified-invoice registration numbers (T-numbers, 適格請求書発行事業者登録番号,
  インボイス登録番号) against the National Tax Agency registry with JPVerify, and compare an
  invoice issuer's name and address with the registered record. Use when a task involves
  verifying a T-number, checking whether a Japanese supplier can issue qualified invoices,
  confirming who issued a Japanese invoice, or matching an invoice to a supplier's expected
  T-number or corporate number from master data (AP / vendor checks). Paid per call (API key
  credits or x402).
license: MIT
---

# Japanese T-number check / インボイス登録番号の確認

Version 1.0.9 · JPVerify · https://www.jpverify.com

## When to use / いつ使うか

- You have a T-number (`T` + 13 digits) and need to know whether it is registered and active.
- You have an invoice's issuer name/address and T-number and need to know whether they belong together.
- You have up to 10 T-numbers to check at once.
- You need to know whether an invoice really comes from a supplier in your master data, and you have that supplier's expected T-number or corporate number.

For general invoice OCR use the `jp-business-document-ocr` skill. The one exception here is `/v1/invoices/issuer-match/extract`, which reads the invoice itself and then matches the issuer to your supplier master data.

## Connect / 接続

JPVerify is a paid, per-call API. Pick the first option that applies; never guess credentials.

1. **API key (recommended).** If the environment has `JPVERIFY_API_KEY` (a `jpv_live_…` key the user created), send it on every call:
   - HTTP: header `Authorization: Bearer $JPVERIFY_API_KEY` (or `X-API-Key`).
   - MCP: if the JPVerify Claude Code plugin is installed, the `jpverify` MCP server is already configured and uses the key saved in the plugin's settings (`/plugin` → JPVerify → Configure), not `JPVERIFY_API_KEY`. Otherwise: `claude mcp add --transport http jpverify https://api.jpverify.com/mcp --header "Authorization: Bearer $JPVERIFY_API_KEY" --header "X-JPVerify-Client: jp-invoice-number-check/1.0.9"`
   Each successful call is deducted from the user's prepaid USD credits; failed or invalid calls are refunded automatically.
2. **x402 wallet.** If you have an x402 client with USDC on Base (`eip155:8453`) and the user approved a budget, call without a key: the API answers HTTP 402 with the exact price; sign and retry with `PAYMENT-SIGNATURE`. Pay only within the approved budget.
3. **Neither.** Do not pay and do not invent a key. The MCP server also works without a key for the free tool `jpverify_guide` (`claude mcp add --transport http jpverify https://api.jpverify.com/mcp`); use it to confirm which call fits, then tell the user they can create a free account with starter credit at https://www.jpverify.com/signup?ref=jp-invoice-number-check and set `JPVERIFY_API_KEY`.

Always send `X-JPVerify-Client: jp-invoice-number-check/1.0.9` on HTTP calls. Never print, log or share the API key.

## Workflow / 手順

1. **Normalize the number.** Accept `T1234567890123`, `t1234567890123` or full-width digits; send it as `T` + 13 ASCII digits. If there are not 13 digits, ask the user instead of guessing; a malformed number returns `422` and is not charged.
2. **Choose the call.**
   - Number only → `POST /jp-invoice/verify` (MCP `jp_invoice_registration_verify`).
   - Number + issuer name and/or address from an invoice → `POST /jp-invoice/check` (MCP `jp_invoice_issuer_check`). It also verifies the number, so do not call both.
   - 2–10 numbers → `POST /jp-invoice/verify-batch` (one call, fixed price). For more than 10, tell the user the cost first.
   - The question is whether the invoice comes from a supplier in the user's master data (the user has the supplier's expected T-number or corporate number) → `POST /v1/invoices/issuer-match` (MCP `jp_invoice_issuer_match`) with the printed values in `document` and the master-data identifier in `expected`. If JPVerify should read the invoice image, PDF or text itself, use `POST /v1/invoices/issuer-match/extract` (MCP `jp_invoice_issuer_match_extract`) instead; it runs OCR and does not accept issuer overrides. Do not also call `/jp-invoice/check`.
3. **Report** the status, the registered name, the registration (and any cancel/expiry) date, and the `data_as_of` date of the registry snapshot.

## Endpoints and prices / エンドポイントと料金

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-invoice/verify` | `jp_invoice_registration_verify` | $0.01 | You already have a Japanese T+13-digit qualified-invoice registration number. | NTA registration status, corporate number, registered name, and relevant dates. |
| `POST /jp-invoice/check` | `jp_invoice_issuer_check` | $0.03 | You have extracted issuer fields and need T-number, company-name, and address comparison. | OCR issuer fields, NTA registry fields, comparison results, and resolved values; phone is not registry-compared. |
| `POST /jp-invoice/verify-batch` | — | $0.08 | You need up to 10 Japanese T-number checks in one request. | One NTA registration result per T-number. |
| `POST /v1/invoices/issuer-match` | `jp_invoice_issuer_match` | $0.05 | Match structured invoice fields against supplier master data. | Issuer decision and separate document, expected and registry evidence. |
| `POST /v1/invoices/issuer-match/extract` | `jp_invoice_issuer_match_extract` | $0.10 | Read an invoice document before matching it against supplier master data. | Issuer decision and separate document, expected and registry evidence. |

### Request fields / リクエスト項目

| Endpoint | Required fields | Optional fields |
|---|---|---|
| `POST /jp-invoice/verify` | `registration_number` | `response_language` |
| `POST /jp-invoice/check` | `registration_number` | `supplier_name`, `address`, `response_language` |
| `POST /jp-invoice/verify-batch` | `registration_numbers` | `response_language` |
| `POST /v1/invoices/issuer-match` | `document` | `supplier_id`, `client_reference`, `expected`, `response_language` |
| `POST /v1/invoices/issuer-match/extract` | — | `supplier_id`, `client_reference`, `expected`, `text`, `image_base64`, `file_url`, `mime_type`, `max_pages`, `response_language`, `fields` |

Where no field is required, send at least one identifier or input (for OCR: `text`, `file_url` or `image_base64`; for business cards: `front_image_url` or `front_image_base64`). `response_language` is `ja`, `en` or `both` (default `both`).

Japanese descriptions and request examples for every endpoint: [references/endpoints.md](references/endpoints.md), [references/examples.md](references/examples.md).

## Reading results / 結果の読み方

- `/jp-invoice/verify`: `status` is `registered`, `registered_until_expiry`, `expired`, `cancelled`, `deleted` or `not_found`; `verdict` is `qualified` only while the registration is valid. `format_valid` / `checksum_valid` false means the number itself is wrong (check for a typo before concluding anything).
- `/jp-invoice/check`: `decision` is `verified`, `manual_review` or `not_found`. `company_match` and `address_match` compare the invoice's issuer with the registered record; `risk_flags` lists differences such as `supplier_name_differs_from_registered_legal_name`, `address_mismatch` or `invoice_cancelled`. A trade name differing from the legal name is common — present it as a difference to confirm, not as fraud.
- `/v1/invoices/issuer-match` and `/extract`: `decision` is `issuer_matched`, `supplier_mismatch`, `document_conflict`, `registration_problem`, `insufficient_evidence` or `source_unavailable`. Only `issuer_matched` confirms the invoice issuer against the expected identifiers, using registration status at the time of the check (`dates.date_check` is `not_performed`: no as-of-invoice-date judgement). `values` keeps the invoice, expected and registry values side by side; `reasons` lists stable codes such as `document_t_number_differs_from_expected` or `issuer_address_differs_from_registry`; `next_actions` says what data to add. Without `expected`, the result is `insufficient_evidence` with the registry evidence still returned. This is not a payment-approval or tax-deduction decision.
- `/v1/invoices/issuer-match/extract` also returns `invoice_eligibility` (`eligible`, `not_eligible`, `needs_review`) for input tax credit, with the seven qualified-invoice items and whether the issuer was registered on the transaction date. Report `summary_en`; it is not tax advice.
- For individuals (sole proprietors) the registry often does not publish an address, and the published name may differ from the trade name on the invoice; say so instead of treating missing or different fields as a mismatch.

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
  -H "X-JPVerify-Client: jp-invoice-number-check/1.0.9" \
  -H "Content-Type: application/json" \
  -d '{"registration_number": "T1013301046627", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/verify",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-invoice-number-check/1.0.9"},
    json={"registration_number": "T1013301046627", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

x402 (no account):

```bash
# No key: shows the HTTP 402 x402 price; pay with an x402 client and retry with PAYMENT-SIGNATURE.
curl -i -X POST https://api.jpverify.com/jp-invoice/verify \
  -H "X-JPVerify-Client: jp-invoice-number-check/1.0.9" \
  -H "Content-Type: application/json" \
  -d '{"registration_number": "T1013301046627", "response_language": "both"}'
```

Full SDK examples (Python `x402`, JavaScript `@x402/fetch`): https://api.jpverify.com/docs/x402

## Limits and privacy / 制限とプライバシー

- Results are a **public-registry pre-check** with the source and as-of date of the data. They are not KYB, AML or sanctions screening, and not legal, tax or accounting advice. A "not found" does not mean the entity does not exist or is risky.
- If `manual_review_required` is true or a status is ambiguous, show the evidence to the user and let them decide; do not decide on their behalf.
- Only send documents, images and personal data the user is entitled to process. Do not repeat full personal details (names, phone numbers, e-mail addresses on business cards) back unless the user asked for them.
- Docs: API key https://api.jpverify.com/docs/api-key · x402 https://api.jpverify.com/docs/x402 · terms https://api.jpverify.com/en/terms · privacy https://api.jpverify.com/en/privacy
