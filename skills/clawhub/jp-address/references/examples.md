# jp-address — request examples

Set `JPVERIFY_API_KEY` (create one at https://www.jpverify.com/signup?ref=jp-address). Without a key the API answers HTTP 402 with the x402 price; see https://api.jpverify.com/docs/x402 for x402 SDK code.

## `POST /jp-address/normalize` — $0.005

```bash
curl -X POST https://api.jpverify.com/jp-address/normalize \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-address/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"address": "東京都新宿区西新宿2丁目8番1号", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-address/normalize",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-address/1.0.1"},
    json={"address": "東京都新宿区西新宿2丁目8番1号", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-address/validate` — $0.005

```bash
curl -X POST https://api.jpverify.com/jp-address/validate \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-address/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"address": "東京都千代田区千代田1丁目1番1号", "required_level": 8, "strict": false}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-address/validate",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-address/1.0.1"},
    json={"address": "東京都千代田区千代田1丁目1番1号", "required_level": 8, "strict": False},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-address/parse` — $0.005

```bash
curl -X POST https://api.jpverify.com/jp-address/parse \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-address/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"address": "東京都千代田区千代田1丁目1番1号", "response_language": "ja"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-address/parse",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-address/1.0.1"},
    json={"address": "東京都千代田区千代田1丁目1番1号", "response_language": "ja"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-address/geocode` — $0.005

```bash
curl -X POST https://api.jpverify.com/jp-address/geocode \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-address/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"address": "東京都千代田区千代田1丁目1番1号", "max_candidates": 3}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-address/geocode",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-address/1.0.1"},
    json={"address": "東京都千代田区千代田1丁目1番1号", "max_candidates": 3},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-address/postal-lookup` — $0.001

```bash
curl -X POST https://api.jpverify.com/jp-address/postal-lookup \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-address/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"postal_code": "100-0001", "max_results": 10}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-address/postal-lookup",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-address/1.0.1"},
    json={"postal_code": "100-0001", "max_results": 10},
    timeout=60,
)
print(response.status_code, response.json())
```
