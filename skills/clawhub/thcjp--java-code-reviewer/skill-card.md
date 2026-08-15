## Description:

Java代码 helps agents review Java code changes and generate structured review reports with severity-ranked findings and repair suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review git diffs or Java source files, identify quality and security issues, and produce Markdown or HTML reports with actionable fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, command execution, report-writing, external API, and generic API key handling that are not clearly scoped to Java code review.

Mitigation: Review the skill before installing, use it only in repositories where that access is acceptable, and avoid providing a generic API_KEY unless the provider, purpose, transmitted data, and permissions are clearly documented.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/java-code-reviewer)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown or HTML review report with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include severity-ranked findings, issue counts, repair suggestions, and consistency checks when requirements or design documents are provided.]

## Skill Version(s):

1.0.1 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
