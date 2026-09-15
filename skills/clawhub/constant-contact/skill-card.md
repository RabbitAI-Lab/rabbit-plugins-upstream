## Description:

Constant Contact API integration with managed OAuth for reading and administering contacts, campaigns, lists, tags, custom fields, segments, bulk operations, and marketing analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing operations teams use this skill to let an agent work with Constant Contact data through Maton-authenticated API calls. It is suited for tasks such as inspecting account state, managing contact records and lists, reviewing analytics, and preparing or approving high-impact campaign operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer Constant Contact data, including writes, bulk changes, exports, and campaign send or schedule actions.

Mitigation: Review every write, export, campaign send, function, trigger, and destination before approval, with specific resource identifiers and expected consequences.

Risk: Long-lived API keys and raw HTTP calls increase credential exposure risk.

Mitigation: Prefer OAuth through the Maton CLI, avoid raw HTTP unless the CLI is unavailable, and never expose credentials in command arguments, files, destinations, or logs.

Risk: Functions, triggers, and destinations can create persistent automation or data-forwarding paths.

Mitigation: Approve automation separately, keep destinations on platform-controlled endpoints unless a specific external host is approved, and revoke or delete unused connections, functions, triggers, and destinations promptly.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/constant-contact)
- [Maton](https://maton.ai)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
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

**Output Format:** [Markdown guidance with shell commands, JSON examples, and API request snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Maton CLI commands, raw HTTP fallbacks, hosted function code, and trigger configuration; write, export, send, automation, and destination operations require explicit user approval.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
