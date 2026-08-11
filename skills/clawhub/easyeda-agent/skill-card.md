## Description:

EasyEDA Agent helps developers design, clean up, verify, and export EasyEDA Pro schematics and PCBs through local EasyEDA automation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and electronics engineers use this skill to operate EasyEDA Pro through a local CLI, daemon, and connector for schematic capture, PCB layout, validation gates, BOM and netlist export, and manufacturing-oriented design review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make broad schematic and PCB edits through the local EasyEDA daemon and connector.

Mitigation: Use the documented inspect-before-mutate workflow, confirm destructive actions, and review validation gate results before accepting design changes.

Risk: Part replacements, network part lookups, browser or profile setup, and screenshot or recording outputs may affect project data or expose local context.

Mitigation: Approve those actions explicitly, rely on trusted local specifications, and inspect generated outputs before sharing or manufacturing.

Risk: PCB or schematic mutations can leave stale views or incomplete validation if workflow gates are skipped.

Mitigation: Run the skill's save, reload, DRC, check, bridge-check, and layout-lint gates as described before progressing to later design stages.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [SKILL.md](artifact/SKILL.md)
- [Design Flow](artifact/references/design-flow.md)
- [Schematic Workflow](artifact/references/schematic.md)
- [PCB Workflow](artifact/references/pcb.md)
- [Typed Actions Reference](artifact/references/actions.md)
- [Environment Setup](artifact/references/environment-setup.md)
- [PCB Design Rules](artifact/references/pcb-design-rules.md)
- [Part Selection](artifact/references/part-selection.md)
- [EasyEDA Agent Connector Marketplace](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, configuration, and generated EasyEDA project artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include validation summaries, saved artifact paths, BOM/netlist exports, and gate status reports.]

## Skill Version(s):

0.23.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
