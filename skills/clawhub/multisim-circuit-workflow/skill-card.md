## Description:

Diagnose, configure, generate, simulate, and report on NI Multisim circuits through the Multisim MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yxy050208](https://clawhub.ai/user/yxy050208)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and electrical engineers use this skill to install or configure a local Multisim MCP workflow, generate schematics from approved circuit specifications, run circuit simulations, analyze waveforms, and produce design reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can start Multisim, connect to a local MCP server, and create circuit or report artifacts after approval.

Mitigation: Use the documented approval gates before connection, schematic generation, file writes, and simulation steps.

Risk: Unrestricted command mode could execute commands outside the ordinary safe simulation subset.

Mitigation: Use only the safe op, dc, ac, and tran command subset unless intentionally performing trusted local security research in an operator-enabled environment.

Risk: Circuit generation or reporting steps could overwrite existing user work if pointed at live project files.

Mitigation: Generate fragments and outputs in a working directory, inspect them, and save modified circuits to a new path unless the user explicitly approves replacement.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown, Files]

**Output Format:** [Markdown guidance with inline shell commands, configuration fragments, generated circuit artifacts, CSV data, and reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local Multisim project artifacts, netlists, CSV simulation data, schematic images, plots, and Markdown reports when the user approves the relevant workflow steps.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
