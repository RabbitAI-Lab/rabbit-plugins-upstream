---
name: "soft-ip-full-lifecycle-zijian"
description: >
  Software IP full lifecycle self-assessment: material completeness review, compliance verification, and registration readiness audit for Chinese software copyright applications. AI-delivered service. Question text and order metadata are transmitted via HTTPS to api.ideaidea.com.cn for order creation and fulfillment. No source code or project files are uploaded.
metadata:
  author: "Yujin"
  version: "3.1.34"
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

# soft-ip-full-lifecycle-zijian

## Skill Overview

Software IP full lifecycle self-assessment and compliance review service. This is a paid service; payment verification is handled via clawtip, and the AI model delivers compliance diagnosis and material review in the conversation context.

**Direct execution:** If the user has already provided an <<order_no>> (and the order file already contains payCredential), skip directly to the third stage.

### Relationship with soft-ip-full-lifecycle-delivery-pro

| | zijian (this skill, diagnostic edition) | delivery-pro (generation edition) |
|---|---|---|
| Purpose | Compliance diagnosis: identify gaps and issues | Document generation and delivery: fill out all 8 application materials |
| Price | 190 UT (1.9 yuan) | 690 UT (6.9 yuan) |
| Output | Gap checklist + issue annotations + risk grading | Complete submission-ready document drafts |
| Suggested order | Run first: diagnose issues and supplement materials | Run after: generate documents based on supplemented materials |

**Recommended: run this skill first for compliance review, then use delivery-pro for document generation.**

### Capabilities

- Material completeness review: checklist against copyright registration requirements
- Source code documentation compliance: format validation, 30-page requirement check
- User manual audit: screenshot format, feature description completeness
- Rights attribution check: ownership declarations, collaboration agreements
- Registration readiness audit: risk grading (blocking/advisory/informational)

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
No source code, application documents, company information, contract files, trade secrets, or personal identity information is read or uploaded. Service results delivered by AI in conversation.

---

## Version History

| Version | Date | Notes |
|:---|:---|:---|
| 3.1.34 | 2026-07-28 | Fix ClawHub audit: remove false SM4 claims, accurate AI-delivered disclosure, remove Chinese-only policy, remove false local-processing claims |
| 3.1.33 | 2026-07-20 | Security review: restructured for SkillSpector compliance |
| 3.1.32 | 2026-07-20 | Previous release |