## Description:

Fixes SonarQube code quality issues across languages by analyzing reported issues, generating targeted code and test changes, and running SonarQube-aware validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to resolve SonarQube-reported issues in an existing project, add or update tests, and prepare review notes for the fixes. It is intended for SonarQube-driven remediation, not general code review or unrelated static analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make broad automatic changes to source, tests, .gitignore, generated review files, and analysis configuration.

Mitigation: Review the full diff before accepting changes, keep fixes scoped to the SonarQube issues being remediated, and require project tests and lint checks to pass.

Risk: The security evidence flags insecure local scan behavior around SonarQube token handling.

Mitigation: Avoid the local scan helper unless token handling is fixed; use configured environment variables without printing or inspecting token values.

Risk: Validation may invoke external project tools or unpinned npx commands.

Mitigation: Prefer locally installed or explicitly pinned tool versions and review commands before execution in sensitive repositories.

Risk: The artifact instructs removal of some SonarQube scanner configuration files.

Mitigation: Disable or override configuration deletion unless the project owner confirms those files are disposable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/sonarqube-review)
- [Source repository](https://github.com/afonsoft/skills)
- [SonarScanner documentation](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/)
- [Stack detection helper](references/detect-stack.sh)
- [SonarQube issue download helper](references/download-issues.sh)
- [Local SonarQube scan helper](references/sonar-local-scan.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code changes, generated review files, and configuration edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create .sonar_devin_auto_fix review artifacts, update .gitignore, and modify source or test files during remediation.]

## Skill Version(s):

1.0.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
