## Description:

智能会议机器人 helps an agent join API-supported meetings, track meeting lifecycle and voice events, transcribe discussion, produce summaries and action items, and optionally speak through TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers can use this skill to automate meeting participation workflows, including joining supported meetings, monitoring speaker state, capturing transcripts, producing summaries, and extracting follow-up tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes automatic joining, listening, transcription, and saved meeting records without clearly defining consent or retention expectations.

Mitigation: Use it only where each meeting join can be explicitly approved, participants can be notified as required, and transcript storage and deletion locations are controlled.

Risk: The artifact requests broad execution and write capabilities for meeting automation.

Mitigation: Avoid granting broad exec or write authority unless the publisher narrows the needed commands and data locations for the supported meeting platforms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/join-meeting)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON response examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include meeting summaries, transcripts, action items, status updates, execution logs, and configuration guidance.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
