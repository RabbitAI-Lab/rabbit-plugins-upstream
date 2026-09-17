## Description:

Emelia (emelia.io). Use this skill for ANY Emelia request - searching and reading data. Whenever a task involves Emelia, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Emelia connector schemas and read campaign, contact, email provider, webhook, and activity data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote shell and PowerShell installer commands with broad local execution authority.

Mitigation: Review setup instructions first; prefer a pinned, verified oo CLI release or package manager, and run remote installer scripts only when the OOMOL endpoint is trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-emelia)
- [Emelia Homepage](https://emelia.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before running Emelia read actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
