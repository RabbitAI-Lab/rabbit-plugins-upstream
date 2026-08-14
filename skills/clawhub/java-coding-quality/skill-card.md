## Description:

Java Coding Quality helps agents run PMD 7, SpotBugs, and FindSecBugs quality gates for Java and Spring Boot code, fix findings by severity, and report remaining risks before delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baixuanzhu](https://clawhub.ai/user/baixuanzhu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill after Java or Spring Boot implementation, refactoring, review, or pre-submit work to run static analysis, prioritize Blocker and Critical findings, and guide fixes until the gate can pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create a local .qualitygate directory and change project files while setting up or running Java quality gates.

Mitigation: Review generated files and code changes before accepting them, and keep the default wrapper setup separate from project build files unless persistence is explicitly approved.

Risk: Persistent Maven or Gradle quality-gate configuration can affect future local and CI builds.

Mitigation: Require user approval before adding persistent PMD or SpotBugs configuration, then review the exact build-file changes before committing them.

Risk: Static-analysis output can include false positives or findings that need project-specific context.

Mitigation: Require documented justification and user confirmation for suppressions, and do not suppress security findings without user review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/baixuanzhu/skills/java-coding-quality)
- [Publisher profile](https://clawhub.ai/user/baixuanzhu)
- [Setup and quality gate configuration](references/01-setup.md)
- [PMD 7 ruleset](references/02-pmd-rules.md)
- [SpotBugs and FindSecBugs security scanning](references/03-spotbugs-security.md)
- [Fix workflow and severity mapping](references/04-fix-workflow.md)
- [Bundled PMD 7 ruleset XML](assets/pmd7-ruleset.xml)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code changes, configuration snippets, and scan summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a local .qualitygate folder and may propose persistent Maven or Gradle quality-gate configuration only after user consent.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
