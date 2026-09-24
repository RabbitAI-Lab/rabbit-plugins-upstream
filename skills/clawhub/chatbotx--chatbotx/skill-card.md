## Description:

Manage contacts, conversations, broadcasts, flows, sequences, appointments, minigames, and every other ChatbotX workspace resource from the command line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chatbotx](https://clawhub.ai/user/chatbotx)

### License/Terms of Use:

MIT-0

## Use Case:

Agents, developers, and workspace operators use this skill to inspect and manage ChatbotX workspaces from the command line, including customer contacts, conversations, broadcasts, flows, analytics, appointments, and integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send messages, change broadcasts or flows, delete data, and affect customer records through the user's ChatbotX token.

Mitigation: Confirm recipients, filters, payloads, schedules, and workspace scope before mutating commands; verify every write with a matching get or list command.

Risk: ChatbotX credentials can grant broad workspace access and saved CLI config may store credentials on disk.

Mitigation: Prefer environment variables or tightly scoped API keys, avoid exposing saved config or unredacted contact data, and rotate credentials if they are disclosed.

Risk: Some generated CLI commands may collide or silently do nothing while exiting successfully.

Mitigation: Check command help and verify resulting state after each write; use documented alternative commands or the REST API when a collision blocks a CLI action.

## Reference(s):

- [ChatbotX ClawHub Skill Page](https://clawhub.ai/chatbotx/skills/chatbotx)
- [ChatbotX API Endpoint](https://app.chatbotx.io/api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI commands operate on a live ChatbotX workspace and commonly return JSON responses.]

## Skill Version(s):

1.1.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
