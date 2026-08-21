## Description:

EasyEDA Agent helps agents design, clean up, and verify EasyEDA Pro schematics and PCBs through the local easyeda-agent CLI, daemon, and connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Developers and electronics engineers use this skill to automate EasyEDA Pro board-design work, including schematic organization, part selection, PCB layout, design-rule checks, and export preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on local tooling that can control EasyEDA projects through a daemon and connector.

Mitigation: Install and run it only in trusted workspaces, confirm the active EasyEDA window before mutation, and review proposed schematic or PCB changes before saving.

Risk: Remote install, update, and self-update flows may run code from the project distribution channel.

Mitigation: Prefer read-only update checks first and review installer or update commands before use in locked-down or production environments.

Risk: Automation may interact with browser profiles, connector state, IndexedDB hot-reload paths, and recovery commands.

Mitigation: Use a dedicated browser or EasyEDA profile for automation and reserve hot-reload or process-kill recovery steps for development or explicit troubleshooting.

Risk: Workflow, audit, and optional lint snapshots may persist local design state under the user's home directory.

Mitigation: Treat persisted snapshots as project data and clear or protect them according to the user's design-confidentiality requirements.

Risk: Online part lookup can disclose part search terms to JLC/LCSC services.

Mitigation: Use online lookup only when sharing those search terms is acceptable; otherwise rely on local or pre-approved part data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [Project Homepage](https://github.com/zhoushoujianwork/easyeda-agent)
- [Release v1.1.1](https://github.com/zhoushoujianwork/easyeda-agent/releases/tag/v1.1.1)
- [EasyEDA Agent Connector](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector)
- [Environment Setup](references/environment-setup.md)
- [EasyEDA Design Flow](references/design-flow.md)
- [EasyEDA Action Reference](references/actions.md)
- [EasyEDA Schematic](references/schematic.md)
- [EasyEDA PCB](references/pcb.md)
- [PCB Design Rules](references/pcb-design-rules.md)
- [Part Selection](references/part-selection.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline commands, code snippets, configuration guidance, and generated design artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify local EasyEDA project artifacts through the required local CLI, daemon, and connector.]

## Skill Version(s):

1.1.1 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
