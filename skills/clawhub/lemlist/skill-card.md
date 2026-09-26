## Description:

Lemlist API integration with managed OAuth for managing campaigns, leads, activities, schedules, sequences, and unsubscribes in sales automation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, revenue operations, and developer users use this skill to work with Lemlist account data through Maton-authenticated API calls. It supports reviewed workflows for reading data, making approved writes, and optionally wiring approved hosted functions or triggers around Lemlist actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations or new Lemlist connections can change account data or authorization state.

Mitigation: Default to read and list calls, and require explicit user confirmation before creating connections or running POST, PUT, PATCH, or DELETE requests.

Risk: Hosted functions, triggers, and destinations can continue acting on future events after setup.

Mitigation: Require user approval for each deploy, invocation, trigger, or destination, and use least-privilege connection selection with DENY_ALL network policy where documented.

Risk: Maton API keys and Lemlist responses can expose credentials, business data, or personal data.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting keys, and extract only the fields needed for the user's task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/lemlist)
- [Maton Homepage](https://maton.ai)
- [Lemlist API Documentation](https://developer.lemlist.com/)
- [Lemlist API Reference](https://developer.lemlist.com/api-reference)
- [Lemlist Help Center - API](https://help.lemlist.com/en/collections/17109856-api-webhooks)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly trigger catalog](references/calendly/triggers.md)
- [GitHub trigger catalog](references/github/triggers.md)
- [Google Mail trigger catalog](references/google-mail/triggers.md)
- [HubSpot trigger catalog](references/hubspot/triggers.md)
- [Linear trigger catalog](references/linear/triggers.md)
- [Notion trigger catalog](references/notion/triggers.md)
- [Slack trigger catalog](references/slack/triggers.md)
- [Stripe trigger catalog](references/stripe/triggers.md)
- [Time trigger catalog](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code blocks, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP examples for restricted environments, endpoint guidance, and approval prompts for writes or automation.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
