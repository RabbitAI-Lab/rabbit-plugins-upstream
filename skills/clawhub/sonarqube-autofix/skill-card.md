## Description:

Use when analyzing SonarQube issues and turning them into SPEC SDDs for TDD implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to fetch and classify SonarQube findings, generate approved SPEC SDDs for fixes, and hand the work to /execute-specs with stack-specific validation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can drive broad repository changes after SonarQube issue analysis.

Mitigation: Install and run it only in a disposable branch or sandboxed workspace, then review the generated SPECs and resulting changes before merging.

Risk: The workflow uses SonarQube URLs and authentication tokens.

Mitigation: Use a least-privilege read-only token, require a trusted HTTPS SonarQube URL, and never print or inspect token values.

Risk: Generated SPECs may be handed off to /execute-specs for implementation.

Mitigation: Review each generated SPEC before any handoff and confirm it stays scoped to the downloaded SonarQube issues.

Risk: The artifact instructs cleanup of SonarQube scanner configuration that may be required by a project.

Mitigation: Remove or override scanner-configuration deletion instructions when those files are intentionally part of the project.

Risk: Included JavaScript and Angular validation scripts may invoke npx commands.

Mitigation: Run those scripts only after pinning npx package versions or replacing them with local lockfile-resolved tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/sonarqube-autofix)
- [Publisher metadata URL](https://github.com/afonsoft/skills)
- [SonarScanner documentation](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/)
- [SPEC SDD template](references/spec-sdd-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown SPEC SDD files, review notes, HTML metrics, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project-local artifacts under .sonar_devin_auto_fix/ and .specs/ and relies on configured SonarQube environment variables.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
