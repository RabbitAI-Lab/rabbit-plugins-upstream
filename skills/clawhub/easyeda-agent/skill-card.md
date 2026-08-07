## Description:

EasyEDA Agent helps agents design, clean up, and verify EasyEDA Pro schematics and PCBs through the local EasyEDA Agent CLI, daemon, and connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and electronics engineers use this skill to automate EasyEDA Pro schematic and PCB work, including board creation, cleanup, refactoring, part placement, PCB synchronization, checks, DRC, BOM/netlist export, and guided design workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local EasyEDA CLI, daemon, and connector can control open EasyEDA designs and perform real mutations such as clear, delete, replace, routing, and export actions.

Mitigation: Use the skill only with intended projects, keep design backups, inspect before mutation, and treat destructive or routing operations as changes that require deliberate confirmation.

Risk: Setup and helper workflows can persistently modify the user's browser or EasyEDA connector environment.

Mitigation: Prefer the normal marketplace or release-based connector installation path; use IndexedDB hot reload only as an explicit developer action after backing up or accepting the risk.

Risk: The workflow may query external JLC/LCSC catalog APIs and store workflow or lint data under ~/.easyeda-agent.

Mitigation: Confirm that external catalog queries and local workflow storage are acceptable for the design context before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [Release v0.21.2](https://github.com/zhoushoujianwork/easyeda-agent/releases/tag/v0.21.2)
- [Project Source and Docs](https://github.com/zhoushoujianwork/easyeda-agent)
- [EasyEDA Agent Connector](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector)
- [EasyEDA Action Reference](references/actions.md)
- [EasyEDA Design Flow](references/design-flow.md)
- [Environment Setup](references/environment-setup.md)
- [PCB Design Rules](references/pcb-design-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON or playbook snippets, and generated EasyEDA workflow artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce EasyEDA design mutations, checks, exports, BOM/netlist artifacts, and local files through the EasyEDA CLI/daemon.]

## Skill Version(s):

0.21.2 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
