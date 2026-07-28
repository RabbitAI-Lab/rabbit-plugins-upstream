---
name: "soft-ip-full-lifecycle-delivery-pro"
description: >
  Software copyright registration full lifecycle delivery: generate and complete all 8 application documents (application form, source code documentation, user manual, rights declaration, etc.) for Chinese software copyright filing. AI-delivered service; works best after running soft-ip-full-lifecycle-zijian for compliance diagnosis first. Payment verification via clawtip. Question text and order metadata are transmitted via HTTPS to api.ideaidea.com.cn for order creation and fulfillment.
metadata:
  author: "Yujin"
  version: "1.1.1"
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

# soft-ip-full-lifecycle-delivery-pro

## Skill Overview

Software copyright registration full lifecycle delivery service. This is a paid service; payment verification is handled via clawtip, and the AI model delivers document drafting and application material preparation in the conversation context.

**Direct execution:** If the user has already provided an <<order_no>> (and the order file already contains payCredential), skip directly to the third stage.

### Relationship with soft-ip-full-lifecycle-zijian

| | zijian (diagnostic edition) | delivery-pro (this skill, generation edition) |
|---|---|---|
| Purpose | Compliance diagnosis: identify gaps and issues | Document generation and delivery: fill out all 8 application materials |
| Price | 190 UT (1.9 yuan) | 690 UT (6.9 yuan) |
| Output | Gap checklist + issue annotations + risk grading | Complete submission-ready document drafts |
| Suggested order | Run first: diagnose issues and supplement materials | Run after: generate documents based on supplemented materials |

**Recommended: run zijian first for compliance review, confirm materials are complete, then use this skill for document generation.**

### Capabilities

- Application form assistance: standardized entry of software name, version, classification
- Source code documentation: auto-extraction and formatting of first/last 30 pages
- User manual generation: framework based on software feature descriptions
- Rights attribution documents: ownership declaration templates, collaboration agreement frameworks
- Application material summary: cross-consistency check across all 8 documents

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
No source code, application documents, copyright holder personal information, company information, or draft content is read or uploaded. Service results delivered by AI in conversation.

---

## Version History

| Version | Date | Notes |
|:---|:---|:---|
| 1.1.1 | 2026-07-28 | Fix ClawHub audit: remove false SM4 claims, accurate AI-delivered disclosure, remove Chinese-only policy |
| 1.1.0 | 2026-07-20 | Restructured SKILL.md: capability-first layout, explicit differentiation from zijian edition |
| 1.0.1 | 2026-07-20 | Fix payment flow to match clawtip standard |
| 1.0.0 | 2026-07-19 | Initial release |