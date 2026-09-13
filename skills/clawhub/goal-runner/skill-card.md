## Description:

Goal Runner orchestrates roadmap or checkbox task lists one item at a time, delegating coding, review, and regression testing to sub-agents before marking tasks complete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to work through roadmap or task files unattended while keeping one task in flight, requiring observed evidence before task close-out, and respecting explicit authorization for git actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unattended task automation can take actions the user did not intend if the goal text is ambiguous.

Mitigation: Review the goal text before starting, especially whether commits or pushes are authorized.

Risk: Local run ledgers and task reports may retain sensitive implementation details from the repository.

Mitigation: Clean up .claude/goal-runner after use when repository details should not persist.

Risk: Optional git actions can publish or preserve changes if explicitly authorized in the goal text.

Mitigation: Require explicit commit or push authorization and keep one verified task per commit when those actions are requested.

## Reference(s):

- [Goal Runner Skill Page](https://clawhub.ai/dennisrongo/skills/goal-runner)
- [Sub-agent briefs](references/agent-briefs.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with sub-agent briefs, command summaries, task-file updates, and optional git instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update roadmap checkboxes and local run ledgers; commits or pushes occur only when the goal text explicitly authorizes them.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
