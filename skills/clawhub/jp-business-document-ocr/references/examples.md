# jp-business-document-ocr — request examples

Set `JPVERIFY_API_KEY` (create one at https://www.jpverify.com/signup?ref=jp-business-document-ocr). Without a key the API answers HTTP 402 with the x402 price; see https://api.jpverify.com/docs/x402 for x402 SDK code.

## `POST /jp-invoice/extract` — $0.01

```bash
curl -X POST https://api.jpverify.com/jp-invoice/extract \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-business-document-ocr/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"text": "請求書 株式会社ABC 登録番号 T1013301046627 請求日 2026年8月15日 支払期日 2026年9月30日 合計110000円 消費税10000円", "fields": ["supplier_name", "registration_number", "invoice_date", "due_date", "total", "tax_amount", "payment_terms"], "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/extract",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-business-document-ocr/1.0.1"},
    json={"text": "請求書 株式会社ABC 登録番号 T1013301046627 請求日 2026年8月15日 支払期日 2026年9月30日 合計110000円 消費税10000円", "fields": ["supplier_name", "registration_number", "invoice_date", "due_date", "total", "tax_amount", "payment_terms"], "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-invoice/extract-and-verify` — $0.05

```bash
curl -X POST https://api.jpverify.com/jp-invoice/extract-and-verify \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-business-document-ocr/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"text": "登録番号 T1013301046627 合計110000円 消費税10000円", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-invoice/extract-and-verify",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-business-document-ocr/1.0.1"},
    json={"text": "登録番号 T1013301046627 合計110000円 消費税10000円", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-receipt/extract` — $0.03

```bash
curl -X POST https://api.jpverify.com/jp-receipt/extract \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-business-document-ocr/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"text": "八福餃子房 2025年4月12日 21:18 登録番号 T1013301046627 合計12425円 内消費税1130円", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-receipt/extract",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-business-document-ocr/1.0.1"},
    json={"text": "八福餃子房 2025年4月12日 21:18 登録番号 T1013301046627 合計12425円 内消費税1130円", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-business-card/extract` — $0.03

```bash
curl -X POST https://api.jpverify.com/jp-business-card/extract \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-business-document-ocr/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"front_image_url": "https://www.jpverify.com/samples/business-card-front.png", "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-business-card/extract",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-business-document-ocr/1.0.1"},
    json={"front_image_url": "https://www.jpverify.com/samples/business-card-front.png", "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```

## `POST /jp-business-card/extract-and-enrich` — $0.10

```bash
curl -X POST https://api.jpverify.com/jp-business-card/extract-and-enrich \
  -H "Authorization: Bearer $JPVERIFY_API_KEY" \
  -H "X-JPVerify-Client: jp-business-document-ocr/1.0.1" \
  -H "Content-Type: application/json" \
  -d '{"front_image_url": "https://www.jpverify.com/samples/business-card-front.png", "back_image_url": "https://www.jpverify.com/samples/business-card-back.png", "output_format": "json", "include_raw_text": false, "response_language": "both"}'
```

```python
import os, requests

response = requests.post(
    "https://api.jpverify.com/jp-business-card/extract-and-enrich",
    headers={"Authorization": f"Bearer {os.environ['JPVERIFY_API_KEY']}",
             "X-JPVerify-Client": "jp-business-document-ocr/1.0.1"},
    json={"front_image_url": "https://www.jpverify.com/samples/business-card-front.png", "back_image_url": "https://www.jpverify.com/samples/business-card-back.png", "output_format": "json", "include_raw_text": False, "response_language": "both"},
    timeout=60,
)
print(response.status_code, response.json())
```
