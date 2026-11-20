## Description:

Hand context to a new receive-only chat when explicitly invoked, or send relevant context to an already authorized subtask through its existing channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-en](https://clawhub.ai/user/peterflow-en)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to hand current task context to a fresh chat or synchronize an already authorized subtask. It helps the recipient resume from the correct scope, workspace state, and interruption point.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A handoff could blur what the recipient is authorized to do.

Mitigation: State the recipient's role, current authority, scope, and stopping condition; separate future work from present authorization.

Risk: A handoff could expose credentials or unrelated conversation details.

Mitigation: Exclude credentials and unrelated history, and share only context needed for the assigned task.

Risk: A recipient could lack access to key files or miss the interruption point.

Mitigation: Provide absolute paths and current work status, include essential text inline when files are inaccessible, and verify receipt.

## Reference(s):

- [Explicit handoff to a new chat](references/new-chat.md)
- [Sync an assigned subtask](references/subagent.md)
- [Context handoff on ClawHub](https://clawhub.ai/peterflow-en/skills/context-handoff)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise Markdown handoff packet or inline context message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to the recipient role and authorized task; may include workspace paths, progress, and the exact interruption point.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
