## Description:

Organizes OpenClaw conversations into deduplicated long-term memory and daily logs, with sensitive-information safeguards and user-controlled writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to distill conversation history into workspace memory, build missing long-term memory from past logs, and keep daily records organized without duplicating entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plaintext memory files can retain sensitive or third-party private information.

Mitigation: Review the distillation report before approving writes and do not store secrets or third-party private data in memory files.

Risk: Enabling autoWrite permits unattended changes to workspace memory.

Mitigation: Leave autoWrite disabled unless unattended updates are acceptable; inspect proposed changes before enabling it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-memory-distill)
- [Publisher-provided project documentation](https://github.com/dtsola/xiaoyaoclaw-memory-distill)

## Skill Output:

**Output Type(s):** [Markdown, Text reports, JSON configuration]

**Output Format:** [Markdown memory files and distillation reports; JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes workspace memory after confirmation; scheduled runs report only unless autoWrite is enabled.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
