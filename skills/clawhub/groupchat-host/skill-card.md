## Description:

Prevent accidental participant pings and endless groupchat loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chizumystic](https://clawhub.ai/user/chizumystic)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users use this skill to host controlled multi-agent group chats, add or remove participants, and synthesize participant replies into one user-facing response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Informal requests for a roundtable or join/leave statements may engage the group-chat workflow unintentionally.

Mitigation: Use explicit !gc commands when precise participant control is required.

Risk: Forwarding participant replies or host summaries back to other agents could create accidental pings or looping conversations.

Mitigation: Dispatch once per open round, accept at most one reply per participant, close the round, and do not call participant messaging while composing the user-facing reply.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chizumystic/skills/groupchat-host)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and command-style chat instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains bounded per-round participant state and emits one user-facing host response per round.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
