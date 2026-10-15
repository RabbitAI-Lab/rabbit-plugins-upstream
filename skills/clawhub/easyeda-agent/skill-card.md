## Description:

Helps design, edit, and verify EasyEDA Pro schematics and PCB layouts using project data and readback checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhoushoujianwork](https://clawhub.ai/user/zhoushoujianwork)

### License/Terms of Use:

MIT

## Use Case:

Electronics engineers and designers use this skill to develop or refine EasyEDA Pro schematics and PCB layouts, check connectivity and design rules, and verify saved results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing unreviewed scripts from a moving branch can execute unexpected code.

Mitigation: Use a trusted, pinned release and verify its checksum; avoid piping remote scripts directly into a shell.

Risk: Editor writes can alter or damage an unintended EasyEDA project.

Mitigation: Back up projects and confirm the active project and document before every write.

Risk: Raw helper scripts or disabled protection and design-rule checks can bypass safeguards.

Mitigation: Avoid raw helpers; reserve unsafe flags for manual exceptions followed by fresh design-rule checks, save, reload, and readback.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhoushoujianwork/skills/easyeda-agent)
- [Project homepage (skill metadata)](https://github.com/zhoushoujianwork/easyeda-agent)
- [Design workflow](artifact/references/design-flow.md)
- [Environment and installation](artifact/references/environment-setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Design artifacts, Verification reports]

**Output Format:** [Markdown or text guidance, JSON reports, and EasyEDA project documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Design changes require save, reload, and readback verification.]

## Skill Version(s):

1.12.0 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
