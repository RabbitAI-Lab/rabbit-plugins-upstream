## Description: <br>
Builds and debugs Stripe integrations across payments, subscriptions, Checkout, invoices, webhooks, Connect, disputes, tax, testing, reconciliation, and go-live workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to build, debug, test, and launch Stripe payment, billing, marketplace, webhook, dispute, tax, and reconciliation workflows. It is most useful when an agent must produce concrete Stripe guidance, code examples, API calls, runbooks, or local configuration notes with explicit safety checks for live money movement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stripe operations can move money or change customer-visible billing state. <br>
Mitigation: Keep the default confirm-each live mode, verify test versus live keys before commands, and require explicit approval for refunds, payouts, cancellations, invoice finalization, deletes, and webhook changes. <br>
Risk: Saved incidents, disputes, evidence packets, recovery outreach, and account notes can contain sensitive business or customer context. <br>
Mitigation: Set retention and privacy rules for local notes, store only necessary context, and avoid saving credentials, card data, client secrets, or raw payment credentials. <br>
Risk: Environment-provided Stripe keys and webhook secrets grant access to real Stripe account operations. <br>
Mitigation: Keep secrets in environment variables or a secret manager, write only locator pointers such as env:STRIPE_SECRET_KEY, and strip secret values from generated notes and examples. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/stripe-api-integration) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic skill page](https://clawic.com/skills/stripe-api-integration) <br>
- [Skill overview](artifact/SKILL.md) <br>
- [Webhook guidance](artifact/webhooks.md) <br>
- [Go-live guidance](artifact/go-live.md) <br>
- [Testing guidance](artifact/testing.md) <br>
- [Local memory template](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks, shell commands, configuration snippets, and plain-language guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Stripe API calls and local note updates; live-mode writes require explicit confirmation under the default policy.] <br>

## Skill Version(s): <br>
1.0.4 (source: evidence.release.version and artifact/SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
