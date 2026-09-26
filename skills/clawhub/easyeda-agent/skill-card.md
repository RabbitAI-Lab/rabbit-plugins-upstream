## Description:

Helps engineers build, repair, and verify EasyEDA Pro schematics and PCBs using parameterized designs and readback checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Electronics developers and engineers use this skill to plan, edit, and check EasyEDA Pro schematics and PCB layouts, including connectivity, geometry, design rules, and saved results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing local tooling from unreviewed scripts may introduce unwanted changes.

Mitigation: Install only from a trusted publisher; review or pin installer scripts before running them.

Risk: Schematic or PCB edits may damage a real design or leave results unverified.

Mitigation: Back up projects, preview changes where possible, and check saved readback and design-rule results.

Risk: Broad debug helpers or bypass flags can circumvent normal design safeguards.

Mitigation: Avoid raw debug helpers and no-DRC or no-protection bypasses unless the board-level risk is understood.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [Project homepage (skill metadata)](https://github.com/zhoushoujianwork/easyeda-agent)
- [Installation and connection guidance](references/environment-setup.md)
- [Design workflow](references/design-flow.md)
- [PCB routing and verification](references/pcb-routing.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with commands and parameterized JSON data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can modify EasyEDA projects; verify changes through saved readback and design-rule checks.]

## Skill Version(s):

1.7.0 (source: skill metadata and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
