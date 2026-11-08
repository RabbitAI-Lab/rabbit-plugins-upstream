---
name: jp-address
description: >-
  Normalize, parse, validate and geocode Japanese addresses (住所の正規化・解析・検証) with JPVerify,
  and look up Japanese postal codes (郵便番号) — down to 丁目, block and building level, with the
  evidence behind each match. Use when a task involves cleaning or standardizing a Japanese address,
  checking that an address exists at a required precision, splitting it into components, finding
  coordinates, or finding the area for a postal code. Paid per call (API key credits or x402).
license: MIT
---

# Japanese addresses / 日本の住所

Version 1.0.9 · JPVerify · https://www.jpverify.com

## When to use / いつ使うか

- Clean up or standardize a Japanese address (full-width/half-width digits, 丁目・番・号 notation, kanji numerals).
- Split an address into prefecture, city, ward, town, 丁目, block, lot and building.
- Check that an address exists at a required precision before shipping, onboarding or storing it.
- Get coordinates, or the areas that belong to a postal code.

## Connect / 接続

JPVerify is a paid, per-call API. Pick the first option that applies; never guess credentials.

1. **API key (recommended).** If the environment has `JPVERIFY_API_KEY` (a `jpv_live_…` key the user created), send it on every call:
   - HTTP: header `Authorization: Bearer $JPVERIFY_API_KEY` (or `X-API-Key`).
   - MCP: if the JPVerify Claude Code plugin is installed, the `jpverify` MCP server is already configured and uses the key saved in the plugin's settings (`/plugin` → JPVerify → Configure), not `JPVERIFY_API_KEY`. Otherwise: `claude mcp add --transport http jpverify https://api.jpverify.com/mcp --header "Authorization: Bearer $JPVERIFY_API_KEY" --header "X-JPVerify-Client: jp-address/1.0.9"`
   Each successful call is deducted from the user's prepaid USD credits; failed or invalid calls are refunded automatically.
2. **x402 wallet.** If you have an x402 client with USDC on Base (`eip155:8453`) and the user approved a budget, call without a key: the API answers HTTP 402 with the exact price; sign and retry with `PAYMENT-SIGNATURE`. Pay only within the approved budget.
3. **Neither.** Do not pay and do not invent a key. The MCP server also works without a key for the free tool `jpverify_guide` (`claude mcp add --transport http jpverify https://api.jpverify.com/mcp`); use it to confirm which call fits, then tell the user they can create a free account with starter credit at https://www.jpverify.com/signup?ref=jp-address and set `JPVERIFY_API_KEY`.

Always send `X-JPVerify-Client: jp-address/1.0.9` on HTTP calls. Never print, log or share the API key.

## Workflow / 手順

1. **Pick the cheapest call that answers the question.**
   - Postal code → areas: `POST /jp-address/postal-lookup` (cheapest).
   - Standardized address + evidence in one call: `POST /jp-address/normalize` (MCP `jp_address_normalize`). This is the default.
   - Components only, no geocoding: `POST /jp-address/parse`.
   - Coordinates / candidates: `POST /jp-address/geocode`.
   - "Is this address good enough?": `POST /jp-address/validate` (MCP `jp_address_validate`) with `required_level` (5/6 = 大字・字, 7 = block/街区, 8 = building/house) and `strict` when every supplied piece of evidence must agree.
2. **Send the address as written** (Japanese). Do not translate it to English first. You can pass the output of `parse`/`postal-lookup`/`geocode` to `validate` as `parsed`, `postal_evidence` or `geocode_evidence` instead of calling again.
3. **Many addresses?** Up to 1,000 normalizations run as one x402 batch job (`/v1/batch-jobs`, operation `address_normalize`); confirm the total cost with the user first.

