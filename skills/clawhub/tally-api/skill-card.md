## Description:

Tally API integration with managed OAuth for managing forms, submissions, workspaces, webhooks, organization users, and organization invites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Tally accounts through managed OAuth, primarily reading and managing forms, submissions, workspaces, webhooks, and organization membership. Write operations, new connections, hosted functions, triggers, and external forwarding flows require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized writes and organization membership operations can modify Tally account data or account access.

Mitigation: Confirm the exact target resource, payload, and intended effect with the user before POST, PUT, PATCH, DELETE, connection, invite, or user-removal actions.

Risk: Webhooks, triggers, and destinations can persistently forward form submissions or other personal data to external URLs.

Mitigation: Confirm the exact destination, who controls it, what data flows there, and that forwarding is persistent; use only user-provided destinations and remove flows that are no longer needed.

Risk: Maton API keys and OAuth connections can expose or authorize access to the user's Tally data.

Mitigation: Prefer OAuth and the credential store, avoid long-lived environment variables where possible, scope connections to the task, and avoid logging raw API responses.

Risk: Local event handlers and hosted functions can run code against user-connected services.

Mitigation: Use user-authored or user-reviewed handlers only, summarize least-privilege access and network policy before deployment or invocation, and require separate approval for each hosted automation action.

## Reference(s):

- [Tally API Introduction](https://developers.tally.so/api-reference/introduction)
- [Tally API Reference](https://developers.tally.so/llms.txt)
- [Tally Help Center](https://help.tally.so/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
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

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with inline shell, HTTP, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are authenticated through the user's Maton connection and should minimize personal data exposure.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
