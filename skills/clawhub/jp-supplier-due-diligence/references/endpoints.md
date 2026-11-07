# jp-supplier-due-diligence — endpoints

Generated from the live JPVerify catalog. Prices are USD per successful call (the same with an API key or x402).

## English

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /v1/suppliers/resolve` | `jp_supplier_resolve` | $0.01 | You need one coverage-aware supplier check combining company, qualified-invoice, and address evidence; optionally includes projected gBizINFO activity evidence when the internal feature flag is enabled. | Independent evidence checks, source versions, and a resolved/ambiguous/not-found/insufficient-coverage status; optional gBizINFO is projected enrichment inside this response, not a standalone source or raw-response resale. Not a legal or KYB determination. |
| `POST /jp-invoice/check` | `jp_invoice_issuer_check` | $0.03 | You have extracted issuer fields and need T-number, company-name, and address comparison. | OCR issuer fields, NTA registry fields, comparison results, and resolved values; phone is not registry-compared. |
| `POST /jp-regulated-entity/verify` | — | $0.03 | You need to verify an entity against the covered Japanese FSA financial instruments, funds transfer, or crypto-asset exchange datasets. | Coverage-aware licensing decision, freshness, identity match, license evidence, and review warnings; not a legal unlicensed determination. |
| `GET /jp-company/filings` | — | $0.01 | You need EDINET filing metadata for a Japanese company by corporate number, EDINET code, or security code. | Filing metadata, correction/withdrawal relationships, freshness, and official evidence references; raw files remain internal. |
| `POST /v1/entities/resolve-cross-border` | — | $0.04 | You need a JP or GB entity identity pre-check from one country-routed API; the first release uses NTA/gBizINFO for JP and Companies House for GB. | Projected entity identity, evidence checks, source freshness, coverage, conflicts, and a conservative confidence band; raw upstream responses are never returned. |
| `POST /v1/invoices/counterparty-check` | `jp_counterparty_check` | $0.05 | You need separate EU VAT validity, returned-name entity matching, and Peppol participant discoverability evidence. | Projected VIES and Peppol evidence only; VIES is known-ID validation and member-state outages are insufficient coverage. |
| `GET /v1/entities/{cik}/filing-risk-snapshot` | — | $0.05 | You need objective recent SEC EDGAR filing and XBRL availability metadata for a known CIK. | Recent filing metadata and objective disclosure signals; never a credit rating or investment recommendation. |

## 日本語

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /v1/suppliers/resolve` | `jp_supplier_resolve` | $0.01 | 会社、適格請求書、住所の根拠を組み合わせ、必要に応じて内部機能フラグでgBizINFO活動根拠も付加した、対象範囲を明示した仕入先確認を行う場合。 | 個別の根拠チェック、ソース版、resolved/ambiguous/not-found/insufficient-coverage状態を返します。任意のgBizINFOはこのレスポンス内の加工済み補助根拠であり、単独ソースや原レスポンスの再販ではありません。法的判断やKYB判定ではありません。 |
| `POST /jp-invoice/check` | `jp_invoice_issuer_check` | $0.03 | 抽出済みの発行者情報について、T番号・会社名・住所を照合したい場合。 | OCR発行者情報、国税庁登記情報、比較結果、採用値を返します。電話番号は登記比較しません。 |
| `POST /jp-regulated-entity/verify` | — | $0.03 | 金融商品、資金移動、暗号資産交換の対象事業者データセットで日本法人を照合する場合。 | 対象範囲、鮮度、法人照合、免許根拠、確認警告を返します。無登録の法的判断ではありません。 |
| `GET /jp-company/filings` | — | $0.01 | 法人番号、EDINETコード、証券コードから日本企業のEDINET提出書類を検索する場合。 | 提出書類メタデータ、訂正・撤回関係、鮮度、公式根拠を返します。原本ファイルは返しません。 |
| `POST /v1/entities/resolve-cross-border` | — | $0.04 | 日本または英国の企業を国別に公式公開根拠で確認したい場合。第一期はJPが国税庁・gBizINFO、GBがCompanies Houseです。 | 加工済みの企業識別情報、根拠チェック、鮮度、対象範囲、矛盾、保守的な信頼度区分を返します。元データは返しません。 |
| `POST /v1/invoices/counterparty-check` | `jp_counterparty_check` | $0.05 | EU VAT有効性、返却名による法人一致、Peppol参加者到達性を分けて確認する場合。 | VIESとPeppolの加工済み根拠のみを返します。VIESは既知IDの検証であり、加盟国停止は対象範囲不足です。 |
| `GET /v1/entities/{cik}/filing-risk-snapshot` | — | $0.05 | 既知のCIKについてSEC EDGAR提出書類とXBRL開示状況の客観的メタデータを確認する場合。 | 最近の提出書類メタデータと客観的な開示シグナルを返します。信用格付けや投資助言ではありません。 |
