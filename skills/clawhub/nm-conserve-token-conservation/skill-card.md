## Description:

Enforces token quota management at session start with conservation and compression checks before large context loads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to keep sessions within token budgets by planning reads, summarizing context, checking delegation options, and logging conservation decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may suggest external delegation for compute-intensive work, which can expose private context if used carelessly.

Mitigation: Review delegation suggestions before sending private context to a separate tool.

Risk: The skill may recommend compaction or a new session, which can affect continuity if important context has not been summarized.

Mitigation: Confirm the current workflow state and summarize critical results before compacting or starting a new session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-token-conservation)
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/conserve)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with concise checklists and command references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a short explanation of token-saving steps, delegated tasks, remaining runway, next actions, and reset or compaction recommendations when useful.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
