## Description:

Design, clean up, and verify EasyEDA schematics and PCBs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Developers and hardware engineers use this skill to create or refine EasyEDA Pro schematics and PCB layouts, check connectivity, geometry, and design-rule results, and verify saved project state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bootstrap install command has not been verified, and the available scan did not inspect all referenced content.

Mitigation: Independently inspect the bootstrap command and review the remaining referenced content before installation.

Risk: ClawScan reports concerns in documented project-editing workflows and scripts.

Mitigation: Review the project-editing safeguards, work on a project copy where practical, and verify edits through fresh readback before saving.

## Reference(s):

- [EasyEDA Agent on ClawHub](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [Publisher-provided project homepage](https://github.com/zhoushoujianwork/easyeda-agent)
- [EasyEDA Agent v1.20.0 release notes](https://github.com/zhoushoujianwork/easyeda-agent/releases/tag/v1.20.0)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Schematic and PCB project files]

**Output Format:** [Markdown guidance, shell commands, and structured JSON with EasyEDA project edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project changes require fresh readback and save/reload verification; results depend on the connected EasyEDA Pro project and supported interfaces.]

## Skill Version(s):

1.20.0 (source: server-resolved release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
