## Description:

Use when analyzing SonarQube issues and turning them into SPEC SDDs for TDD implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to triage unresolved SonarQube findings, convert them into approved SPEC SDDs, and hand fixes to a TDD implementation workflow across common application stacks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can rewrite repositories, change formatting, create tracking files, update .gitignore, and alter or remove SonarQube-related configuration.

Mitigation: Review planned changes before applying them and require human approval before deleting scanner or CI-related configuration.

Risk: The workflow can execute broad build, test, lint, formatter, scanner, and npx validation commands.

Mitigation: Run it in a controlled workspace with locked local dependencies and avoid unpinned npx validation scripts unless dependency versions are already pinned.

Risk: SonarQube tokens may be sent to configured URLs.

Mitigation: Use least-privilege SonarQube tokens, prefer HTTPS-only SonarQube URLs, and avoid printing or inspecting token values.

## Reference(s):

- [SonarScanner documentation](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/)
- [Project repository](https://github.com/afonsoft/skills)
- [SPEC SDD template](references/spec-sdd-template.md)
- [SonarQube local scan script](references/sonar-local-scan.sh)
- [Download issues script](references/download-issues.sh)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown files and shell commands with code and configuration changes delegated to the TDD execution workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates SonarQube issue tracking artifacts and approved SPEC SDDs before implementation handoff.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
