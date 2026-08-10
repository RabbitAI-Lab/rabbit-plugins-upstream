## Description:

EasyEDA Agent helps agents design, inspect, clean up, verify, and export EasyEDA Pro schematics and PCBs through the local easyeda CLI, daemon, and connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent operators use this skill to automate EasyEDA Pro schematic and PCB work, including board creation, safe refactoring, LCSC/JLC part placement, PCB synchronization, layout checks, DRC, BOM/netlist export, and manufacturing-oriented review gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify live EasyEDA schematic and PCB projects.

Mitigation: Use the skill's inspect-before-mutate flow, require explicit confirmation for destructive edits, and review check, DRC, layout-lint, and saved checkpoint status before accepting design changes.

Risk: The local automation path can affect persistent EasyEDA connector or browser profile state.

Mitigation: Install and run it only in an intended EasyEDA profile, keep CLI and connector versions aligned, and avoid connector hot-reload paths unless doing isolated connector development.

Risk: Helper scripts run as local code with the user's file permissions and some workflows may query network part data.

Mitigation: Review scripts before use, run them from a trusted workspace, and confirm network-backed part lookups are acceptable for the project.

## Reference(s):

- [EasyEDA Agent source and docs](https://github.com/zhoushoujianwork/easyeda-agent)
- [EasyEDA Agent Connector listing](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector)
- [EasyEDA Design Flow](references/design-flow.md)
- [EasyEDA Schematic](references/schematic.md)
- [EasyEDA PCB](references/pcb.md)
- [EasyEDA Action Reference](references/actions.md)
- [Environment Setup](references/environment-setup.md)
- [JLCPCB Fabrication Rules](references/fab-rules-jlcpcb.json)
- [Standard Parts Catalog](references/standard-parts.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Markdown, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, generated EasyEDA design artifacts, BOM/netlist exports, and local script output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May operate through a local EasyEDA CLI/daemon/connector and helper scripts that inspect or mutate live EasyEDA projects.]

## Skill Version(s):

0.22.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
