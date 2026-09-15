## Description:

SonarQube Cloud helps agents search and read SonarQube Cloud project, measure, and issue data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to inspect SonarQube Cloud action schemas, list projects, retrieve component code-health measures, and search code issues without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded scripts directly.

Mitigation: Review the oo CLI installer before running it, and prefer an official package manager, signed release, or checksum-verified download.

Risk: The skill depends on OOMOL-connected SonarQube Cloud credentials.

Mitigation: Confirm the account connection and credential handling model are acceptable before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sonarcloud)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [SonarQube Cloud product page](https://www.sonarsource.com/products/sonarqube/cloud/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return oo CLI JSON responses containing connector data and execution metadata.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
