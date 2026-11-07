# jpverify — endpoints

Generated from the live JPVerify catalog. Prices are USD per successful call (the same with an API key or x402).

## English

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
| `POST /jp-invoice/extract` | `jp_invoice_extract` | $0.01 | You need Japanese billing-invoice OCR and deterministic quality checks without registry lookup. | OCR-derived invoice fields plus format, arithmetic, tax, completeness, and review status. |
| `POST /jp-invoice/extract-and-verify` | `jp_invoice_extract_and_verify` | $0.05 | You need invoice OCR and issuer name/address comparison or completion using NTA public data. | OCR values, registry values, resolved issuer values, validation, and an explicit review signal. |
| `POST /jp-receipt/extract` | `jp_receipt_extract` | $0.03 | You need Japanese receipt or 領収書 OCR with local tax, amount, T-number, and format checks. | Structured receipt fields, deterministic validation, field status, and review signals. |
| `POST /jp-business-card/extract` | `jp_business_card_extract` (enrich=false) | $0.03 | You need only the person, role, department, company, phone, email, or address printed on a Japanese business card. | Card-printed contact fields only; no corporate-number or NTA issuer verification. |
| `POST /jp-business-card/extract-and-enrich` | `jp_business_card_extract` (enrich=true) | $0.10 | You need business-card OCR plus Japanese corporate-number and qualified-invoice enrichment. | Separate card OCR values and registry-resolved company values; registry pre-check, not full KYB. |
| `POST /jp-address/normalize` | `jp_address_normalize` | $0.005 | You need Japanese address normalization or standardization, whether or not the input contains a postal code. | Normalized prefecture/city/town/chome/block/lot/house components, parser confidence, match hierarchy, geocoder evidence, and postal-code evidence when a postal code is supplied. It does not infer a missing postal code. |
| `POST /jp-address/parse` | — | $0.005 | You need Japanese address components such as prefecture, city, town, chome, block, lot, or house without postal lookup or geocoding. | Parser-only components, normalized value, chome/block/lot/house fields, normalization changes, unparsed fragments, parser status, and parser confidence. Postal and geocoder evidence are not returned. |
| `POST /jp-address/postal-lookup` | — | $0.001 | You need a Japan Post postal-code lookup or reverse lookup from a postal code or administrative address. | Japan Post local-snapshot matches with postal code, prefecture, city, town, kana, confidence, source, data version, and candidate count. |
| `POST /jp-address/geocode` | — | $0.005 | You need Japanese forward-geocoding candidates, coordinates, address IDs, or hierarchy levels. The required hierarchy is inferred from the input. | Provider-neutral Jageocoder candidates with normalized address, coordinates, address ID, match level, granularity, confidence, reasons, unmatched tails, and dictionary status. Level 5/6 is oaza/aza, 7 is block, and 8 is building or house node when covered. City-level or town-prefix candidates remain partial; town-level results are not door-number or coordinate accuracy claims. |
| `POST /jp-address/validate` | `jp_address_validate` | $0.005 | You need one evidence-based Japanese address quality decision combining parsed address, postal evidence, and geocoder evidence. | Exact, partial, ambiguous, conflict, or unverified status with accepted hierarchy, confidence signals, validation scope, and reasons. |
| `POST /v1/invoices/validate-jp-pint` | — | $0.02 | You need offline validation of a JP PINT 1.1.3 UBL Invoice before accounting or payment workflow acceptance. | Official document_valid from pinned OASIS UBL 2.1 XSD and OpenPeppol JP PINT 1.1.3 Schematron, plus separate decision/trusted fields and optional NTA registry evidence. |
| `POST /v1/invoices/counterparty-check` | `jp_counterparty_check` | $0.05 | You need separate EU VAT validity, returned-name entity matching, and Peppol participant discoverability evidence. | Projected VIES and Peppol evidence only; VIES is known-ID validation and member-state outages are insufficient coverage. |
| `POST /v1/entities/resolve-cross-border` | — | $0.04 | You need a JP or GB entity identity pre-check from one country-routed API; the first release uses NTA/gBizINFO for JP and Companies House for GB. | Projected entity identity, evidence checks, source freshness, coverage, conflicts, and a conservative confidence band; raw upstream responses are never returned. |
| `GET /v1/entities/{cik}/filing-risk-snapshot` | — | $0.05 | You need objective recent SEC EDGAR filing and XBRL availability metadata for a known CIK. | Recent filing metadata and objective disclosure signals; never a credit rating or investment recommendation. |
| `POST /v1/batch-jobs` | — | per item (x402 only) | You need up to 1,000 structured company, invoice, supplier, or Japanese address operations as one durable paid job with progress and downloadable per-item results. | An owner-scoped job ID, exact operation-based price, payment and execution state, progress counts, and stable per-item results with retry metadata; results are released only after settlement. |

