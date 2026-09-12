## Description:

Clio API integration with managed OAuth for reading, creating, updating, and deleting Clio Manage legal-practice data such as matters, contacts, activities, tasks, documents, calendar entries, time entries, and billing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, legal-operations teams, and agents use this skill to work with Clio Manage data through Maton-managed OAuth while keeping write, delete, connection, trigger, and hosted-function actions subject to explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Clio legal-practice data through Maton-mediated OAuth.

Mitigation: Install only when that access is acceptable, use OAuth with the narrowest available Clio scopes, and remove unused Clio connections, functions, triggers, and destinations.

Risk: The skill supports write and delete operations that could change matters, contacts, activities, tasks, documents, calendar entries, time entries, or billing data.

Mitigation: Default to read and list calls, and confirm every write or deletion by exact resource identifier before execution.

Risk: External destinations or hosted functions can forward Clio-derived data outside the platform if intentionally configured.

Mitigation: Avoid external destination URLs unless the user intentionally wants ongoing forwarding; deploy Clio-related functions with DENY_ALL networking and only the Clio connection they were written for.

## Reference(s):

- [Clio Skill Page](https://clawhub.ai/byungkyu/skills/clio)
- [Maton Homepage](https://maton.ai)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [Clio API Documentation](https://docs.developers.clio.com/api-reference/)
- [Clio Fields Guide](https://docs.developers.clio.com/api-docs/clio-manage/fields/)
- [Clio Rate Limits](https://docs.developers.clio.com/api-docs/clio-manage/rate-limits/)
- [Clio Permissions](https://docs.developers.clio.com/api-docs/permissions/)
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

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash, Python, JSON, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user approval for Clio writes, deletes, connection changes, triggers, and hosted functions.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
