## Description:

Create a durable, self-contained state package so a fresh agent, session, or different harness can resume non-trivial work without the original chat history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to write a local CHECKPOINT.md that captures enough project state for a fresh agent, session, or different harness to resume non-trivial work. It is suited for long-running tasks, context resets, handoffs, and paused work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generated CHECKPOINT.md may include private code details, customer data, credentials, or confidential decisions if the workspace state contains them.

Mitigation: Review CHECKPOINT.md before sharing it outside the workspace and remove sensitive or confidential information.

Risk: A vague or incomplete checkpoint can cause a receiving agent to resume from incorrect assumptions.

Mitigation: Apply the receiver test from the skill and include concrete goals, sources, decisions, evidence, known issues, and the next action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/raguets/skills/checkpoint)
- [Publisher profile](https://clawhub.ai/user/raguets)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically writes or updates CHECKPOINT.md in the working directory unless the user specifies another location.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
