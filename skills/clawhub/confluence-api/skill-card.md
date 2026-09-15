## Description:

Confluence API integration with managed OAuth for managing Confluence pages, spaces, blog posts, comments, attachments, and properties.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to help agents access authorized Confluence Cloud workspaces through Maton for content retrieval, content management, and approved automation setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Confluence content after the user authorizes a connection.

Mitigation: Prefer read/list operations first, use least-privilege OAuth scopes, and require explicit user approval before writes, deletes, new connections, functions, triggers, or destinations.

Risk: Trigger destinations can create persistent automatic forwarding of future event data.

Mitigation: Approve each destination separately, name the exact host and fields that will be sent, prefer platform destinations, and remove unused destinations.

Risk: API keys are long-lived credentials and may be exposed to child processes if exported into the environment.

Mitigation: Prefer OAuth through the Maton CLI and credential store; use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/confluence-api)
- [Maton Homepage](https://maton.ai)
- [Confluence REST API V2 Documentation](https://developer.atlassian.com/cloud/confluence/rest/v2/intro/)
- [Confluence REST API V2 Reference](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/)
- [Confluence Storage Format](https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Confluence connection.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
