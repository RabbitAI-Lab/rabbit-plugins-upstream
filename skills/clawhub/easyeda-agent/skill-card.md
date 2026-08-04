## Description: <br>
Design, clean up, and verify EasyEDA Pro schematics and PCBs through the local easyeda-agent CLI, daemon, and connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and electrical engineers use this skill to operate EasyEDA Pro through typed CLI and daemon actions for schematic creation or refactoring, PCB synchronization and layout, DRC and design-rule checks, and manufacturing artifact export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad control over a logged-in EasyEDA or browser environment. <br>
Mitigation: Install only when agent operation of EasyEDA projects is intended, verify the active EasyEDA target before action, and require confirmation before destructive schematic, PCB, or browser-profile changes. <br>
Risk: Connector hot-reload and IndexedDB paths can persist changes outside ordinary project files. <br>
Mitigation: Avoid connector hot-reload except during deliberate connector development, and require explicit confirmation before IndexedDB, browser-profile, or persistent standard-parts changes. <br>
Risk: Incorrect schematic or PCB actions can damage topology, layout quality, or manufacturability. <br>
Mitigation: Use the skill's inspect-before-mutate workflow, typed actions, staged save points, layout linting, DRC, bridge checks, and post-route checks before accepting changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent) <br>
- [Source and Documentation](https://github.com/zhoushoujianwork/easyeda-agent) <br>
- [EasyEDA Agent Connector Marketplace Listing](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector) <br>
- [Design Flow](references/design-flow.md) <br>
- [Schematic Workflow](references/schematic.md) <br>
- [PCB Workflow](references/pcb.md) <br>
- [Action Reference](references/actions.md) <br>
- [Environment Setup](references/environment-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown instructions with inline CLI commands and JSON/YAML reference data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May operate local EasyEDA projects through the easyeda-agent CLI, daemon, connector, and optional MCP adapter.] <br>

## Skill Version(s): <br>
0.19.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
