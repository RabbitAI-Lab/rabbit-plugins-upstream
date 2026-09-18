## Description:

Vendor-neutral, governed industrial/OT data tap and intelligent troubleshooting skill that routes industrial protocol, PLC, SCADA, HMI, historian, CNC, RTU, IED, OEE, downtime root-cause, and OT asset inventory tasks to the appropriate iaiops MCP profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to identify industrial and building automation tasks, choose the matching iaiops edition skill and MCP profile, and follow read-first troubleshooting or onboarding workflows. It is intended for governed OT diagnostics, routing, setup guidance, and carefully controlled write workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Operators may misread or miss important Chinese operational instructions.

Mitigation: Install and use the skill only with operators who can understand and review those instructions.

Risk: The skill points users to an external iaiops-energy package for energy protocols.

Mitigation: Pin or otherwise verify the external package before installation.

Risk: Industrial and OT write actions can affect real equipment or production systems.

Mitigation: Use least-privileged hosts and keep real OT writes behind the documented dry-run, approval, and change-management controls.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes users to specific iaiops edition skills and MCP profiles; emphasizes read-first operation, dry-run behavior, approval controls, and human-supplied site semantics.]

## Skill Version(s):

0.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
