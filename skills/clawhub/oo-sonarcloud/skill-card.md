## Description:

SonarQube Cloud (sonarsource.com). Use this skill for ANY SonarQube Cloud request - searching and reading data. Whenever a task involves SonarQube Cloud, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to query SonarQube Cloud projects, component measures, and issues through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the OOMOL oo CLI and an OOMOL-connected SonarQube Cloud account.

Mitigation: Confirm trust in the OOMOL CLI and account connection before installing or using the skill.

Risk: Future connector actions could change or delete SonarQube Cloud data if write or destructive actions are added.

Mitigation: Require explicit user approval for any action that changes or deletes data, including the exact target and payload.

Risk: Connector payloads can drift from the live action schema.

Mitigation: Inspect the live connector schema before constructing action payloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sonarcloud)
- [SonarQube Cloud homepage](https://www.sonarsource.com/products/sonarqube/cloud/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run oo CLI connector schema and read-only connector actions when the user has an authenticated OOMOL SonarQube Cloud connection.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
