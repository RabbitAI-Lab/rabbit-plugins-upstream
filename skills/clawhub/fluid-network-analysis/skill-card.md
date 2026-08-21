## Description:

Design, validate, solve, and analyze schema 1.0 steady-state incompressible fluid networks from TOML or natural-language requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhang1jing2](https://clawhub.ai/user/zhang1jing2)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or validate schema 1.0 fluid-network TOML, run local pressure and flow analysis, and report scenario-specific function availability for explicitly modeled steady-state systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Engineering conclusions can be misleading when topology, boundary pressures, resistance data, load thresholds, or scenario assumptions are incomplete or incorrect.

Mitigation: Validate TOML before solving, state assumptions explicitly, and review convergence, residuals, pressure, flow, and function-status outputs before relying on results.

Risk: The skill runs a bundled local Python analyzer against user-provided model files.

Mitigation: Run it in an appropriate workspace and review model inputs and generated reports before using outputs for engineering decisions.

## Reference(s):

- [TOML Schema 1.0 Reference](references/schema.md)
- [ClawHub skill page](https://clawhub.ai/zhang1jing2/skills/fluid-network-analysis)
- [Publisher profile](https://clawhub.ai/user/zhang1jing2)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON reports with TOML configuration and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include validation status, solver convergence, mass-balance residuals, pressure and flow results, velocity, and scenario function status.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
