## Description:

ClickSend API integration with managed authentication for sending SMS, MMS, and voice messages, managing contacts, lists, verified email addresses, and account configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to work with a connected ClickSend account through Maton: send approved SMS, MMS, and voice messages, manage contact lists and verified sender addresses, inspect account data, and optionally configure approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messaging operations can send SMS, MMS, or voice messages to real recipients and may incur costs.

Mitigation: Confirm recipient, content, send timing, and expected cost before approving any send operation.

Risk: Contact, list, and verified email address changes can modify account data or sender identities.

Mitigation: Review the exact target resource and payload before approving create, update, or delete operations.

Risk: Hosted functions, triggers, and destinations can continue running or forwarding data after setup.

Mitigation: Approve each automation separately, restrict destinations to intended hosts, use least-privilege scopes, and delete unused connections, functions, or triggers.

Risk: ClickSend account data and trigger payloads may contain personal, business, or payment-related information.

Mitigation: Forward only the minimum fields needed for the task, avoid logging raw responses, and prefer Maton-controlled destinations unless the user explicitly approves a third-party host.

## Reference(s):

- [ClawHub ClickSend Skill](https://clawhub.ai/byungkyu/skills/clicksend)
- [byungkyu Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [ClickSend Developer Portal](https://developers.clicksend.com/)
- [ClickSend REST API v3 Documentation](https://developers.clicksend.com/docs)
- [ClickSend PHP SDK](https://github.com/ClickSend/clicksend-php)
- [ClickSend Help Center](https://help.clicksend.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit approval before write operations or new connections.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
