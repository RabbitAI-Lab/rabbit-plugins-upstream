## Description:

Helps agents fix SonarQube-reported code quality issues across languages by analyzing issues, generating fixes, adding tests, and running validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to triage and fix SonarQube issues in application repositories, including stack detection, code changes, unit tests, coverage checks, and review documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad authority to change repository code, tests, review files, and configuration.

Mitigation: Run it in a disposable branch or sandbox and review all generated changes before merge.

Risk: SonarQube API calls may send tokens to untrusted or misconfigured SonarQube URLs.

Mitigation: Use narrowly scoped SonarQube tokens and only configure trusted HTTPS SonarQube endpoints.

Risk: Bundled helper scripts can affect the wrong project directory or alter scanner and CI-related configuration.

Mitigation: Verify the target directory before running local scan helpers and require explicit review before deleting or changing existing scanner or CI configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/sonarqube-review)
- [Publisher metadata URL](https://github.com/afonsoft/skills)
- [SonarScanner documentation](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/)
- [Stack detection helper](references/detect-stack.sh)
- [SonarQube issue download helper](references/download-issues.sh)
- [Local SonarQube scan helper](references/sonar-local-scan.sh)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and repository file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create review notes, metrics, issue checklists, tests, and SonarQube-related configuration in the target repository.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
