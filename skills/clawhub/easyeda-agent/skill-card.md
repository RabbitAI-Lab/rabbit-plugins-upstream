## Description:

Helps engineers design, edit, and verify EasyEDA Pro schematics and PCB layouts using project data and live design checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Engineers and developers use this skill to create or refine EasyEDA Pro circuit designs, select parts, lay out and route PCBs, and check connections, geometry, design rules, and saved results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can edit live EasyEDA projects; a bundled schematic helper can change or delete open content through a less controlled path.

Mitigation: Use only with a trusted publisher and projects you are willing to modify; remove or avoid artifact/scripts/sch.py until that path uses typed actions, and review changes and saved results.

Risk: Installation instructions pipe remote scripts directly into a shell.

Mitigation: Review the installer scripts before executing them rather than piping downloads directly to a shell.

## Reference(s):

- [Project homepage (skill metadata)](https://github.com/zhoushoujianwork/easyeda-agent)
- [Version 1.14.0 release notes](https://github.com/zhoushoujianwork/easyeda-agent/releases/tag/v1.14.0)
- [Design workflow](artifact/references/design-flow.md)
- [Environment setup](artifact/references/environment-setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Design files]

**Output Format:** [Markdown guidance, structured design data, and EasyEDA project changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports checks, limitations, and save/readback evidence for live project edits.]

## Skill Version(s):

1.14.0 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
