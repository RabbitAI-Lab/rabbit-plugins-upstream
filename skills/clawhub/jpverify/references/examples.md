# jpverify — request examples

Set `JPVERIFY_API_KEY` (create one at https://www.jpverify.com/signup?ref=jpverify). Without a key the API answers HTTP 402 with the x402 price; see https://api.jpverify.com/docs/x402 for x402 SDK code.

## `POST /jp-invoice/verify` — $0.01

```bash
curl -X POST https://api.jpverify.com/jp-invoice/verify \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"registration_number": "T1013301046627", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/verify",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"registration_number": "T1013301046627", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-invoice/check` — $0.03

```bash
curl -X POST https://api.jpverify.com/jp-invoice/check \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"registration_number": "T1013301046627", "supplier_name": "株式会社ABC", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/check",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"registration_number": "T1013301046627", "supplier_name": "株式会社ABC", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-invoice/verify-batch` — $0.05

```bash
curl -X POST https://api.jpverify.com/jp-invoice/verify-batch \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"registration_numbers": ["T1013301046627"], "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/verify-batch",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"registration_numbers": ["T1013301046627"], "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-company/verify` — $0.005

```bash
curl -X POST https://api.jpverify.com/jp-company/verify \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"name": "トヨタ自動車株式会社", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-company/verify",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"name": "トヨタ自動車株式会社", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-company/report` — $0.05

```bash
curl -X POST https://api.jpverify.com/jp-company/report \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"name": "株式会社ABC", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-company/report",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"name": "株式会社ABC", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-company/verify-batch` — $0.05

```bash
curl -X POST https://api.jpverify.com/jp-company/verify-batch \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"items": [{"corporate_number": "1180301018771"}], "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-company/verify-batch",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"items": [{"corporate_number": "1180301018771"}], "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /v1/suppliers/resolve` — $0.01

```bash
curl -X POST https://api.jpverify.com/v1/suppliers/resolve \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"name": "株式会社ABC", "registration_number": "T1013301046627", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/v1/suppliers/resolve",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"name": "株式会社ABC", "registration_number": "T1013301046627", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-regulated-entity/verify` — $0.03

```bash
curl -X POST https://api.jpverify.com/jp-regulated-entity/verify \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"corporate_number": "1234567890123", "categories": ["funds_transfer_business"], "response_language": "en"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-regulated-entity/verify",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"corporate_number": "1234567890123", "categories": ["funds_transfer_business"], "response_language": "en"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `GET /jp-company/filings` — $0.01

```bash
curl -G https://api.jpverify.com/jp-company/filings \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  --data-urlencode 'edinet_code=E00000' \
  --data-urlencode 'limit=20' \
  --data-urlencode 'response_language=en'
```

```python
import os, requests

response = requests.get(
    "https://api.jpverify.com/jp-company/filings",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    params={"edinet_code": "E00000", "limit": 20, "response_language": "en"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-invoice/extract` — $0.01

```bash
curl -X POST https://api.jpverify.com/jp-invoice/extract \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"text": "請求書 株式会社ABC 登録番号 T1013301046627 請求日 2026年8月15日 支払期日 2026年9月30日 合計110000円 消費税10000円", "fields": ["supplier_name", "registration_number", "invoice_date", "due_date", "total", "tax_amount", "payment_terms"], "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/extract",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"text": "請求書 株式会社ABC 登録番号 T1013301046627 請求日 2026年8月15日 支払期日 2026年9月30日 合計110000円 消費税10000円", "fields": ["supplier_name", "registration_number", "invoice_date", "due_date", "total", "tax_amount", "payment_terms"], "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-invoice/extract-and-verify` — $0.05

```bash
curl -X POST https://api.jpverify.com/jp-invoice/extract-and-verify \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"text": "登録番号 T1013301046627 合計110000円 消費税10000円", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/extract-and-verify",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"text": "登録番号 T1013301046627 合計110000円 消費税10000円", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-receipt/extract` — $0.03

```bash
curl -X POST https://api.jpverify.com/jp-receipt/extract \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"text": "八福餃子房 2025年4月12日 21:18 登録番号 T1013301046627 合計12425円 内消費税1130円", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-receipt/extract",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"text": "八福餃子房 2025年4月12日 21:18 登録番号 T1013301046627 合計12425円 内消費税1130円", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-business-card/extract` — $0.03

```bash
curl -X POST https://api.jpverify.com/jp-business-card/extract \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"front_image_url": "https://www.jpverify.com/samples/business-card-front.png", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-business-card/extract",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"front_image_url": "https://www.jpverify.com/samples/business-card-front.png", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-business-card/extract-and-enrich` — $0.10

```bash
curl -X POST https://api.jpverify.com/jp-business-card/extract-and-enrich \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"front_image_url": "https://www.jpverify.com/samples/business-card-front.png", "back_image_url": "https://www.jpverify.com/samples/business-card-back.png", "output_format": "json", "include_raw_text": false, "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-business-card/extract-and-enrich",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"front_image_url": "https://www.jpverify.com/samples/business-card-front.png", "back_image_url": "https://www.jpverify.com/samples/business-card-back.png", "output_format": "json", "include_raw_text": False, "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-address/normalize` — $0.005

```bash
curl -X POST https://api.jpverify.com/jp-address/normalize \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"address": "東京都新宿区西新宿2丁目8番1号", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-address/normalize",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"address": "東京都新宿区西新宿2丁目8番1号", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-address/parse` — $0.005

```bash
curl -X POST https://api.jpverify.com/jp-address/parse \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"address": "東京都千代田区千代田1丁目1番1号", "response_language": "ja"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-address/parse",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"address": "東京都千代田区千代田1丁目1番1号", "response_language": "ja"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-address/postal-lookup` — $0.001

```bash
curl -X POST https://api.jpverify.com/jp-address/postal-lookup \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"postal_code": "100-0001", "max_results": 10}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-address/postal-lookup",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"postal_code": "100-0001", "max_results": 10},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-address/geocode` — $0.005

```bash
curl -X POST https://api.jpverify.com/jp-address/geocode \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"address": "東京都千代田区千代田1丁目1番1号", "max_candidates": 3}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-address/geocode",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"address": "東京都千代田区千代田1丁目1番1号", "max_candidates": 3},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-address/validate` — $0.005

```bash
curl -X POST https://api.jpverify.com/jp-address/validate \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"address": "東京都千代田区千代田1丁目1番1号", "required_level": 8, "strict": false}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-address/validate",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"address": "東京都千代田区千代田1丁目1番1号", "required_level": 8, "strict": False},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /v1/invoices/validate-jp-pint` — $0.02

```bash
# invoice.xml: your JP PINT 1.1.3 UBL Invoice
jq -n --rawfile xml invoice.xml '{xml: $xml, registry_enhance: true}' |
  curl -X POST https://api.jpverify.com/v1/invoices/validate-jp-pint \
    -H "Authorization: Bearer $JPVERIFY_API_KEY" \
    -H "X-JPVerify-Client: jpverify/1.0.1" \
    -H "Content-Type: application/json" \
    --data-binary @-
```

```python
import os, pathlib, requests

response = requests.post(
    "https://api.jpverify.com/v1/invoices/validate-jp-pint",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"xml": pathlib.Path("invoice.xml").read_text(encoding="utf-8"), "registry_enhance": True},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /v1/invoices/counterparty-check` — $0.05

```bash
curl -X POST https://api.jpverify.com/v1/invoices/counterparty-check \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"vat_id": "DE123456789", "participant_id": "iso6523-actorid-upis::0088:123456789", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/v1/invoices/counterparty-check",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"vat_id": "DE123456789", "participant_id": "iso6523-actorid-upis::0088:123456789", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /v1/entities/resolve-cross-border` — $0.04

```bash
curl -X POST https://api.jpverify.com/v1/entities/resolve-cross-border \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"country_code": "GB", "identifiers": {"company_number": "00000006"}, "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/v1/entities/resolve-cross-border",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    json={"country_code": "GB", "identifiers": {"company_number": "00000006"}, "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `GET /v1/entities/{cik}/filing-risk-snapshot` — $0.05

```bash
curl -G https://api.jpverify.com/v1/entities/0000320193/filing-risk-snapshot \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jpverify/1.0.1"
```

```python
import os, requests

response = requests.get(
    "https://api.jpverify.com/v1/entities/0000320193/filing-risk-snapshot",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jpverify/1.0.1"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /v1/batch-jobs` — per item (x402 only)

x402 only (not available with an API key). Choose your own capability token (32+ characters) and a unique `Idempotency-Key` per job.

```bash
# No key: shows the HTTP 402 x402 price; pay with an x402 client and retry with PAYMENT-SIGNATURE.
curl -i -X POST https://api.jpverify.com/v1/batch-jobs \
  -H "X-JPVerify-Client: jpverify/1.0.1" \
  -H "Authorization: Bearer REPLACE_WITH_YOUR_OWN_RANDOM_TOKEN_32_CHARS_OR_MORE" \
  -H "Idempotency-Key: my-batch-job-0001" \
  -H "Content-Type: application/json" \
  -d '{"operation": "invoice_verify", "items": [{"registration_number": "T1013301046627"}, {"registration_number": "T1180301018771"}], "response_language": "en"}'
```
