## Description:

Reviews Java code changes or source files and produces a structured review report covering style, exception handling, security, performance, design, and resource management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxweven](https://clawhub.ai/user/wxweven)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review Java pull requests, git diffs, or source files and receive prioritized findings with severity, explanations, and before-and-after Java fix examples. Optional requirements or design documents can be used for consistency checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional HTML reports can expose unescaped reviewed code, filenames, issue text, or consistency-check content when opened or hosted.

Mitigation: Prefer Markdown for untrusted inputs, or escape all dynamic report fields before producing or publishing HTML.

## Reference(s):

- [Java Code Review Rules](references/rules.md)
- [Markdown Report Template](assets/report-template.md)
- [HTML Report Template](assets/report-template.html)
- [Java Code Reviewer on ClawHub](https://clawhub.ai/wxweven/skills/java-code-reviewer)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, guidance]

**Output Format:** [Markdown by default, with optional HTML report output and Java code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include issue counts, severity ordering, rule references, repair guidance, before-and-after Java snippets, and optional consistency checks.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
