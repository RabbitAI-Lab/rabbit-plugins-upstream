## Description:

You.com skill for searching, reading webpages, checking account balance, and generating cited research or finance answers through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route You.com search, webpage retrieval, account balance lookup, and cited research workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes commands that download and execute remote installer scripts.

Mitigation: Download and inspect the installer before execution, verify an official checksum or signature if available, and avoid running it from an elevated shell.

Risk: You.com requests are routed through OOMOL as an intermediary account connection.

Mitigation: Use the skill only when that intermediary model is acceptable, and review the connected account scope before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-you)
- [You.com homepage](https://you.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, text, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when commands run successfully.]

## Skill Version(s):

1.0.4 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
