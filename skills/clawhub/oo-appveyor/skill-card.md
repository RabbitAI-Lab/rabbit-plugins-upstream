## Description:

Enables an agent to inspect AppVeyor connector schemas and run read-only AppVeyor actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent read AppVeyor projects, build artifacts, environments, roles, and users through an OOMOL-connected AppVeyor account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Review the installation source before use and prefer a verified or manually reviewed oo CLI installation path.

Risk: AppVeyor metadata and artifact information may pass through a third-party OOMOL connector.

Mitigation: Use the skill only when that data flow is acceptable and connect AppVeyor with a least-privilege API key.

## Reference(s):

- [ClawHub AppVeyor Skill](https://clawhub.ai/oomol/skills/oo-appveyor)
- [AppVeyor Homepage](https://www.appveyor.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent commands call the oo CLI and may return connector JSON responses.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
