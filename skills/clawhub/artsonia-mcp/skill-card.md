## Description:

Access Artsonia student-art portfolios, comments, and fans via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to an Artsonia parent or fan account, review linked student artwork, inspect portfolios, manage comments and fans, download artwork, and update notification preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup may run mutable third-party MCP code while handling Artsonia account credentials and sensitive student-art data.

Mitigation: Use a pinned and audited package version or commit before installation, and review the skill before connecting real account credentials.

Risk: Reusable Artsonia passwords and session cookies can be exposed if stored in shared project files or an unprotected session cache.

Mitigation: Store credentials only in protected local configuration, avoid shared project files, and disable or protect the session cache on shared machines.

Risk: Downloads, comments, fan invites, and notification changes can expose data or modify an Artsonia account.

Mitigation: Require explicit user confirmation before running download, comment, fan invite, or notification update actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [npm package](https://www.npmjs.com/package/artsonia-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool recommendations, setup snippets, and confirmation-oriented guidance for account actions.]

## Skill Version(s):

0.12.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
