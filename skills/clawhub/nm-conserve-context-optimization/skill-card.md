## Description:

Optimizes context window via MECW principles and memory tiering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to monitor context pressure, choose memory and routing strategies, delegate context-heavy work, and preserve concise findings during long agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File-based checkpoint and memory examples could preserve sensitive data if copied directly into a project workflow.

Mitigation: Keep checkpoint and memory files scoped to the project, avoid secrets, set appropriate permissions, and clean up temporary state when it is no longer needed.

Risk: Over-aggressive context reduction can omit details needed for accurate downstream decisions.

Mitigation: Preserve raw findings files, read summaries first, and reopen detailed evidence selectively before acting on high-severity or ambiguous findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-context-optimization)
- [Context optimization homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve)
- [MECW principles module](artifact/modules/mecw-principles.md)
- [MECW assessment module](artifact/modules/mecw-assessment.md)
- [Subagent coordination module](artifact/modules/subagent-coordination.md)
- [Context waiting module](artifact/modules/context-waiting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes context-pressure thresholds, memory tiering conventions, routing guidance, and subagent coordination patterns.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
