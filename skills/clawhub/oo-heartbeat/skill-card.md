## Description:

Heartbeat (heartbeat.chat). Use this skill for ANY Heartbeat request - searching and reading data. Whenever a task involves Heartbeat, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search and read Heartbeat community data through an OOMOL-connected account, including users, access groups, channels, and events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to run remote install scripts directly in a shell.

Mitigation: Install only after reviewing or verifying official OOMOL installation steps; avoid blindly running curl-to-bash or PowerShell iex installers.

Risk: The skill can access Heartbeat community data through the connected OOMOL account.

Mitigation: Use only the listed read-only Heartbeat actions and confirm account connection, scopes, and billing state before retrying failed connector calls.

## Reference(s):

- [ClawHub Heartbeat skill](https://clawhub.ai/oomol/skills/oo-heartbeat)
- [Heartbeat homepage](https://www.heartbeat.chat)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions and returns read-only Heartbeat connector results when invoked.]

## Skill Version(s):

1.0.2 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
