# jp-company-verify — endpoints

Generated from the live JPVerify catalog. Prices are USD per successful call (the same with an API key or x402).

## English

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /v1/jp/entities/resolve` | `jp_entity_resolve` | $0.25 | You hold an English, brand or romanized Japanese company name, an English address or postal code, a website or e-mail domain, a T-number, corporate number, LEI or securities code and need the Japanese legal entity, in English. | Decision (matched / likely_match / candidates), legally binding Japanese name, kana, English name with source, contract party name, status and qualified-invoice registration. |
| `POST /jp-company/verify` | `jp_company_verify` | $0.01 | You need a Japanese company or corporate-number lookup. | Corporate number, registered Japanese legal name (legal_name_ja) and address, English name (NTA official, EDINET, or romanized reading) and English address (official or Japan Post romanization) with their sources, active or closed status, and match evidence. |
| `POST /jp-company/report` | — | $0.10 | You need a Japan company registry pre-check with risk flags. | Registry identity, status, evidence and risk flags, plus a profile (capital, employees, founding date, website, representative), listing and latest EDINET filing, FSA licences and former names, each with its source; not full KYC/KYB. |
| `POST /jp-company/verify-batch` | — | $0.08 | You need up to 10 Japanese company or corporate-number lookups in one request. | One result per input with match status and registry evidence. |
| `GET /jp-company/filings` | — | $0.01 | You need EDINET filing metadata for a Japanese company by corporate number, EDINET code, or security code. | Filing metadata, correction/withdrawal relationships, freshness, and official evidence references; raw files remain internal. |
| `POST /jp-regulated-entity/verify` | — | $0.03 | You need to verify an entity against the covered Japanese FSA financial instruments, funds transfer, or crypto-asset exchange datasets. | Coverage-aware licensing decision, freshness, identity match, license evidence, and review warnings; not a legal unlicensed determination. |

## 日本語

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /v1/jp/entities/resolve` | `jp_entity_resolve` | $0.25 | 英語名・ブランド名・ローマ字・英語住所・郵便番号・Webサイト／メールのドメイン・T番号・法人番号・LEI・証券コードから日本の法人を特定したい場合。 | 判定、正式な日本語商号、読み、出典付き英語名、契約当事者名、状態、適格請求書登録を返します。 |
| `POST /jp-company/verify` | `jp_company_verify` | $0.01 | 日本企業または法人番号を検索・照合したい場合。 | 法人番号、登記上の法人名（legal_name_ja）・住所、英語名（国税庁公式・EDINET・読みのローマ字）と英語住所（公式または日本郵便ローマ字）とその出典、活動状態、一致根拠を返します。 |
| `POST /jp-company/report` | — | $0.10 | 日本企業の登記情報に基づく事前確認とリスクフラグが必要な場合。 | 登記上の企業情報、状態、根拠、リスクフラグに加え、企業概要（資本金・従業員数・設立日・Webサイト・代表者）、上場情報と最新のEDINET提出書類、金融庁登録、旧商号を出典付きで返します。完全なKYC/KYBではありません。 |
| `POST /jp-company/verify-batch` | — | $0.08 | 最大10件の日本企業・法人番号を1回のリクエストで照合したい場合。 | 入力ごとの一致状態と登記根拠を返します。 |
| `GET /jp-company/filings` | — | $0.01 | 法人番号、EDINETコード、証券コードから日本企業のEDINET提出書類を検索する場合。 | 提出書類メタデータ、訂正・撤回関係、鮮度、公式根拠を返します。原本ファイルは返しません。 |
| `POST /jp-regulated-entity/verify` | — | $0.03 | 金融商品、資金移動、暗号資産交換の対象事業者データセットで日本法人を照合する場合。 | 対象範囲、鮮度、法人照合、免許根拠、確認警告を返します。無登録の法的判断ではありません。 |
