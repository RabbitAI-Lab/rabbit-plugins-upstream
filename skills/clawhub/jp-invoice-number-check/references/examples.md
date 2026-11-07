# jp-invoice-number-check — request examples

Set `JPVERIFY_API_KEY` (create one at https://www.jpverify.com/signup?ref=jp-invoice-number-check). Without a key the API answers HTTP 402 with the x402 price; see https://api.jpverify.com/docs/x402 for x402 SDK code.

## `POST /jp-invoice/verify` — $0.01

```bash
curl -X POST https://api.jpverify.com/jp-invoice/verify \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-invoice-number-check/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"registration_number": "T1013301046627", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/verify",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-invoice-number-check/1.0.1"},
    json={"registration_number": "T1013301046627", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-invoice/check` — $0.03

```bash
curl -X POST https://api.jpverify.com/jp-invoice/check \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-invoice-number-check/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"registration_number": "T1013301046627", "supplier_name": "株式会社ABC", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/check",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-invoice-number-check/1.0.1"},
    json={"registration_number": "T1013301046627", "supplier_name": "株式会社ABC", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-invoice/verify-batch` — $0.05

```bash
curl -X POST https://api.jpverify.com/jp-invoice/verify-batch \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-invoice-number-check/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"registration_numbers": ["T1013301046627"], "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/verify-batch",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-invoice-number-check/1.0.1"},
    json={"registration_numbers": ["T1013301046627"], "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```
