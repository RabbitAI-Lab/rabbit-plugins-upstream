## Description:

Organizes OpenClaw conversations into long-term and daily workspace memory with deduplication and sensitive-content skipping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and developers use this skill to distill conversation history into persistent workspace memory, keeping long-term notes separate from daily logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory and daily logs are plain-text local records that may contain personal context.

Mitigation: Review the generated files, avoid storing secrets or third-party private information, and limit who can access workspace memory.

Risk: Enabling autoWrite allows scheduled runs to update memory without per-run confirmation.

Mitigation: Keep autoWrite disabled unless unattended updates are intended; review proposed changes and archived copies.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-memory-distill)
- [Skill documentation](https://github.com/dtsola/xiaoyaoclaw-memory-distill)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Guidance]

**Output Format:** [Markdown memory files and reports; JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Manual writes require confirmation; scheduled runs report only unless autoWrite is enabled.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
