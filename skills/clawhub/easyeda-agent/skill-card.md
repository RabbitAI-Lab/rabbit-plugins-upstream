## Description: <br>
EasyEDA Agent automates EasyEDA Pro schematic and PCB workflows through the local easyeda-agent CLI, daemon, and connector, including board design, inspection, part placement, routing checks, DRC/layout linting, and artifact export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and electronics engineers use this skill to guide agents through EasyEDA Pro schematic and PCB design, inspection, validation, and manufacturing artifact export using the local easyeda-agent tooling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can alter live EasyEDA schematic and PCB projects. <br>
Mitigation: Work from backups, inspect proposed changes, approve destructive actions explicitly, and review EasyEDA check, DRC, and layout-lint results before accepting outputs. <br>
Risk: Helper or recovery paths may have weak safeguards. <br>
Mitigation: Use recovery actions only when the EasyEDA daemon or connector is stuck, and confirm project state is saved before running them. <br>
Risk: Workflow state and lint baselines can retain local design data. <br>
Mitigation: Store generated baselines and workflow files in an appropriate local project area and remove sensitive design artifacts before sharing logs or reports. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent) <br>
- [EasyEDA Agent Connector Marketplace](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector) <br>
- [EasyEDA Design Flow](artifact/references/design-flow.md) <br>
- [EasyEDA Schematic](artifact/references/schematic.md) <br>
- [EasyEDA PCB](artifact/references/pcb.md) <br>
- [EasyEDA Action Reference](artifact/references/actions.md) <br>
- [Environment Setup](artifact/references/environment-setup.md) <br>
- [PCB Design Rules](artifact/references/pcb-design-rules.md) <br>
- [Part Selection](artifact/references/part-selection.md) <br>
- [Standard Parts Catalog](artifact/references/standard-parts.json) <br>
- [JLCPCB Fabrication Rule Fallback](artifact/references/fab-rules-jlcpcb.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and file or artifact paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include EasyEDA CLI commands, design-check summaries, DRC/layout-lint status, and exported BOM, netlist, or manufacturing artifact paths.] <br>

## Skill Version(s): <br>
0.18.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
