## Description:

TimelinesAI (timelines.ai). Use this skill for ANY TimelinesAI request — reading, creating, and updating data. Whenever a task involves TimelinesAI, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to read TimelinesAI workspace, chat, message, status, and WhatsApp account data, and to send plain-text WhatsApp messages through an OOMOL-connected TimelinesAI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code if followed without verification.

Mitigation: Review setup instructions before installing; prefer an official package manager or a version-pinned installer with checksum or signature verification, and do not let an agent run the remote installer automatically.

Risk: Sending WhatsApp messages changes external communication state and may contact the wrong recipient or send unintended text.

Mitigation: Require explicit confirmation of the recipient and message text before running write actions.

## Reference(s):

- [TimelinesAI Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-timelinesai)
- [TimelinesAI Homepage](https://timelines.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent actions may return JSON data and execution metadata from the TimelinesAI connector.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
