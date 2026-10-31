## Description:

Automates multi-round code review and iteration with parallel reviews, a defensive-programming mode, onboarding, and checksum-verified cross-assistant installation and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to review and iteratively improve a codebase, run configured validation, and generate project onboarding and configuration files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting instructions may publish code without approval.

Mitigation: Work in an isolated repository copy without push permission until instructions are corrected; do not assume disabling automatic pushes prevents publication.

Risk: Installation controls may not consistently match their promises.

Mitigation: Review each configured command, explicitly select the installation destination, keep signature checks enabled, and avoid the optional pipe-to-bash installer.

## Reference(s):

- [Iterate on ClawHub](https://clawhub.ai/jingzhao-l/skills/iterate-skill)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown summaries, code changes, shell commands, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Iterative project-wide reviews and changes, scoped by the user's goal and configured round limit.]

## Skill Version(s):

3.8.2 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
