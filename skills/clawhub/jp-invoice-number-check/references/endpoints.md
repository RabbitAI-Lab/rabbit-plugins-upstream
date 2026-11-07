# jp-invoice-number-check — endpoints

Generated from the live JPVerify catalog. Prices are USD per successful call (the same with an API key or x402).

## English

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-invoice/verify` | `jp_invoice_registration_verify` | $0.01 | You already have a Japanese T+13-digit qualified-invoice registration number. | NTA registration status, corporate number, registered name, and relevant dates. |
| `POST /jp-invoice/check` | `jp_invoice_issuer_check` | $0.03 | You have extracted issuer fields and need T-number, company-name, and address comparison. | OCR issuer fields, NTA registry fields, comparison results, and resolved values; phone is not registry-compared. |
| `POST /jp-invoice/verify-batch` | — | $0.05 | You need up to 10 Japanese T-number checks in one request. | One NTA registration result per T-number. |

## 日本語

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-invoice/verify` | `jp_invoice_registration_verify` | $0.01 | 日本のT+13桁インボイス登録番号が既にある場合。 | 国税庁の登録状態、法人番号、登録名、関連日付を返します。 |
| `POST /jp-invoice/check` | `jp_invoice_issuer_check` | $0.03 | 抽出済みの発行者情報について、T番号・会社名・住所を照合したい場合。 | OCR発行者情報、国税庁登記情報、比較結果、採用値を返します。電話番号は登記比較しません。 |
| `POST /jp-invoice/verify-batch` | — | $0.05 | 最大10件の日本のT番号を1回のリクエストで検証したい場合。 | T番号ごとの国税庁登録結果を返します。 |
