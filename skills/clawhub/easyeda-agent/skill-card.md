## Description: <br>
EasyEDA Agent helps agents design, clean up, verify, and export EasyEDA Pro schematics and PCBs through the local easyeda-agent CLI, daemon, and connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and electronics engineers use this skill to operate EasyEDA Pro through typed actions for schematic creation, safe refactoring, PCB layout, design-rule checks, BOM and netlist export, and staged board-delivery workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control an active EasyEDA project, local CLI tools, and an EasyEDA browser or profile session. <br>
Mitigation: Install only in trusted workspaces, use typed actions and dry-runs where available, inspect before mutating designs, and review board changes before saving or manufacturing. <br>
Risk: The skill includes raw JavaScript escape hatches for cases where typed EasyEDA actions are unavailable. <br>
Mitigation: Avoid debug.exec_js unless the user explicitly approves the reviewed snippet and the typed-action path cannot satisfy the task. <br>
Risk: Snapshot baselines and audit data can retain proprietary design details under local easyeda-agent storage. <br>
Mitigation: Avoid persistent snapshot baselines for confidential designs unless storage policy permits it, and clear or protect local easyeda-agent state after sensitive work. <br>
Risk: The artifact can prepare GitHub issues or block-library contributions from design evidence. <br>
Mitigation: Review any issue draft or contribution content before submission and do not submit external reports automatically. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent) <br>
- [EasyEDA Agent skill instructions](artifact/SKILL.md) <br>
- [EasyEDA design flow](artifact/references/design-flow.md) <br>
- [EasyEDA schematic workflow](artifact/references/schematic.md) <br>
- [EasyEDA PCB workflow](artifact/references/pcb.md) <br>
- [EasyEDA action reference](artifact/references/actions.md) <br>
- [Environment setup](artifact/references/environment-setup.md) <br>
- [PCB design rules](artifact/references/pcb-design-rules.md) <br>
- [JLC connector marketplace listing](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, structured summaries, and artifact paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include EasyEDA CLI commands, design checkpoints, DRC/check/lint status, BOM/netlist/export paths, and warnings that require user review.] <br>

## Skill Version(s): <br>
0.18.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
