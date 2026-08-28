## Description:

Jira API工具 helps agents use managed OAuth to search Jira issues with JQL, create and update issues, and manage boards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation engineers, and teams use this skill to connect agents to Jira through the Maton-managed API for issue search, issue updates, project workflows, and board operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact Jira changes such as creating, updating, transitioning, closing, deleting, or bulk-modifying issues.

Mitigation: Require explicit user confirmation before any write, transition, delete, close, or bulk Jira operation.

Risk: Jira and Maton credentials may grant broad access to project data and workflow actions.

Mitigation: Use least-privilege Jira and Maton tokens, avoid sharing secrets in prompts, and keep credentials in environment variables or approved secret storage.

Risk: The artifact describes broad command-execution and file-handling capabilities beyond the core Jira integration.

Mitigation: Limit use to the Jira integration workflow and review generated shell commands or file operations before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/jira-api)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Maton connections API](https://api.maton.ai/connections)
- [Maton Jira accessible resources API](https://api.maton.ai/jira/oauth/token/accessible-resources)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Jira API request examples, JQL guidance, setup steps, and troubleshooting notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
