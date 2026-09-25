## Description:

Reviews Java code changes and produces structured review reports with issue findings and repair suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review Java diffs or source files, identify quality and security issues, and generate Markdown or HTML review reports with suggested fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command execution and write access that are broader than a Java code review report generator needs.

Mitigation: Install and run it only in trusted repositories, supervise command execution, and restrict use to explicit review or report-generation tasks.

Risk: Generated review reports and repair suggestions may be incorrect, incomplete, or unsafe to apply directly.

Mitigation: Require developer review before applying suggested code changes or using the report as a release gate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/java-code-reviewer)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, guidance]

**Output Format:** [Markdown by default, with optional HTML when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include issue summaries, severity-ordered findings, code-focused fix suggestions, and optional consistency checks against supplied requirements or design documents.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
