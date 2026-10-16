## Description:

Helps engineers design, edit, and check EasyEDA Pro schematics and PCBs using a local editor connection, including readback and save verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Electronics engineers and developers use this skill to plan and modify EasyEDA Pro schematic and PCB designs, check connectivity and layout, and confirm that project changes were saved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer or updater can execute downloaded code.

Mitigation: Install only from a trusted publisher; inspect or download the installer separately rather than piping it directly to a shell.

Risk: The local EasyEDA connection can modify and save open projects.

Mitigation: Back up important designs, use dry-runs where available, and confirm changes through fresh readback before relying on a saved project.

## Reference(s):

- [EasyEDA Agent project homepage](https://github.com/zhoushoujianwork/easyeda-agent)
- [Environment setup and connection](references/environment-setup.md)
- [Schematic data contract](references/schematic-data.md)
- [PCB layout guidance](references/pcb-layout.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Files]

**Output Format:** [Markdown instructions and commands; design changes and verification results in EasyEDA projects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports readback, checks, save status, and any unverified design aspects.]

## Skill Version(s):

1.13.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
