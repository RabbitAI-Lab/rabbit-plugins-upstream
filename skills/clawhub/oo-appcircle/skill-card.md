## Description:

Appcircle (appcircle.io). Use this skill for ANY Appcircle request -- searching and reading data. Whenever a task involves Appcircle, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Appcircle organizations and list Appcircle Build, Testing Distribution, and Enterprise App Store profiles through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to pipe remote installer scripts directly into Bash or PowerShell.

Mitigation: Review the OOMOL oo CLI installer first and prefer a pinned, signed, or checksum-verified installation path.

Risk: The skill depends on an OOMOL-connected account and durable local CLI authentication.

Mitigation: Use the connected account with the least Appcircle access needed and reconnect only when an authentication, scope, or credential error occurs.

Risk: Connector command inputs may drift from the documented examples.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing each payload.

## Reference(s):

- [Appcircle ClawHub listing](https://clawhub.ai/oomol/skills/oo-appcircle)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Appcircle homepage](https://appcircle.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running Appcircle read actions.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
