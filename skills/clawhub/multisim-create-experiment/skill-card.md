## Description:

Creates safe, reproducible Multisim circuit experiments from engineering requirements and checks theoretical results against simulation evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yxy050208](https://clawhub.ai/user/yxy050208)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create Multisim circuit schematics, simulations, and experiment reports from explicit requirements while preserving review gates for design options, components, netlists, simulation plans, and exported artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can write approved project outputs and run circuit simulations through Multisim MCP.

Mitigation: Require explicit user approval before schematic generation, simulation, export, or handoff confirmation; review output directories and exported artifacts.

Risk: Circuit claims may be overstated if theory, measurement data, or approval provenance are incomplete.

Mitigation: Mark unsupported metrics as unverified and compare approval provenance, netlist, simulation plan, and experiment summaries before declaring PASS.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Files]

**Output Format:** [Markdown status and result summaries with optional shell commands and exported experiment artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final responses include circuit assumptions, netlist and analysis summary, key measurements, PASS/FAIL/unverified conclusions, and artifact lists.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
