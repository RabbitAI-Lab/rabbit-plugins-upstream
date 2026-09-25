## Description:

Sina Finance ZYHub lets agents search and read Sina Finance market, company, fund, and news data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Sina Finance ZYHub action schemas and retrieve market quotes, financial statements, fund data, company information, and Sina Finance news through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback includes remote shell installer commands that may run without independent verification.

Mitigation: Prefer the official installer page or verify installer source, version, and integrity before installation; do not let an agent run remote shell installers automatically.

Risk: ZYHub queries run through the user's OOMOL-connected account.

Mitigation: Use the skill only when the user expects requests to go through their OOMOL account and connected Sina Finance ZYHub credentials.

## Reference(s):

- [Sina Finance ZYHub homepage](https://zyhub.finance.sina.cn/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zyhub)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs can return JSON objects with data and meta.executionId when invoked with --json.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
