## Description:

Attio API integration with managed OAuth for managing CRM records, objects, tasks, notes, comments, lists, meetings, and related workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Attio CRM data through Maton-managed authentication, with read/list operations as the default and explicit approval required for writes, new connections, hosted functions, and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attio and Maton credentials can expose CRM data if OAuth connections or API keys are mishandled.

Mitigation: Prefer OAuth, use the operating system credential store, avoid long-lived API keys unless the CLI cannot be installed, and verify the active profile before calls.

Risk: Write operations or new connections can change CRM data or broaden account access.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit user approval before creating connections or making POST, PUT, PATCH, or DELETE requests.

Risk: Hosted functions and triggers can continue running after setup and can act on future events.

Mitigation: Use user-authored or user-reviewed handlers, require separate approval for creation, deployment, invocation, and trigger setup, prefer DENY_ALL network policy, and delete automations when the task is complete.

## Reference(s):

- [ClawHub Attio Skill](https://clawhub.ai/byungkyu/skills/attio-api)
- [Maton Homepage](https://maton.ai)
- [Attio API Overview](https://docs.attio.com/rest-api/overview)
- [Attio API Reference](https://docs.attio.com/rest-api/endpoint-reference)
- [Records API](https://docs.attio.com/rest-api/endpoint-reference/records)
- [Objects API](https://docs.attio.com/rest-api/endpoint-reference/objects)
- [Tasks API](https://docs.attio.com/rest-api/endpoint-reference/tasks)
- [Rate Limiting](https://docs.attio.com/rest-api/guides/rate-limiting)
- [Pagination](https://docs.attio.com/rest-api/guides/pagination)
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

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces authenticated Attio API workflows and Maton automation guidance; it does not itself return Attio data.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
