---
name: "innovation-research"
description: >
  Technology innovation research, patent landscape analysis, and emerging tech evaluation. AI-delivered service.
metadata:
  author: "Yujin"
  version: "1.0.21"
  category: "expert"
  capabilities:
    - "payment.process"
  permissions:
    - "network.outbound"
    - "credential.read"
    - "filesystem.read"
    - "filesystem.write"
  requires:
    - "clawtip-skill"
---

# innovation-research

Please interact with users in Chinese.

## Skill Overview

Innovation research service providing technology stack analysis, patent landscape review, competitive comparison, and emerging technology evaluation. This is a paid service; payment verification is handled via clawtip, and the AI model delivers the actual research results in the conversation context.

**Direct execution:** If the user has already provided an <<order_no>> (and the order file already contains payCredential), skip directly to the third stage.

---

## First Stage: Create Order

### 1. Required Parameters
* `<question>`: the user specific question or content.

### 2. Execution Command
```bash
python3 scripts/create_order.py "<question>"
```

### 3. Output Processing
**On success:** ORDER_NO, AMOUNT, QUESTION, INDICATOR
AMOUNT is in RMB fen (divide by 100 for yuan).
**On failure:** ORDER_CREATION_FAILED: <error> then exit 1

---

## Second Stage: Payment Processing

Use skill `clawtip` to process payment with `order_no` and `indicator`.

---

## Third Stage: Service Execution

```bash
python3 scripts/service.py "<order_no>"
```

Output: PAY_STATUS: SUCCESS|PROCESSING|FAIL|ERROR

---

## Data Handling

### Local Storage
Order metadata saved to ~/.openclaw/skills/orders/{indicator}/{order_no}.json (skill-id, order_no, amount, question, encrypted_data, pay_to, description, slug, resource_url).

### Remote Transmission
- Phase 1: Sends slug + question text to api.ideaidea.com.cn via HTTPS
- Phase 2: clawtip reads local order file, writes payCredential back
- Phase 3: Sends slug, order_no, encrypted payCredential to api.ideaidea.com.cn

### Not Collected or Transmitted
No source code, project files, credentials, or API keys. Service results delivered by AI in conversation.

---

## Version History

| Version | Date | Notes |
|:---|:---|:---|
| 1.0.21 | 2026-07-27 | Fix ClawHub audit: accurate description, remove misleading NOTICE claims |
| 1.0.1 | 2026-07-20 | Fix payment flow to match clawtip standard |
| 1.0.0 | 2026-07-19 | Initial release |