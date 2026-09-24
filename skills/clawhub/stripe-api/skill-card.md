## Description:

Stripe API integration with managed OAuth for customers, subscriptions, invoices, products, prices, payments, and related Stripe administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to perform Stripe administration through a managed OAuth connection, including read/list workflows and explicitly approved writes. It also provides guidance for hosted functions and triggers when users intentionally create Stripe-related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial writes may create, modify, refund, or delete Stripe resources in the wrong account or mode.

Mitigation: Require explicit approval that names the endpoint, target resource, object IDs, amounts, and test or live mode before every write.

Risk: A broad or stale Stripe connection may expose more payment and customer data than the task requires.

Mitigation: Use the least-privileged Stripe connection available, verify the connection ID before each request, and revoke unused connections promptly.

Risk: Persistent triggers can continuously forward Stripe payment events containing PII or card-related metadata.

Mitigation: Create trigger destinations only when the user intentionally requests ongoing automation, approve the destination, and forward only required fields.

Risk: Long-lived Maton credentials can be exposed through environment variables or logs.

Mitigation: Prefer OAuth through the Maton CLI credential store, avoid persistent MATON_API_KEY use, and do not log raw API responses or secrets.

## Reference(s):

- [Stripe API Reference](https://docs.stripe.com/api)
- [Stripe Dashboard](https://dashboard.stripe.com/)
- [Stripe Testing](https://docs.stripe.com/testing)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/stripe-api)
- [Stripe Trigger Reference](artifact/references/stripe/triggers.md)
- [Time Trigger Reference](artifact/references/time/triggers.md)
- [Calendly Trigger Reference](artifact/references/calendly/triggers.md)
- [GitHub Trigger Reference](artifact/references/github/triggers.md)
- [Google Mail Trigger Reference](artifact/references/google-mail/triggers.md)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Linear Trigger Reference](artifact/references/linear/triggers.md)
- [Notion Trigger Reference](artifact/references/notion/triggers.md)
- [Slack Trigger Reference](artifact/references/slack/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval for connection creation, writes, hosted functions, and persistent triggers.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
