## Description:

Helps engineers design, repair, and verify EasyEDA Pro schematics and PCBs using parameterized workflows and readback checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Developers and electronics engineers use this skill to build or repair EasyEDA Pro schematics and PCB layouts, inspect connectivity and design checks, and verify saved project changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup scripts and local automation may execute broad commands or leave a persistent connector running.

Mitigation: Review setup steps, use a pinned release with verified checksums, and enable the local daemon and connector only when needed.

Risk: Automated apply actions can persist incorrect schematic or PCB changes.

Mitigation: Back up projects, review dry-run plans before approving writes, and verify saved changes with fresh readback and design checks.

Risk: Debug JavaScript helpers can run unreviewed commands in the design environment.

Mitigation: Avoid debug.exec_js helpers except for explicitly reviewed diagnostics.

## Reference(s):

- [EasyEDA Agent release on ClawHub](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [Project homepage (skill metadata)](https://github.com/zhoushoujianwork/easyeda-agent)
- [Design workflow](references/design-flow.md)
- [Environment setup](references/environment-setup.md)
- [PCB design rules](references/pcb-design-rules.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with commands and parameterized design data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Design changes require readback and validation; incomplete checks must be reported.]

## Skill Version(s):

1.8.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
