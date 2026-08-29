## Description:

EasyEDA Agent helps developers design, refactor, lay out, and verify EasyEDA Pro schematics and PCBs through the local easyeda-agent CLI, daemon, and connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Developers and electronics engineers use this skill to operate EasyEDA Pro workflows for schematic creation, schematic cleanup, PCB synchronization, layout, checks, DRC, BOM/netlist export, and LCSC/JLC part selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external local CLI, daemon, and EasyEDA connector with broad ability to inspect and change EasyEDA projects.

Mitigation: Install only when the publisher and external tooling are trusted, verify the active EasyEDA window with health checks, and keep project backups or checkpoints before material changes.

Risk: Automation can make destructive or unintended schematic and PCB edits when pointed at the wrong project, window, page, or board.

Mitigation: Use typed actions, inspect project state before mutation, prefer dry-run modes, and require confirmation before destructive operations.

Risk: Debug execution paths can bypass the normal typed-action safeguards.

Mitigation: Avoid debug.exec_js unless a typed action is unavailable and the operator explicitly accepts the narrower review burden.

Risk: Local EasyEDA agent state, lint snapshots, and generated artifacts may contain confidential design details.

Mitigation: Review local state and exported artifacts before sharing, and run the skill only on projects whose confidentiality posture permits local automation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [Project Homepage](https://github.com/zhoushoujianwork/easyeda-agent)
- [Release v1.2.10](https://github.com/zhoushoujianwork/easyeda-agent/releases/tag/v1.2.10)
- [EasyEDA Agent Connector](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector)
- [Design Flow](references/design-flow.md)
- [Environment Setup](references/environment-setup.md)
- [Schematic Workflow](references/schematic.md)
- [PCB Workflow](references/pcb.md)
- [PCB Layout](references/pcb-layout.md)
- [PCB Routing](references/pcb-routing.md)
- [PCB Design Rules](references/pcb-design-rules.md)
- [Part Selection](references/part-selection.md)
- [Standard Parts](references/standard-parts.json)
- [Symbol Pins](references/symbol-pins.json)
- [JLCPCB Fabrication Rules](references/fab-rules-jlcpcb.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, code, files]

**Output Format:** [Markdown guidance with inline shell commands and structured file or configuration suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires EasyEDA Pro plus the local easyeda-agent CLI, daemon, and connector; network access is only described for LCSC lookup and self-update.]

## Skill Version(s):

1.2.10 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
