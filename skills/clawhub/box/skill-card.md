## Description:

Box API integration with managed OAuth for managing files, folders, collaborations, shared links, webhooks, and cloud storage through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to manage Box files, folders, collaborations, shared links, webhooks, and automation through a user-approved Maton Box connection. It is suited for read, list, upload, download, sharing, organization, and approved automation workflows against Box data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Box authorization can expose or modify files, folders, shared links, collaborations, and cloud storage beyond the immediate request.

Mitigation: Review OAuth scopes carefully, prefer read-only access when possible, and confirm every write, share, or delete action with the target and intended effect before execution.

Risk: Persistent automation, webhooks, trigger destinations, and hosted functions can continue forwarding or changing data after setup.

Mitigation: Create or update them only after explicit approval of the destination, payload, cadence, and network policy; review and remove them when no longer needed.

Risk: Long-lived Maton API keys and raw Box responses can leak credentials or personal and business data.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist secrets, and extract only the response fields needed for the user's task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/box)
- [Maton homepage](https://maton.ai)
- [Box API Reference](https://developer.box.com/reference)
- [Box Developer Documentation](https://developer.box.com/guides)
- [Box Authentication Guide](https://developer.box.com/guides/authentication)
- [Box SDKs](https://developer.box.com/sdks-and-tools)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time trigger catalogue](references/time/triggers.md)
- [GitHub trigger catalogue](references/github/triggers.md)
- [Google Mail trigger catalogue](references/google-mail/triggers.md)
- [Slack trigger catalogue](references/slack/triggers.md)
- [Stripe trigger catalogue](references/stripe/triggers.md)
- [Calendly trigger catalogue](references/calendly/triggers.md)
- [HubSpot trigger catalogue](references/hubspot/triggers.md)
- [Linear trigger catalogue](references/linear/triggers.md)
- [Notion trigger catalogue](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, HTTP examples, JSON response examples, and code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-approved Box OAuth connection; write, share, delete, webhook, and persistent automation actions require explicit confirmation.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
