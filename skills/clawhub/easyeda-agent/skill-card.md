## Description:

Community EasyEDA Agent automation skill for EasyEDA Pro schematic and PCB work through the local easyeda-agent CLI, daemon, and connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Developers and electronics engineers use this skill to design, inspect, clean up, verify, and export EasyEDA Pro schematics and PCBs while applying staged workflow gates and JLC/LCSC-oriented design conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or save live EasyEDA schematics and PCBs.

Mitigation: Use a test or scratch project first, require confirmation before destructive actions, and review DRC/check/lint results before accepting design changes.

Risk: Some maintenance paths can interact with browser-session-backed EasyEDA state and local workflow or audit files.

Mitigation: Install only in environments where that access is intended, avoid the IndexedDB hot-reload path unless doing connector development, and restrict browser-kill or update actions to explicit operator approval.

Risk: The skill may query JLC/LCSC services and use live EasyEDA connector state.

Mitigation: Confirm network and account-use expectations before deployment and keep CLI, connector, and skill versions aligned.

## Reference(s):

- [EasyEDA Agent source and docs](https://github.com/zhoushoujianwork/easyeda-agent)
- [EasyEDA Agent connector listing](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector)
- [Design flow](references/design-flow.md)
- [Environment setup](references/environment-setup.md)
- [EasyEDA action reference](references/actions.md)
- [Schematic workflow](references/schematic.md)
- [PCB workflow](references/pcb.md)
- [PCB design rules](references/pcb-design-rules.md)
- [Part selection](references/part-selection.md)
- [JLCPCB fabrication rule fallback](references/fab-rules-jlcpcb.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and references to generated design artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include EasyEDA command traces, DRC/check/lint status, saved checkpoints, exported BOMs, netlists, images, and artifact paths.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
