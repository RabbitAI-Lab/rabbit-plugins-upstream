## Description:

GetResponse API integration with managed OAuth for managing email marketing campaigns, contacts, newsletters, autoresponders, segments, workflows, ecommerce resources, SMS, landing pages, webinars, transactional email, forms, and account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate GetResponse marketing, automation, ecommerce, SMS, webinar, transactional email, form, and account workflows through an authenticated Maton connection. It supports read-first API work and user-approved writes, sends, deletes, connection changes, hosted functions, and trigger-backed automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and using unverified third-party CLI or SDK packages can expose the environment or credentials.

Mitigation: Verify the Maton package sources before installation and prefer an isolated, non-privileged environment.

Risk: GetResponse write, send, delete, and automation actions can affect real contacts, campaigns, SMS messages, and account data.

Mitigation: Default to read-only calls, request explicit user approval for each write or automation action, and confirm audience, content, timing, and target connection before execution.

Risk: Over-broad GetResponse authorization can expose more account data than the task requires.

Mitigation: Connect only the account and OAuth scopes needed for the current task.

Risk: Trigger-backed automation can forward data to destinations the user did not intend.

Mitigation: Avoid third-party trigger destinations unless the user explicitly approves the data being forwarded and the destination.

## Reference(s):

- [GetResponse API Documentation](https://apidocs.getresponse.com/v3)
- [GetResponse OpenAPI Spec](https://apireference.getresponse.com/open-api.json)
- [Maton Homepage](https://maton.ai)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated API call instructions and should minimize exposure of raw response data.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
