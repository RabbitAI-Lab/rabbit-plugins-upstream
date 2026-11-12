## Description:

Design, clean up, and verify EasyEDA Pro schematics and PCBs using component data and read-back checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Developers and electronics engineers use this skill to create or update EasyEDA Pro schematics and PCB layouts, and to check connectivity, geometry, design rules, and saved results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports an unsafe remote installer and says some files were only partially inspected, so the scan cannot establish that unreviewed portions are safe.

Mitigation: Review the installer and verify it through a trusted source; inspect the instructions and scripts before installation.

Risk: The security guidance identifies possible unintended changes to schematics, catalogs, temporary files, or Git history.

Mitigation: Keep a project snapshot or source copy, inspect the relevant scripts, and check read-back results and changes before saving or accepting edits.

## Reference(s):

- [EasyEDA Agent on ClawHub](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [Project homepage listed in skill metadata](https://github.com/zhoushoujianwork/easyeda-agent)
- [Release notes](https://github.com/zhoushoujianwork/easyeda-agent/releases/tag/v1.17.0)
- [Design flow](references/design-flow.md)
- [EasyEDA environment setup](references/environment-setup.md)
- [Schematic data and validation](references/schematic-data.md)
- [PCB layout](references/pcb-layout.md)
- [PCB routing](references/pcb-routing.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, JSON design data, Shell commands, EasyEDA project edits]

**Output Format:** [Markdown, JSON, shell commands, and EasyEDA project documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project changes are checked through read-back; the skill requires explicit saved-state evidence for completion.]

## Skill Version(s):

1.17.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
