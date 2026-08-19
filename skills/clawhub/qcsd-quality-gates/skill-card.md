## Description:

Provides quality-gate checklists and auto-healing guidance for AI-assisted personal software development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-acheng](https://clawhub.ai/user/ai-acheng)

### License/Terms of Use:

MIT

## Use Case:

Developers and individual builders use this skill to review AI-assisted projects across requirements, architecture, coding, dependencies, environment setup, and delivery readiness. It also guides repair of common dependency, import-path, syntax, startup, configuration, and missing-file issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may aggressively enforce quality gates and change project files, dependencies, imports, syntax, configuration examples, or missing files.

Mitigation: Use it under version control and require explicit confirmation or a dry run before accepting automatic repairs.

Risk: Automatic repairs may introduce incorrect changes when project boundaries or user intent are unclear.

Mitigation: Review proposed changes and test the project before merging or releasing.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/AI-aCheng/qcsd-quality-gates)
- [ClawHub skill page](https://clawhub.ai/ai-acheng/skills/qcsd-quality-gates)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured check results and proposed or applied code and configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report pass/fail checks, issues found, fixes applied, and AI-generated-code review items.]

## Skill Version(s):

1.1.1 (source: ClawHub release evidence; artifact package metadata lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
