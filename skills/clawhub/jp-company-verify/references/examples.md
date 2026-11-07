# jp-company-verify — request examples

Set `JPVERIFY_API_KEY` (create one at https://www.jpverify.com/signup?ref=jp-company-verify). Without a key the API answers HTTP 402 with the x402 price; see https://api.jpverify.com/docs/x402 for x402 SDK code.

## `POST /jp-company/verify` — $0.005

```bash
curl -X POST https://api.jpverify.com/jp-company/verify \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-company-verify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"name": "トヨタ自動車株式会社", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-company/verify",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-company-verify/1.0.1"},
    json={"name": "トヨタ自動車株式会社", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-company/report` — $0.05

```bash
curl -X POST https://api.jpverify.com/jp-company/report \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-company-verify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"name": "株式会社ABC", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-company/report",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-company-verify/1.0.1"},
    json={"name": "株式会社ABC", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-company/verify-batch` — $0.05

```bash
curl -X POST https://api.jpverify.com/jp-company/verify-batch \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-company-verify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"items": [{"corporate_number": "1180301018771"}], "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-company/verify-batch",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-company-verify/1.0.1"},
    json={"items": [{"corporate_number": "1180301018771"}], "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `GET /jp-company/filings` — $0.01

```bash
curl -G https://api.jpverify.com/jp-company/filings \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-company-verify/1.0.1" \
  --data-urlencode 'edinet_code=E00000' \
  --data-urlencode 'limit=20' \
  --data-urlencode 'response_language=en'
```

```python
import os, requests

response = requests.get(
    "https://api.jpverify.com/jp-company/filings",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-company-verify/1.0.1"},
    params={"edinet_code": "E00000", "limit": 20, "response_language": "en"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-regulated-entity/verify` — $0.03

```bash
curl -X POST https://api.jpverify.com/jp-regulated-entity/verify \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-company-verify/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"corporate_number": "1234567890123", "categories": ["funds_transfer_business"], "response_language": "en"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-regulated-entity/verify",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-company-verify/1.0.1"},
    json={"corporate_number": "1234567890123", "categories": ["funds_transfer_business"], "response_language": "en"},
    timeout=60,
)
print(response.status_code, response.json())
```
