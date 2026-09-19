## Description:

Drive a desktop application from one plain-language goal, or resolve one intent at a time, without reading the accessibility tree.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to drive desktop applications through `run.mjs` for goal-directed automation or `act.mjs` for one resolved interaction at a time, while keeping large accessibility trees out of the agent context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screen metadata, accessible names or descriptions, field values, window titles, and recent actions may be sent to a remote API during desktop automation.

Mitigation: Use the skill only with trusted companion scripts and agent-desktop binaries, avoid private documents or filled forms when possible, and pass `--no-values` for sensitive workflows.

Risk: Desktop automation can perform hard-to-undo actions if a goal or target is wrong.

Mitigation: Review proposed actions for sensitive workflows and rely on the documented confidence thresholds and destructive-action gates before enabling execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lahfir/skills/jev-desktop)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The described automation scripts emit JSON status objects per turn or per action, including decisions, targets, confidence, gates, notes, and execution status.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
