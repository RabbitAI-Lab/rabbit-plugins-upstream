## Description: <br>
Builds and debugs Stripe integrations for payments, subscriptions, Checkout, invoices, webhooks, Connect, disputes, tax, go-live work, and operational troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and operators use this skill to build, debug, and operate Stripe payment systems, including money movement, recurring billing, webhook handling, marketplace flows, disputes, tax, testing, and reconciliation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help operate live Stripe money movement, including charges, refunds, transfers, payouts, deletions, invoice finalization, and customer-visible changes. <br>
Mitigation: Use test or restricted keys where possible and require explicit confirmation before live writes or other state-changing actions. <br>
Risk: The skill keeps Stripe operational memory and shared finance, contact, and device pointers under ~/Clawic/data/. <br>
Mitigation: Review the local Clawic data paths for sensitivity and keep stored records to durable operational context rather than unnecessary customer or account detail. <br>
Risk: Stripe secret keys, webhook signing secrets, client secrets, or raw card data could create payment and privacy exposure if copied into saved notes or logs. <br>
Mitigation: Store credential pointers such as env:STRIPE_SECRET_KEY or vault item names, not credential values, client secrets, card numbers, or CVCs. <br>
Risk: Incorrect payment guidance can cause duplicate charges, wrong amounts, broken fulfillment, failed renewals, or unreconciled payouts. <br>
Mitigation: Review generated API calls and code for idempotency, currency minor units, webhook-driven fulfillment, explicit mode, and reconciliation from balance transactions before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/stripe-api-integration) <br>
- [Publisher Profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic Skill Homepage](https://clawic.com/skills/stripe-api-integration) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [API Mechanics Guidance](artifact/api-mechanics.md) <br>
- [Webhook Guidance](artifact/webhooks.md) <br>
- [Go-Live Guidance](artifact/go-live.md) <br>
- [Stripe Working File Templates](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline API examples, shell commands, JSON payloads, configuration notes, checklists, and concise troubleshooting explanations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local operational memory updates under ~/Clawic/data/stripe-api-integration/ and shared Clawic data paths; requires STRIPE_SECRET_KEY and STRIPE_WEBHOOK_SECRET for live Stripe API and webhook work.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
