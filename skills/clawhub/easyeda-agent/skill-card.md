## Description:

Use the local EasyEDA Pro CLI and connected interfaces to design or refine schematics and PCB layouts, then verify connections, geometry, design-rule checks, and saved results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Electronics designers and engineers use this skill to build or safely revise EasyEDA Pro schematics and PCBs, then check connectivity, layout geometry, design-rule results, and saved state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer is unverified, and scan coverage is incomplete.

Mitigation: Verify the installer source independently and review its contents before installing.

Risk: Design changes could overwrite existing content or create unintended connections.

Mitigation: Keep a source copy, review proposed edits before applying them, and verify connectivity with fresh readback afterward.

## Reference(s):

- [EasyEDA Agent project homepage](https://github.com/zhoushoujianwork/easyeda-agent)
- [ClawHub skill page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [Release notes for 1.18.2](https://github.com/zhoushoujianwork/easyeda-agent/releases/tag/v1.18.2)
- [Design flow](references/design-flow.md)
- [Schematic data and validation](references/schematic-data.md)
- [PCB layout guidance](references/pcb-layout.md)
- [PCB routing guidance](references/pcb-routing.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, EasyEDA design files, Validation reports]

**Output Format:** [Markdown guidance, shell commands, and structured EasyEDA project data and reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update the active EasyEDA project; results should be checked against fresh readback and save evidence.]

## Skill Version(s):

1.18.2 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
