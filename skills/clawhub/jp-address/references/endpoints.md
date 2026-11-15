# jp-address — endpoints

Generated from the live JPVerify catalog. Prices are USD per successful call (the same with an API key or x402).

## English

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /v1/jp/addresses/normalize` | `jp_address_normalize` | $0.005 | You need Japanese address normalization or standardization, whether or not the input contains a postal code. | Normalized prefecture/city/town/chome/block/lot/house components, an English address from Japan Post romanization, parser confidence, match hierarchy, geocoder evidence, and postal-code evidence when a postal code is supplied. It does not infer a missing postal code. |
| `POST /v1/jp/addresses/validate` | `jp_address_validate` | $0.005 | You need one evidence-based Japanese address quality decision combining parsed address, postal evidence, and geocoder evidence. | Exact, partial, ambiguous, conflict, or unverified status with accepted hierarchy, confidence signals, validation scope, and reasons. |
| `POST /v1/jp/addresses/parse` | — | $0.005 | You need Japanese address components such as prefecture, city, town, chome, block, lot, or house without postal lookup or geocoding. | Parser-only components, normalized value, chome/block/lot/house fields, English address and components from Japan Post romanization, normalization changes, unparsed fragments, parser status, and parser confidence. Postal and geocoder evidence are not returned. |
| `POST /v1/jp/addresses/geocode` | — | $0.005 | You need Japanese forward-geocoding candidates, coordinates, address IDs, or hierarchy levels. The required hierarchy is inferred from the input. | Provider-neutral Jageocoder candidates with normalized address, coordinates, address ID, match level, granularity, confidence, reasons, unmatched tails, and dictionary status. Level 5/6 is oaza/aza, 7 is block, and 8 is building or house node when covered. City-level or town-prefix candidates remain partial; town-level results are not door-number or coordinate accuracy claims. Parcel addresses (番地) match at level 7; a sub-number (枝番) the dictionary lacks stays partial. |
| `POST /v1/jp/postal-codes/lookup` | — | $0.001 | You need a Japan Post postal-code lookup or reverse lookup from a postal code or administrative address. | Japan Post local-snapshot matches with postal code, prefecture, city, town, kana, Japan Post romanized prefecture/city/town, confidence, source, data version, and candidate count. Business-specific codes of single offices (e.g. 100-8310) return postal_code_type business_specific with the office name and street. |

## 日本語

| Endpoint | MCP tool | Price (USD) | Use when | Returns |
|---|---|---|---|---|
| `POST /v1/jp/addresses/normalize` | `jp_address_normalize` | $0.005 | 入力に郵便番号があってもなくても、日本住所を正規化・標準化したい場合。 | 都道府県・市区町村・町名・丁目・番地・号などの正規化項目、解析信頼度、照合階層、地理コード根拠を返します。郵便番号を入力した場合のみ郵便番号根拠を返し、未入力の郵便番号は推定しません。 |
| `POST /v1/jp/addresses/validate` | `jp_address_validate` | $0.005 | 解析住所、郵便番号根拠、ジオコーダー根拠を統一ルールで判定したい場合。 | 完全一致、部分一致、候補不一意、矛盾、未検証の状態に加え、採用階層、信頼度、判定範囲、理由を返します。 |
| `POST /v1/jp/addresses/parse` | — | $0.005 | 郵便番号照合やジオコーディングなしで、日本住所の構成要素だけが必要な場合。 | 住所構成要素、正規化値、丁目・番地・号、正規化変更、未解析部分、解析状態、解析信頼度を返します。郵便・地理コード根拠は返しません。 |
| `POST /v1/jp/addresses/geocode` | — | $0.005 | 日本住所を座標に変換し、候補、住所ID、階層レベルが必要な場合。 | 正規化住所、座標、住所ID、照合レベル、粒度、信頼度、理由、未照合末尾、辞書状態を含むJageocoder候補を返します。5/6=大字・字、7=街区、8=住居番号です。市町村候補や町域の部分一致はpartialのままで、町域一致を門牌・座標精度とは表示しません。地番（番地）はレベル7で照合し、辞書にない枝番はpartialのままです。 |
| `POST /v1/jp/postal-codes/lookup` | — | $0.001 | 郵便番号または行政区・町名から日本の郵便番号を逆引きしたい場合。 | Japan Postローカルデータの郵便番号、都道府県、市区町村、町名、かな、信頼度、出典、データ版、候補数を返します。事業所の個別郵便番号（例: 100-8310）はpostal_code_type=business_specificと事業所名・番地を返します。 |
