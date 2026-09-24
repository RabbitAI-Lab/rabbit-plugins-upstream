## Description:

Quo API integration with managed OAuth for managing calls, messages, contacts, conversations, call recordings, and transcripts in a business phone system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operators use this skill to work with Quo business-phone data through Maton-managed authentication, including SMS, calls, contacts, conversations, recordings, transcripts, and approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Quo business-phone data through a Maton connection, including calls, messages, contacts, conversations, recordings, and transcripts.

Mitigation: Install only when Quo access through Maton is intended, use the least-privilege connection available, and avoid exposing raw responses unless the user asked for the specific data.

Risk: Writes, new connections, functions, triggers, webhooks, and deletions can change business-phone data or create ongoing behavior.

Mitigation: Require explicit user approval for each operation and summarize the target resource, payload, and expected effect before execution.

Risk: Persistent forwarding destinations can continue sending future messages, calls, or event data until removed.

Mitigation: Approve the exact destination URL and transmitted fields separately, prefer Maton-controlled destinations, review existing forwarding, and remove destinations that are no longer needed.

## Reference(s):

- [Quo Skill Page](https://clawhub.ai/byungkyu/skills/quo)
- [Maton Homepage](https://maton.ai)
- [Quo API Introduction](https://www.quo.com/docs/mdx/api-reference/introduction)
- [Quo API Authentication](https://www.quo.com/docs/mdx/api-reference/authentication)
- [Quo Support Center](https://support.quo.com/core-concepts/integrations/api)
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

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is task-scoped and should be reviewed before write operations, new connections, functions, triggers, webhooks, or persistent forwarding destinations.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
