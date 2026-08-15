## Description:

EasyEDA Agent helps agents design, clean up, verify, and export EasyEDA Pro schematics and PCBs through local EasyEDA automation workflows, references, and helper scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and electronics engineers use this skill to automate or guide EasyEDA Pro schematic and PCB work, including design from scratch, safe refactoring, part selection, wiring and layout checks, DRC, BOM and netlist export, and delivery summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify and save EasyEDA schematic and PCB projects through local automation.

Mitigation: Use health checks, inspect-before-mutate behavior, explicit save checkpoints, and DRC/check/layout gates before accepting design changes.

Risk: Raw debug execution can bypass typed EasyEDA actions when used.

Mitigation: Prefer typed EasyEDA actions and allow debug.exec_js only when a typed action is missing and the user explicitly accepts that path.

Risk: Part lookup and selection can depend on live JLC/LCSC service results and current availability.

Mitigation: Review selected LCSC C-numbers, BOM output, stock-sensitive choices, and manufacturing constraints before ordering or fabrication.

Risk: Local workflow, audit, lint, snapshot, BOM, netlist, and manufacturing files may persist project details.

Mitigation: Review generated local files and paths before sharing, committing, or submitting issue reports.

## Reference(s):

- [EasyEDA Agent ClawHub Page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [EasyEDA Agent Project Documentation](https://github.com/zhoushoujianwork/easyeda-agent)
- [EasyEDA Agent Connector Plugin](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector)
- [Design Flow](references/design-flow.md)
- [Schematic Workflow](references/schematic.md)
- [PCB Workflow](references/pcb.md)
- [Typed Actions Reference](references/actions.md)
- [PCB Design Rules](references/pcb-design-rules.md)
- [Environment Setup](references/environment-setup.md)
- [JLCPCB Fabrication Rule Fallbacks](references/fab-rules-jlcpcb.json)
- [Standard Parts Catalog](references/standard-parts.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration, Files]

**Output Format:** [Markdown guidance with EasyEDA CLI commands, JSON/YAML configuration references, and script/code outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update EasyEDA project state and local workflow, audit, lint, BOM, netlist, image, and manufacturing artifact files when used by an agent.]

## Skill Version(s):

0.25.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
