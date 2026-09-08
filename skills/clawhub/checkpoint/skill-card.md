## Description:

Part of the Overpowered skill suite, Checkpoint helps an agent create a durable, self-contained state package so work can be resumed by a fresh agent, session, or harness without the original chat history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill during long-running work, context resets, handoffs, or pauses to create a local checkpoint that captures the goal, current state, authoritative inputs, decisions, evidence, open issues, and next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generated checkpoint may include confidential project details, private paths, source references, or unresolved security notes.

Mitigation: Review CHECKPOINT.md before sharing or committing it.

Risk: An incomplete checkpoint can cause a fresh agent or session to resume from vague or incorrect state.

Mitigation: Use the receiver test and include concrete goals, authoritative inputs, decisions, evidence, open issues, and the next action.

## Reference(s):

- [Overpowered suite](https://github.com/raguets/overpowered)
- [Checkpoint skill page](https://clawhub.ai/raguets/skills/checkpoint)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates CHECKPOINT.md in the working directory unless the user specifies another location.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
