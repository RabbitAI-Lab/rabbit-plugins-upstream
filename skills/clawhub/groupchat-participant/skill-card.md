## Description:

Reply once per round and never create participant loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chizumystic](https://clawhub.ai/user/chizumystic)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to participate in host-mediated group chats, reply once per round, and avoid duplicate responses or participant loops. It also guides agents on when to join, leave, or check participation status with the host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to send group chat replies and join, leave, or status commands to a host session.

Mitigation: Enable it only where host-mediated multi-agent chat is expected, and rely on the one-reply-per-round and host-only routing constraints described by the skill.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Markdown guidance with inline command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be concise, routed through the host, and limited to one reply per group chat round.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
