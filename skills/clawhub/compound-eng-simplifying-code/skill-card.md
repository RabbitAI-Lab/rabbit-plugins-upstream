## Description:

Simplifies, polishes, and declutters code without changing behavior for code cleanup, refactoring, dead-code removal, and readability improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to simplify requested code while preserving behavior, interfaces, side effects, and domain intent. It guides agents through scoped cleanup, refactoring, AI-generated clutter removal, verification, and concise reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to edit or delete code during simplification, which may accidentally change behavior.

Mitigation: Use it in a version-controlled workspace and review diffs and test results before accepting changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-simplifying-code)
- [Simplification patterns](artifact/references/simplification-patterns.md)
- [Orchestrated simplification](artifact/references/orchestrated-simplification.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown summary plus code edits and inline verification commands when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scope touched, key simplifications, verification results, and residual risks after changes.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
