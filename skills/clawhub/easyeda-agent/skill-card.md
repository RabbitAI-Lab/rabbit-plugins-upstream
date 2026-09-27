## Description:

Helps engineers build, repair, and verify EasyEDA Pro schematics and PCB layouts using parameterized design steps and readback checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Electronics developers and engineers use this skill to plan, edit, and check EasyEDA Pro schematic and PCB projects through a command-line workflow. They should confirm results in the live project before relying on a design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installation and updates can execute code from external sources.

Mitigation: Trust and inspect the publisher and repository; download and review installers rather than piping them directly into a shell.

Risk: Browser API helper scripts can make unintended changes to EasyEDA designs.

Mitigation: Back up projects, use a least-privileged account or test project first, and avoid raw debug.exec_js helpers and disabled safety checks unless their impact is understood.

## Reference(s):

- [EasyEDA Agent project homepage](https://github.com/zhoushoujianwork/easyeda-agent)
- [EasyEDA Agent release on ClawHub](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [Design workflow](artifact/references/design-flow.md)
- [Installation and environment setup](artifact/references/environment-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and validation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live readback is needed to verify changes; full-board routing and final PCB DRC are not validated for this release.]

## Skill Version(s):

1.8.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
