## Description:

EasyEDA Agent helps agents design, clean up, verify, and export EasyEDA Pro schematics and PCBs through the local easyeda CLI, daemon, and connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and electronics engineers use this skill to automate EasyEDA Pro schematic and PCB workflows, including board creation, existing-design cleanup, part selection, layout, checks, and export preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform local EasyEDA project edits that affect real schematics and PCB files.

Mitigation: Review proposed actions before execution and use backups or scratch projects for probes and first-time use.

Risk: Connector hot-reload and persistent browser-profile setup can change a development browser environment.

Mitigation: Use connector hot-reload only in a development profile and keep production or personal browser profiles separate.

Risk: Part-selection workflows may make optional third-party JLC/LCSC network queries.

Mitigation: Confirm that external part lookup is acceptable for the project before running part-selection workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [EasyEDA Agent source and docs](https://github.com/zhoushoujianwork/easyeda-agent)
- [EasyEDA Agent connector listing](https://jlc-ext.com/item/zhoushoujian/easyeda-agent-connector)
- [EasyEDA Design Flow](artifact/references/design-flow.md)
- [EasyEDA Schematic](artifact/references/schematic.md)
- [EasyEDA PCB](artifact/references/pcb.md)
- [EasyEDA Action Reference](artifact/references/actions.md)
- [Environment setup](artifact/references/environment-setup.md)
- [JLC/LCSC part selection](artifact/references/part-selection.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline EasyEDA CLI commands and references to local scripts or configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run local EasyEDA project edits, validation checks, exports, and optional JLC/LCSC part-selection queries.]

## Skill Version(s):

0.21.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
