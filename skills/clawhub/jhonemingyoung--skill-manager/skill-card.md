## Description:

Skill Manager scans installed Plugins and Skills, analyzes dependencies and risks, assesses task complexity, and recommends execution paths or external skills for agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jhonemingyoung](https://clawhub.ai/user/jhonemingyoung)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inventory installed skills, compare existing skills, built-in tools, and new scripts for a task, and produce a report for user-selected execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads installed skill directories and produces inventory reports that may expose local skill names, descriptions, dependencies, or risk notes.

Mitigation: Run it only in approved environments and review generated reports before sharing them outside the workspace.

Risk: External search recommendations may use sensitive task descriptions or point to unreviewed third-party skills and tools.

Mitigation: Avoid sensitive task text unless external search is explicitly approved, and review recommended sources before installation or use.

Risk: The artifact recommends an unpinned npx search command as one possible discovery path.

Mitigation: Verify the package source and version before running any suggested npx command.

Risk: Risk ratings and cost estimates are heuristic and can be over-trusted.

Mitigation: Treat the report as advisory and perform manual review for security, dependencies, and execution choices.

## Reference(s):

- [Risk Assessment Reference Guide](references/risk_assessment.md)
- [ClawHub Skill Page](https://clawhub.ai/jhonemingyoung/skills/skill-manager)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports, JSON skill inventories, and shell command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes heuristic risk, token cost, and execution time estimates; user confirmation is expected before acting on a selected path.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
