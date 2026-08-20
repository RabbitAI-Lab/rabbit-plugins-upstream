## Description:

EasyEDA Agent helps an agent design, clean up, verify, and export EasyEDA Pro schematics and PCB layouts using local EasyEDA tooling and bundled design rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Developers and hardware engineers use this skill to build or safely refactor EasyEDA Pro schematic and PCB projects, including part selection, schematic organization, PCB placement and routing checks, DRC/layout linting, and BOM or netlist export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control EasyEDA projects, the local EasyEDA daemon/CLI, and the browser profile used for EasyEDA.

Mitigation: Use it only in workspaces and browser profiles where that access is acceptable, and review proposed design changes before destructive actions or saves.

Risk: Troubleshooting guidance may include process-kill commands.

Mitigation: Check the exact target process before running any process-kill command.

Risk: Bundled bulk-operation scripts may be unsafe with untrusted bulk specifications until temp-file path handling is fixed.

Mitigation: Avoid untrusted bulk specs and review generated bulk operation inputs before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [EasyEDA Agent Source and Docs](https://github.com/zhoushoujianwork/easyeda-agent)
- [EasyEDA Agent Connector](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector)
- [Design Flow](references/design-flow.md)
- [Environment Setup](references/environment-setup.md)
- [Schematic Workflow](references/schematic.md)
- [PCB Workflow](references/pcb.md)
- [PCB Design Rules](references/pcb-design-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown text with inline shell commands, code snippets, and file or configuration changes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify EasyEDA design artifacts when used in an EasyEDA workspace.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
