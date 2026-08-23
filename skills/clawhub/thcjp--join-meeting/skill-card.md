## Description:

A meeting bot skill that helps an agent join online meetings, monitor voice and TTS events, transcribe discussions, and generate meeting summaries and action items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure an agent for API-supported meeting participation, speaker-state monitoring, transcription, summaries, action item extraction, and optional TTS responses. It is intended for environments where automated meeting bots, recording, and transcription are explicitly allowed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes autonomous meeting attendance, listening, transcription, and speaking without enough consent and scope controls.

Mitigation: Use only in environments where meeting bots, recording, transcription, and automated participation are allowed, and require explicit user confirmation before joining or listening.

Risk: The artifact requests broad read, exec, and write authority.

Mitigation: Review before installing, disable broad exec/write access where possible, and restrict the skill to the minimum permissions needed for the approved meeting workflow.

Risk: Meeting transcripts and API credentials may expose sensitive information if stored or logged improperly.

Mitigation: Confirm where transcripts and credentials are stored, keep credentials in environment variables or approved secret stores, and avoid retaining meeting content beyond policy requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/join-meeting)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets and structured meeting summaries, transcripts, and action items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require meeting platform API credentials, TTS service configuration, and explicit user confirmation before joining, listening, transcribing, or speaking in a meeting.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
