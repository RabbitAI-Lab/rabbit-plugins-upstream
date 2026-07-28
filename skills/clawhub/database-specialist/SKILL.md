---
name: "database-specialist"
description: >
  Database architecture design, SQL optimization, schema review and migration planning. AI-delivered service.
metadata:
  author: "Yujin"
  version: "1.0.26"
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

# database-specialist

## Skill Overview

Database specialist service covering architecture design, SQL query optimization, schema review, and migration planning. This is a paid service; payment verification is handled via clawtip, and the AI model delivers the actual diagnostic results in the conversation context.

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
No database schemas, connection strings, query logs, credentials, or project files are read or uploaded. Service results delivered by AI in conversation.

---

## Version History

| Version | Date | Notes |
|:---|:---|:---|
| 1.0.26 | 2026-07-28 | Fix ClawHub audit: remove false SM4 claims, accurate data handling disclosure |
| 1.0.1 | 2026-07-20 | Fix payment flow to match clawtip standard |
| 1.0.0 | 2026-07-19 | Initial release |