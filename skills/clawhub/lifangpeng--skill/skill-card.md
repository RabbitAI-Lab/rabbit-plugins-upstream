## Description:

Design TOML steady-state incompressible fluid networks, run the fluid-network Python solver, analyze explicit valve/fault scenarios, and export visualization data. Use for this project's fluid-network calculations and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lifangpeng](https://clawhub.ai/user/lifangpeng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to model steady-state fluid networks, compare explicitly listed operating scenarios, interpret solver results, and export visualization data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Visualization servers may expose exported engineering results to other computers without warning or access controls.

Mitigation: For local static viewing, bind the server to 127.0.0.1. Before using live controls, verify the server's listening address and access controls, and stop servers when finished.

Risk: Installing the external solver from an untrusted project checkout may introduce unsafe or unexpected code.

Mitigation: Install the solver only from a project checkout you trust.

## Reference(s):

- [TOML Schema Reference](schema-reference.md)
- [Network JSON Schema](schema.json)
- [Demo Network](assets/demo_network.toml)
- [ClawHub skill page](https://clawhub.ai/lifangpeng/skills/skill)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Analysis, Files]

**Output Format:** [Markdown guidance, TOML network configuration, shell commands, JSON reports, and visualization data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SI units; evaluates only listed scenarios and explicit user overrides.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
