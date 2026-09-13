## Description:

ClickSend API integration with managed authentication for sending SMS, MMS, and voice messages, managing contacts, lists, verified email addresses, account configuration, and tracking delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent access a user's ClickSend account through Maton for messaging, contact and list management, verified sender management, delivery tracking, and approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SMS, MMS, and voice sends reach real recipients and may incur costs.

Mitigation: Confirm recipient, message content, timing, and expected cost before any send or scheduled send.

Risk: Contact lists and verified email senders contain account data and personal data that can be changed or deleted.

Mitigation: Read or list current records first, verify exact identifiers, and require explicit approval before creating, updating, deleting, or moving records.

Risk: Maton and ClickSend credentials could be exposed if copied into logs, files, command lines, or trigger destination headers.

Mitigation: Use OAuth and the CLI credential store where possible, never print or persist credentials, and send Maton credentials only to Maton-controlled API endpoints.

Risk: Trigger destinations can create persistent forwarding of event payloads to external hosts.

Mitigation: Keep destinations on Maton-controlled hosts unless the user names and approves a specific third-party host after seeing the data fields and forwarding frequency.

Risk: Hosted functions and trigger event handlers can run automation without further human review.

Mitigation: Deploy only user-reviewed handlers with least-privilege connections and network policy, and require separate approval for function creation, deployment, invocation, and trigger binding.

## Reference(s):

- [ClickSend skill page](https://clawhub.ai/byungkyu/skills/clicksend)
- [byungkyu publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [ClickSend Developer Portal](https://developers.clicksend.com/)
- [ClickSend REST API v3 Documentation](https://developers.clicksend.com/docs)
- [ClickSend PHP SDK](https://github.com/ClickSend/clicksend-php)
- [ClickSend Help Center](https://help.clicksend.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is centered on authenticated ClickSend operations through Maton; write operations, connection changes, hosted functions, and trigger destinations require explicit user approval.]

## Skill Version(s):

1.2.4 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
