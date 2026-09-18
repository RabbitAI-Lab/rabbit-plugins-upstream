## Description:

SonarQube Cloud (sonarsource.com). Use this skill for ANY SonarQube Cloud request - searching and reading data. Whenever a task involves SonarQube Cloud, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect SonarQube Cloud action schemas, list projects, retrieve component measures, and search code issues through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup fallback can run remote installer scripts directly in a shell.

Mitigation: Review setup before installing, prefer a verified or pinned oo CLI source, and avoid curl-to-bash or PowerShell download-to-execute commands unless the installer path is trusted.

Risk: The release has a suspicious security verdict due to installer guidance even though the SonarQube Cloud actions are read-oriented.

Mitigation: Use the installed connector for read actions only unless future action schemas explicitly show write or destructive behavior and the user confirms the payload and effect.

## Reference(s):

- [SonarQube Cloud homepage](https://www.sonarsource.com/products/sonarqube/cloud/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sonarcloud)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo CLI connector schemas before submitting SonarQube Cloud read actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
