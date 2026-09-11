## Description:

Analyzes SonarQube issues, classifies them by issue type, generates approved SPEC SDDs for proposed fixes, and hands implementation to execute-tdd-spec.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn unresolved SonarQube findings into reviewable SPEC SDDs, validation steps, and implementation handoffs for code-quality, reliability, and security fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can download SonarQube issues using configured tokens.

Mitigation: Use HTTPS SonarQube URLs with least-privilege tokens, and do not read, print, or inspect token values.

Risk: The skill can create repository files, run build, lint, and test tooling, and delegate code changes.

Mitigation: Review generated SPECs and require explicit approval before execute-tdd-spec runs; preserve existing CI and scanner configuration unless removal is specifically approved.

Risk: Some validation flows may rely on package-runner commands such as npx.

Mitigation: Avoid unpinned npx validation scripts or run them in a constrained environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/sonarqube-autofix)
- [Publisher source URL](https://github.com/afonsoft/skills)
- [SonarScanner documentation](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/)
- [SPEC SDD template](references/spec-sdd-template.md)
- [Stack detection script](references/detect-stack.sh)
- [SonarQube issue download script](references/download-issues.sh)
- [Local SonarQube scan script](references/sonar-local-scan.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown files, shell commands, configuration snippets, and HTML review metrics.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates SPEC SDDs, a SonarQube todo board, review notes, and a metrics dashboard; implementation is handed off to execute-tdd-spec.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
