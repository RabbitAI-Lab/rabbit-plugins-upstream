## Description:

Provides guided Google Tag Manager API access through Maton managed OAuth for managing accounts, containers, workspaces, tags, triggers, variables, versions, environments, and user permissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing operations teams, and analytics engineers use this skill to inspect and manage Google Tag Manager resources through authenticated Maton API calls. It supports read/list workflows by default and requires explicit confirmation for writes, publishing, permission changes, connections, functions, triggers, and deletion actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Tag Manager write, publish, and permission actions can alter production containers or account access.

Mitigation: Default to read/list calls, grant the narrowest available OAuth scopes, verify the target account or connection, and require explicit confirmation before writes, publishing, permission changes, or deletion.

Risk: Long-lived API keys or broad environment exposure can leak credentials.

Mitigation: Prefer Maton OAuth with the operating system credential store, avoid exporting MATON_API_KEY when the CLI can be used, and rotate any key that may have been exposed.

Risk: Hosted functions and triggers can continue running or forwarding data after setup.

Mitigation: Review the function code, trigger source, destination, network policy, and payload fields with the user before deployment; prefer DENY_ALL network policy and remove automation when the task is complete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-tag-manager-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Tag Manager API Overview](https://developers.google.com/tag-platform/tag-manager/api/v2)
- [Tag Manager API Reference](https://developers.google.com/tag-platform/tag-manager/api/reference/rest)
- [Tag Manager Concepts](https://developers.google.com/tag-platform/tag-manager/api/v2/devguide)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, Python, JSON, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and OAuth or API-key authentication; sensitive actions require explicit user confirmation.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
