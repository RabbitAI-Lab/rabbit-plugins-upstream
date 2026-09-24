## Description:

A Markdown-only agent skill that frames a review workflow for checking AI-generated artifacts against policies and producing compliance and risk reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators can use this skill as a review prompt for AI-generated code, configuration, or other artifacts before further use. Because the server security evidence says the artifact does not implement its advertised blocking, ML, authentication, or policy synchronization claims, treat its results as review guidance rather than an enforceable control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact asks for broad read, exec, and write tool authority while providing only Markdown instructions.

Mitigation: Install with the minimum tool access needed for review, and require human approval before any command execution or file writes.

Risk: The artifact advertises blocking, ML detection, API authentication, and policy synchronization without concrete implementation details.

Mitigation: Use the skill only as advisory review guidance unless the publisher adds verifiable implementation details and clear operational limits.

Risk: The release license evidence and artifact frontmatter disagree.

Mitigation: Confirm the published license terms before redistribution or production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/moltblock)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with example JSON reports and optional shell configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The artifact describes review reports with grades, scores, findings, and improvement suggestions.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 0.11.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
