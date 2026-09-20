## Description:

Use AgentOS as the operator control plane above OpenClaw for starting, inspecting, and diagnosing a digital workforce.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sapienx](https://clawhub.ai/user/sapienx)

### License/Terms of Use:

MIT-0

## Use Case:

Operators and developers use this skill to start, inspect, and diagnose AgentOS as a human-controlled Mission Control layer for OpenClaw workspaces and digital workers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AgentOS is intended to inspect and operate OpenClaw agent runtime state.

Mitigation: Install or run the referenced AgentOS runtime and OpenClaw plugin only after confirming trust in the @sapienx publisher.

Risk: Missing, degraded, unavailable, or unknown OpenClaw state can be mistaken for a healthy runtime.

Mitigation: Use the native OpenClaw AgentOS commands and doctor checks, and report unsupported or degraded behavior clearly.

## Reference(s):

- [AgentOS skill on ClawHub](https://clawhub.ai/sapienx/skills/agentos)
- [AgentOS website](https://agentos.sapienx.app/)
- [OpenClaw AgentOS plugin on ClawHub](https://clawhub.ai/plugins/@sapienx/openclaw-agentos)
- [AgentOS source repository](https://github.com/SapienXai/AgentOS)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operator guide; the skill text does not execute code automatically.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
