## Description:

Use when analyzing SonarQube issues and turning them into SPEC SDDs for TDD implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to analyze unresolved SonarQube issues, classify findings, create approved SPEC SDDs for TDD remediation, and hand off implementation across supported stacks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can download SonarQube data and use SonarQube tokens.

Mitigation: Use scoped tokens, avoid exposing token values, and run only in workspaces where SonarQube access is approved.

Risk: The skill can write project files and invoke another skill to modify code.

Mitigation: Require human review of generated SPEC SDDs and approve repository writes before implementation proceeds.

Risk: Validation and formatter commands can execute project toolchains, including npm scripts.

Mitigation: Run validation only with trusted lockfiles and pinned dependencies, and review commands before execution.

Risk: Scanner-configuration deletion guidance may remove project configuration that teams still need.

Mitigation: Review any scanner-configuration removal instruction before applying it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/sonarqube-autofix)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Skill metadata URL](https://github.com/afonsoft/skills)
- [SonarScanner documentation](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/)
- [SPEC SDD template](artifact/references/spec-sdd-template.md)
- [Stack detection script](artifact/references/detect-stack.sh)
- [SonarQube issue download script](artifact/references/download-issues.sh)
- [Local SonarQube scan script](artifact/references/sonar-local-scan.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown SPEC SDD files, review notes, metrics summaries, and shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write repository-local planning and review files and may invoke validation or formatting tools when used by an agent.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter lists 2.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
