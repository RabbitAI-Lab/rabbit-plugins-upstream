## Description:

Kintone (kintone.com) supports Kintone requests for searching and reading data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live Kintone connector schemas and run read-focused Kintone user, department, group, and service lookup actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses OOMOL as the connector layer for Kintone and can read Kintone user, group, department, and service data through the connected account.

Mitigation: Install and use it only when that connector layer and read access are acceptable for the workspace.

Risk: First-time setup includes pipe-to-shell installer commands.

Mitigation: Use an official verified install path or inspect the installer before running it.

Risk: The skill description is broad even though this release exposes read-focused actions.

Mitigation: Treat the release as read-focused and require explicit approval before any future state-changing Kintone action.

## Reference(s):

- [ClawHub Kintone Skill](https://clawhub.ai/oomol/skills/oo-kintone)
- [Kintone homepage](https://www.kintone.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON connector responses from Kintone actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
