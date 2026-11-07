# jp-supplier-due-diligence — request examples

Set `JPVERIFY_API_KEY` (create one at https://www.jpverify.com/signup?ref=jp-supplier-due-diligence). Without a key the API answers HTTP 402 with the x402 price; see https://api.jpverify.com/docs/x402 for x402 SDK code.

## `POST /v1/suppliers/resolve` — $0.01

```bash
curl -X POST https://api.jpverify.com/v1/suppliers/resolve \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-supplier-due-diligence/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"name": "株式会社ABC", "registration_number": "T1013301046627", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/v1/suppliers/resolve",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-supplier-due-diligence/1.0.1"},
    json={"name": "株式会社ABC", "registration_number": "T1013301046627", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-invoice/check` — $0.03

```bash
curl -X POST https://api.jpverify.com/jp-invoice/check \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-supplier-due-diligence/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"registration_number": "T1013301046627", "supplier_name": "株式会社ABC", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/check",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-supplier-due-diligence/1.0.1"},
    json={"registration_number": "T1013301046627", "supplier_name": "株式会社ABC", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-regulated-entity/verify` — $0.03

```bash
curl -X POST https://api.jpverify.com/jp-regulated-entity/verify \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-supplier-due-diligence/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"corporate_number": "1234567890123", "categories": ["funds_transfer_business"], "response_language": "en"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-regulated-entity/verify",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-supplier-due-diligence/1.0.1"},
    json={"corporate_number": "1234567890123", "categories": ["funds_transfer_business"], "response_language": "en"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `GET /jp-company/filings` — $0.01

```bash
curl -G https://api.jpverify.com/jp-company/filings \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-supplier-due-diligence/1.0.1" \
  --data-urlencode 'edinet_code=E00000' \
  --data-urlencode 'limit=20' \
  --data-urlencode 'response_language=en'
```

```python
import os, requests

response = requests.get(
    "https://api.jpverify.com/jp-company/filings",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-supplier-due-diligence/1.0.1"},
    params={"edinet_code": "E00000", "limit": 20, "response_language": "en"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /v1/entities/resolve-cross-border` — $0.04

```bash
curl -X POST https://api.jpverify.com/v1/entities/resolve-cross-border \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-supplier-due-diligence/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"country_code": "GB", "identifiers": {"company_number": "00000006"}, "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/v1/entities/resolve-cross-border",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-supplier-due-diligence/1.0.1"},
    json={"country_code": "GB", "identifiers": {"company_number": "00000006"}, "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /v1/invoices/counterparty-check` — $0.05

```bash
curl -X POST https://api.jpverify.com/v1/invoices/counterparty-check \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-supplier-due-diligence/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"vat_id": "DE123456789", "participant_id": "iso6523-actorid-upis::0088:123456789", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/v1/invoices/counterparty-check",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-supplier-due-diligence/1.0.1"},
    json={"vat_id": "DE123456789", "participant_id": "iso6523-actorid-upis::0088:123456789", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `GET /v1/entities/{cik}/filing-risk-snapshot` — $0.05

```bash
curl -G https://api.jpverify.com/v1/entities/0000320193/filing-risk-snapshot \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-supplier-due-diligence/1.0.1"
```

```python
import os, requests

response = requests.get(
    "https://api.jpverify.com/v1/entities/0000320193/filing-risk-snapshot",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-supplier-due-diligence/1.0.1"},
    timeout=60,
)
print(response.status_code, response.json())
```
