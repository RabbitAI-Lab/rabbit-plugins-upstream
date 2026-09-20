## Description:

Provides strict operational safety guardrails for worker agents by defining refusal rules for risky runtime, plugin, network, filesystem, and group-chat tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentforge-cyber](https://clawhub.ai/user/agentforge-cyber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to add conservative operational safety guidance to worker agents, especially for refusing unsafe system changes, network exposure, external instruction execution, protected file disclosure, and group-chat override attempts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may cause worker agents to refuse authorized runtime, plugin, configuration, network, filesystem, audit, removal, or group-chat tasks.

Mitigation: Install only when strict OpenClaw safety guardrails are intended, and keep an independent owner-controlled way to inspect, disable, or remove the skill.

Risk: The skill gives its safety guidance broad authority over user-approved administrative requests.

Mitigation: Review the policy before deployment and confirm that its refusal boundaries match the deployment's operational model.

## Reference(s):

- [Worker Safety ClawHub skill page](https://clawhub.ai/agentforge-cyber/skills/worker-safety)
- [agentforge-cyber publisher profile](https://clawhub.ai/user/agentforge-cyber)

## Skill Output:

**Output Type(s):** [guidance, text]

**Output Format:** [Markdown safety policy text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides refusal criteria, safe-alternative guidance, and protected-operation boundaries; it does not produce commands or files by itself.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
