# jp-company-verify — endpoints

Generated from the live JPVerify catalog. Prices are USD per successful call (the same with an API key or x402).

## English

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-company/verify` | `jp_company_verify` | $0.005 | You need a Japanese company or corporate-number lookup. | Corporate number, registered legal name/address, active or closed status, and match evidence. |
| `POST /jp-company/report` | — | $0.05 | You need a Japan company registry pre-check with risk flags. | Registry identity, status, evidence, and risk flags; not full KYC/KYB. |
| `POST /jp-company/verify-batch` | — | $0.05 | You need up to 10 Japanese company or corporate-number lookups in one request. | One result per input with match status and registry evidence. |
| `GET /jp-company/filings` | — | $0.01 | You need EDINET filing metadata for a Japanese company by corporate number, EDINET code, or security code. | Filing metadata, correction/withdrawal relationships, freshness, and official evidence references; raw files remain internal. |
| `POST /jp-regulated-entity/verify` | — | $0.03 | You need to verify an entity against the covered Japanese FSA financial instruments, funds transfer, or crypto-asset exchange datasets. | Coverage-aware licensing decision, freshness, identity match, license evidence, and review warnings; not a legal unlicensed determination. |

## 日本語

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-company/verify` | `jp_company_verify` | $0.005 | 日本企業または法人番号を検索・照合したい場合。 | 法人番号、登記上の法人名・住所、活動状態、一致根拠を返します。 |
| `POST /jp-company/report` | — | $0.05 | 日本企業の登記情報に基づく事前確認とリスクフラグが必要な場合。 | 登記上の企業情報、状態、根拠、リスクフラグを返します。完全なKYC/KYBではありません。 |
| `POST /jp-company/verify-batch` | — | $0.05 | 最大10件の日本企業・法人番号を1回のリクエストで照合したい場合。 | 入力ごとの一致状態と登記根拠を返します。 |
| `GET /jp-company/filings` | — | $0.01 | 法人番号、EDINETコード、証券コードから日本企業のEDINET提出書類を検索する場合。 | 提出書類メタデータ、訂正・撤回関係、鮮度、公式根拠を返します。原本ファイルは返しません。 |
| `POST /jp-regulated-entity/verify` | — | $0.03 | 金融商品、資金移動、暗号資産交換の対象事業者データセットで日本法人を照合する場合。 | 対象範囲、鮮度、法人照合、免許根拠、確認警告を返します。無登録の法的判断ではありません。 |
