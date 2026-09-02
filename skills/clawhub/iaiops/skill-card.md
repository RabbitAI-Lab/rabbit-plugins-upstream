## Description:

Vendor-neutral, governed industrial/OT data tap and troubleshooting router for selecting the appropriate iaiops edition skill and MCP profile across PLC, controller, machine-tool, IIoT broker, building, fab, and related OT scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, OT engineers, and site reliability teams use this skill to route industrial protocol, PLC/SCADA/HMI/historian/CNC, OEE, downtime, and OT asset inventory tasks to the correct iaiops edition skill and MCP profile. It is intended for read-first troubleshooting and governed change workflows where any real control-system write requires dry-run, authorization, and approval controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the general iaiops server profile for substations or energy protocols could route work to the wrong package.

Mitigation: Confirm the needed edition before installation and use the iaiops-energy package for IEC-104, DNP3, IEC 61850, substation, or utility SCADA tasks.

Risk: Real OT writes can affect production control systems.

Mitigation: Proceed only with documented read-first checks, dry-run behavior, named approval, double confirmation, authorization, and change-management controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes users to edition skills and MCP profile selections; the router itself does not expose a tool table.]

## Skill Version(s):

0.26.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
