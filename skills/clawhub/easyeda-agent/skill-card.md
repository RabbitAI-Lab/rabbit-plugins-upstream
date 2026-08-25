## Description:

EasyEDA Agent helps agents design, clean up, verify, and export EasyEDA Pro schematics and PCBs through the local easyeda CLI, daemon, connector, bundled scripts, and design workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Developers and hardware engineers use this skill to operate EasyEDA Pro projects through a local automation stack for schematic capture, PCB layout, linting, DRC/check workflows, part selection, BOM/netlist export, and design cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install and self-update powerful local EasyEDA tooling from remote shell code.

Mitigation: Prefer a version-pinned, verified install of the EasyEDA CLI and daemon instead of running a remote shell installer blindly.

Risk: Clear, probe, bulk, and other project operations can erase or alter design data.

Mitigation: Keep backups and review destructive operations before running them on valuable or proprietary PCB designs.

Risk: Lint baselines, audit logs, workflow state, and optional git history may retain schematic or PCB details locally.

Mitigation: Treat those local records as sensitive project data and review them before sharing or publishing artifacts.

## Reference(s):

- [EasyEDA Agent project homepage](https://github.com/zhoushoujianwork/easyeda-agent)
- [ClawHub EasyEDA Agent release page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [EasyEDA Agent releases](https://github.com/zhoushoujianwork/easyeda-agent/releases/latest)
- [EasyEDA Agent Connector marketplace page](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector)
- [Design Flow](references/design-flow.md)
- [Environment Setup](references/environment-setup.md)
- [Schematic Workflow Reference](references/schematic.md)
- [PCB Workflow Reference](references/pcb.md)
- [Actions Reference](references/actions.md)
- [PCB Design Rules](references/pcb-design-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, JSON/configuration edits, and file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update local EasyEDA project artifacts when the user asks the agent to operate on a project.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
