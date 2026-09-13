## Description:

Kit (formerly ConvertKit) API integration with managed OAuth for managing email subscribers, forms, tags, sequences, broadcasts, custom fields, purchase records, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a Kit email marketing account through Maton-managed authentication, including subscriber, tag, form, sequence, broadcast, purchase, and webhook workflows. The skill is also used to propose carefully approved automation through Maton functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Homebrew installation can resolve a different Maton build than the reviewed release.

Mitigation: Prefer the pinned npm command when possible, and review any Homebrew-resolved Maton version before authenticating.

Risk: Writes, webhooks, destinations, functions, and triggers can change account state or create persistent data flows.

Mitigation: Approve these actions only after checking the target account, destination URL, data fields, intended effect, and persistence.

Risk: Subscriber, purchase, email, CRM, payment, and trigger event data can contain personal or sensitive information.

Mitigation: Retrieve only the fields needed for the task, avoid dumping raw responses, and use templates that forward the minimum required data.

Risk: Raw HTTP or API-key fallback can expose a long-lived credential if handled loosely.

Mitigation: Use OAuth through the Maton CLI where available, avoid exporting credentials broadly, and keep tokens out of logs, files, command lines, and destinations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/kit)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Kit API Overview](https://developers.kit.com/api-reference/overview)
- [Kit API Subscribers](https://developers.kit.com/api-reference/subscribers/list-subscribers)
- [Kit API Tags](https://developers.kit.com/api-reference/tags/list-tags)
- [Kit API Forms](https://developers.kit.com/api-reference/forms/list-forms)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
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

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with bash, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated Maton CLI/API operations; write actions require explicit user approval.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
