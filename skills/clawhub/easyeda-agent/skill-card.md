## Description:

Helps engineers design, repair, and verify EasyEDA Pro schematics and PCBs using local automation and readback checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Developers and electronics engineers use this skill to plan, edit, and check EasyEDA Pro schematics and PCB layouts, including connectivity, geometry, design rules, and saved results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A remote installer can execute changing code on the local machine.

Mitigation: Trust the publisher before installation; prefer a pinned release and verify its checksum instead of piping an installer into a shell.

Risk: The connector and daemon can modify or delete schematic and PCB data in the active project.

Mitigation: Work on copies of important projects, review dry-runs before writing, and read back the saved result.

Risk: Raw API access and disabled protection or design-rule checks can bypass expected safeguards.

Mitigation: Review raw API actions and avoid --no-protect or --no-drc unless their effects are understood.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [Project homepage (skill metadata)](https://github.com/zhoushoujianwork/easyeda-agent)
- [Design workflow](references/design-flow.md)
- [CLI and actions reference](references/actions.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with CLI commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes project-specific plans and verification findings.]

## Skill Version(s):

1.9.0 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