## Endpoints and prices / エンドポイントと料金

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-address/normalize` | `jp_address_normalize` | $0.005 | You need Japanese address normalization or standardization, whether or not the input contains a postal code. | Normalized prefecture/city/town/chome/block/lot/house components, an English address from Japan Post romanization, parser confidence, match hierarchy, geocoder evidence, and postal-code evidence when a postal code is supplied. It does not infer a missing postal code. |
| `POST /jp-address/validate` | `jp_address_validate` | $0.005 | You need one evidence-based Japanese address quality decision combining parsed address, postal evidence, and geocoder evidence. | Exact, partial, ambiguous, conflict, or unverified status with accepted hierarchy, confidence signals, validation scope, and reasons. |
| `POST /jp-address/parse` | — | $0.005 | You need Japanese address components such as prefecture, city, town, chome, block, lot, or house without postal lookup or geocoding. | Parser-only components, normalized value, chome/block/lot/house fields, English address and components from Japan Post romanization, normalization changes, unparsed fragments, parser status, and parser confidence. Postal and geocoder evidence are not returned. |
| `POST /jp-address/geocode` | — | $0.005 | You need Japanese forward-geocoding candidates, coordinates, address IDs, or hierarchy levels. The required hierarchy is inferred from the input. | Provider-neutral Jageocoder candidates with normalized address, coordinates, address ID, match level, granularity, confidence, reasons, unmatched tails, and dictionary status. Level 5/6 is oaza/aza, 7 is block, and 8 is building or house node when covered. City-level or town-prefix candidates remain partial; town-level results are not door-number or coordinate accuracy claims. |
| `POST /jp-address/postal-lookup` | — | $0.001 | You need a Japan Post postal-code lookup or reverse lookup from a postal code or administrative address. | Japan Post local-snapshot matches with postal code, prefecture, city, town, kana, Japan Post romanized prefecture/city/town, confidence, source, data version, and candidate count. |

### Request fields / リクエスト項目

| Endpoint | Required fields | Optional fields |
|---|---|---|
| `POST /jp-address/normalize` | `address` | `response_language` |
| `POST /jp-address/validate` | — | `address`, `parsed`, `postal_evidence`, `geocode_evidence`, `required_level`, `strict` |
| `POST /jp-address/parse` | `address` | `postal_code`, `response_language`, `parser_profile` |
| `POST /jp-address/geocode` | — | `address`, `components`, `postal_code`, `max_candidates`, `minimum_acceptable_level`, `provider` |
| `POST /jp-address/postal-lookup` | — | `postal_code`, `prefecture`, `county`, `city`, `ward`, `town`, `max_results` |

Where no field is required, send at least one identifier or input (for OCR: `text`, `file_url` or `image_base64`; for business cards: `front_image_url` or `front_image_base64`). `response_language` is `ja`, `en` or `both` (default `both`).

Japanese descriptions and request examples for every endpoint: [references/endpoints.md](references/endpoints.md), [references/examples.md](references/examples.md).

## Reading results / 結果の読み方

- `validate`: `address_validated` is true only when the address reaches `requested_level`. `match_status` is `exact`, `normalized_exact`, `partial`, `ambiguous`, `conflict`, `not_found` or `unverified`; `reasons` explains why. `partial` usually means the address is real but less precise than requested (e.g. no house number).
- `normalize` / `geocode`: `match_level`, `verified_level` and `precision_satisfied` tell how deep the match went; `candidate_count` above 1 means the address is ambiguous — show the candidates instead of choosing one.
- A missing postal code is **not** inferred by `normalize`; use `postal-lookup` if the user needs it.
- `normalized_en` uses Japan Post's official romanization (KEN_ALL_ROME), e.g. `1-9-1 Marunochi, Chiyoda-ku, Tokyo 100-0005`, with `normalized_en_source: japan_post_romaji` and a `normalized_en_confidence`. Japan Post's spelling is kept as published (no long-vowel marks), and building names are not translated. `/jp-address/parse` also returns `components_en`, and each `/jp-address/postal-lookup` match returns `prefecture_en`, `city_en` and `town_en`. Nothing is machine-translated.
- `normalized_en_common` gives the spelling people usually write where Japan Post's differs (丸の内: Marunouchi rather than Japan Post's Marunochi); use it for display and keep `normalized_en` for matching Japan Post data.

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

## Example / 呼び出し例 (`POST /jp-address/normalize`)

API key:

```bash
curl -X POST https://api.jpverify.com/jp-address/normalize \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-address/1.0.9" \
  -H "Content-Type: application/json" \
  -d '{"address": "東京都新宿区西新宿2丁目8番1号", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-address/normalize",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-address/1.0.9"},
    json={"address": "東京都新宿区西新宿2丁目8番1号", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

x402 (no account):

```bash
# No key: shows the HTTP 402 x402 price; pay with an x402 client and retry with PAYMENT-SIGNATURE.
curl -i -X POST https://api.jpverify.com/jp-address/normalize \
  -H "X-JPVerify-Client: jp-address/1.0.9" \
  -H "Content-Type: application/json" \
  -d '{"address": "東京都新宿区西新宿2丁目8番1号", "response_language": "both"}'
```

Full SDK examples (Python `x402`, JavaScript `@x402/fetch`): https://api.jpverify.com/docs/x402

## Limits and privacy / 制限とプライバシー

- Results are a **public-registry pre-check** with the source and as-of date of the data. They are not KYB, AML or sanctions screening, and not legal, tax or accounting advice. A "not found" does not mean the entity does not exist or is risky.
- If `manual_review_required` is true or a status is ambiguous, show the evidence to the user and let them decide; do not decide on their behalf.
- Only send documents, images and personal data the user is entitled to process. Do not repeat full personal details (names, phone numbers, e-mail addresses on business cards) back unless the user asked for them.
- Docs: API key https://api.jpverify.com/docs/api-key · x402 https://api.jpverify.com/docs/x402 · terms https://api.jpverify.com/en/terms · privacy https://api.jpverify.com/en/privacy
