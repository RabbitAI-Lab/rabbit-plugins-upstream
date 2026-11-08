# jp-business-document-ocr — endpoints

Generated from the live JPVerify catalog. Prices are USD per successful call (the same with an API key or x402).

## English

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-invoice/extract` | `jp_invoice_extract` | $0.03 | You need Japanese billing-invoice OCR and deterministic quality checks without registry lookup. | OCR-derived invoice fields plus format, arithmetic, tax, completeness, and review status. |
| `POST /jp-invoice/extract-and-verify` | `jp_invoice_extract_and_verify` | $0.10 | You need invoice OCR and issuer name/address comparison or completion using NTA public data. | OCR values, registry values, resolved issuer values, validation, an explicit review signal, and invoice_eligibility (eligible / not_eligible / needs_review for input tax credit, with the seven qualified-invoice items and registration on the transaction date). |
| `POST /jp-receipt/extract` | `jp_receipt_extract` | $0.03 | You need Japanese receipt or 領収書 OCR with local tax, amount, T-number, and format checks. | Structured receipt fields, deterministic validation, field status, and review signals. |
| `POST /jp-business-card/extract` | `jp_business_card_extract` (enrich=false) | $0.03 | You need only the person, role, department, company, phone, email, or address printed on a Japanese business card. | Card-printed contact fields only; no corporate-number or NTA issuer verification. |
| `POST /jp-business-card/extract-and-enrich` | `jp_business_card_extract` (enrich=true) | $0.10 | You need business-card OCR plus Japanese corporate-number and qualified-invoice enrichment. | Separate card OCR values and registry-resolved company values; registry pre-check, not full KYB. |

## 日本語

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-invoice/extract` | `jp_invoice_extract` | $0.03 | 日本語の請求書をOCRし、法人照合なしで日付・金額・税額・T番号を検証したい場合。 | OCR請求書項目に加え、形式・金額計算・税額・必須項目・確認状態を返します。 |
| `POST /jp-invoice/extract-and-verify` | `jp_invoice_extract_and_verify` | $0.10 | 請求書OCRに加えて、国税庁公開データで発行者名・住所・T番号を照合・補完したい場合。 | OCR値、登記値、採用した発行者値、検証結果、確認シグナルに加え、仕入税額控除の可否（記載事項7項目と取引日時点の登録）を返します。 |
| `POST /jp-receipt/extract` | `jp_receipt_extract` | $0.03 | 日本語の領収書・レシートをOCRし、金額・税額・T番号・形式を検証したい場合。 | 構造化された領収書項目、決定論的検証、項目状態、確認シグナルを返します。 |
| `POST /jp-business-card/extract` | `jp_business_card_extract` (enrich=false) | $0.03 | 日本語の名刺に印刷された氏名、役職、部署、会社名、電話、メール、住所だけが必要な場合。 | 名刺に印刷された連絡先のみ。法人番号や国税庁発行者照合は含みません。 |
| `POST /jp-business-card/extract-and-enrich` | `jp_business_card_extract` (enrich=true) | $0.10 | 名刺OCRに加えて、日本の法人番号・適格請求書登録情報で企業を照合したい場合。 | 名刺OCR値と登記照合済み企業値を分離して返します。完全なKYBではありません。 |