## 日本語

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /jp-invoice/verify` | `jp_invoice_registration_verify` | $0.01 | 日本のT+13桁インボイス登録番号が既にある場合。 | 国税庁の登録状態、法人番号、登録名、関連日付を返します。 |
| `POST /jp-invoice/check` | `jp_invoice_issuer_check` | $0.03 | 抽出済みの発行者情報について、T番号・会社名・住所を照合したい場合。 | OCR発行者情報、国税庁登記情報、比較結果、採用値を返します。電話番号は登記比較しません。 |
| `POST /jp-invoice/verify-batch` | — | $0.05 | 最大10件の日本のT番号を1回のリクエストで検証したい場合。 | T番号ごとの国税庁登録結果を返します。 |
| `POST /jp-company/verify` | `jp_company_verify` | $0.005 | 日本企業または法人番号を検索・照合したい場合。 | 法人番号、登記上の法人名・住所、活動状態、一致根拠を返します。 |
| `POST /jp-company/report` | — | $0.05 | 日本企業の登記情報に基づく事前確認とリスクフラグが必要な場合。 | 登記上の企業情報、状態、根拠、リスクフラグを返します。完全なKYC/KYBではありません。 |
| `POST /jp-company/verify-batch` | — | $0.05 | 最大10件の日本企業・法人番号を1回のリクエストで照合したい場合。 | 入力ごとの一致状態と登記根拠を返します。 |
| `POST /v1/suppliers/resolve` | `jp_supplier_resolve` | $0.01 | 会社、適格請求書、住所の根拠を組み合わせ、必要に応じて内部機能フラグでgBizINFO活動根拠も付加した、対象範囲を明示した仕入先確認を行う場合。 | 個別の根拠チェック、ソース版、resolved/ambiguous/not-found/insufficient-coverage状態を返します。任意のgBizINFOはこのレスポンス内の加工済み補助根拠であり、単独ソースや原レスポンスの再販ではありません。法的判断やKYB判定ではありません。 |
| `POST /jp-regulated-entity/verify` | — | $0.03 | 金融商品、資金移動、暗号資産交換の対象事業者データセットで日本法人を照合する場合。 | 対象範囲、鮮度、法人照合、免許根拠、確認警告を返します。無登録の法的判断ではありません。 |
| `GET /jp-company/filings` | — | $0.01 | 法人番号、EDINETコード、証券コードから日本企業のEDINET提出書類を検索する場合。 | 提出書類メタデータ、訂正・撤回関係、鮮度、公式根拠を返します。原本ファイルは返しません。 |
| `POST /jp-invoice/extract` | `jp_invoice_extract` | $0.01 | 日本語の請求書をOCRし、法人照合なしで日付・金額・税額・T番号を検証したい場合。 | OCR請求書項目に加え、形式・金額計算・税額・必須項目・確認状態を返します。 |
| `POST /jp-invoice/extract-and-verify` | `jp_invoice_extract_and_verify` | $0.05 | 請求書OCRに加えて、国税庁公開データで発行者名・住所・T番号を照合・補完したい場合。 | OCR値、登記値、採用した発行者値、検証結果、明示的な確認シグナルを返します。 |
| `POST /jp-receipt/extract` | `jp_receipt_extract` | $0.03 | 日本語の領収書・レシートをOCRし、金額・税額・T番号・形式を検証したい場合。 | 構造化された領収書項目、決定論的検証、項目状態、確認シグナルを返します。 |
| `POST /jp-business-card/extract` | `jp_business_card_extract` (enrich=false) | $0.03 | 日本語の名刺に印刷された氏名、役職、部署、会社名、電話、メール、住所だけが必要な場合。 | 名刺に印刷された連絡先のみ。法人番号や国税庁発行者照合は含みません。 |
| `POST /jp-business-card/extract-and-enrich` | `jp_business_card_extract` (enrich=true) | $0.10 | 名刺OCRに加えて、日本の法人番号・適格請求書登録情報で企業を照合したい場合。 | 名刺OCR値と登記照合済み企業値を分離して返します。完全なKYBではありません。 |
| `POST /jp-address/normalize` | `jp_address_normalize` | $0.005 | 入力に郵便番号があってもなくても、日本住所を正規化・標準化したい場合。 | 都道府県・市区町村・町名・丁目・番地・号などの正規化項目、解析信頼度、照合階層、地理コード根拠を返します。郵便番号を入力した場合のみ郵便番号根拠を返し、未入力の郵便番号は推定しません。 |
| `POST /jp-address/parse` | — | $0.005 | 郵便番号照合やジオコーディングなしで、日本住所の構成要素だけが必要な場合。 | 住所構成要素、正規化値、丁目・番地・号、正規化変更、未解析部分、解析状態、解析信頼度を返します。郵便・地理コード根拠は返しません。 |
| `POST /jp-address/postal-lookup` | — | $0.001 | 郵便番号または行政区・町名から日本の郵便番号を逆引きしたい場合。 | Japan Postローカルデータの郵便番号、都道府県、市区町村、町名、かな、信頼度、出典、データ版、候補数を返します。 |
| `POST /jp-address/geocode` | — | $0.005 | 日本住所を座標に変換し、候補、住所ID、階層レベルが必要な場合。 | 正規化住所、座標、住所ID、照合レベル、粒度、信頼度、理由、未照合末尾、辞書状態を含むJageocoder候補を返します。5/6=大字・字、7=街区、8=住居番号です。市町村候補や町域の部分一致はpartialのままで、町域一致を門牌・座標精度とは表示しません。 |
| `POST /jp-address/validate` | `jp_address_validate` | $0.005 | 解析住所、郵便番号根拠、ジオコーダー根拠を統一ルールで判定したい場合。 | 完全一致、部分一致、候補不一意、矛盾、未検証の状態に加え、採用階層、信頼度、判定範囲、理由を返します。 |
| `POST /v1/invoices/validate-jp-pint` | — | $0.02 | 会計処理や支払ワークフローに受け入れる前に、JP PINT 1.1.3 UBL請求書をオフライン検証したい場合。 | 固定したOASIS UBL 2.1 XSDとOpenPeppol JP PINT 1.1.3 Schematronによるdocument_valid、分離されたdecision/trusted、任意の国税庁登記根拠を返します。 |
| `POST /v1/invoices/counterparty-check` | `jp_counterparty_check` | $0.05 | EU VAT有効性、返却名による法人一致、Peppol参加者到達性を分けて確認する場合。 | VIESとPeppolの加工済み根拠のみを返します。VIESは既知IDの検証であり、加盟国停止は対象範囲不足です。 |
| `POST /v1/entities/resolve-cross-border` | — | $0.04 | 日本または英国の企業を国別に公式公開根拠で確認したい場合。第一期はJPが国税庁・gBizINFO、GBがCompanies Houseです。 | 加工済みの企業識別情報、根拠チェック、鮮度、対象範囲、矛盾、保守的な信頼度区分を返します。元データは返しません。 |
| `GET /v1/entities/{cik}/filing-risk-snapshot` | — | $0.05 | 既知のCIKについてSEC EDGAR提出書類とXBRL開示状況の客観的メタデータを確認する場合。 | 最近の提出書類メタデータと客観的な開示シグナルを返します。信用格付けや投資助言ではありません。 |
| `POST /v1/batch-jobs` | — | per item (x402 only) | 会社、請求書、仕入先、日本住所の構造化処理を最大1,000件、進捗確認と項目別ダウンロード結果付きの永続有料ジョブとして実行したい場合。 | 所有者限定のジョブID、操作別の正確な料金、支払・実行状態、進捗件数、再試行情報付きの安定した項目別結果を返します。結果は決済完了後のみ取得できます。 |
