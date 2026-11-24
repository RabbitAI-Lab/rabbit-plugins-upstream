## Description:

Turns audio or video into text or subtitles offline with local speech models, and keeps a dictation dictionary accurate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geragarazagh](https://clawhub.ai/user/geragarazagh)

### License/Terms of Use:

MIT-0

## Use Case:

External users can transcribe local audio and video into text or subtitles, search past dictations, and maintain a speech-to-text dictionary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live microphone activation was flagged as beyond the skill's stated scope.

Mitigation: Review the microphone toggle behavior and grant host microphone permission only when live dictation is intended.

Risk: The security analysis was partial, leaving some setup details unassessed.

Mitigation: Review the platform-specific setup steps before use, and get user approval before installing software or downloading a model.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/geragarazagh/skills/offline-stt)
- [Publisher profile](https://clawhub.ai/user/geragarazagh)

## Skill Output:

**Output Type(s):** [Text, Files, Shell commands, Guidance]

**Output Format:** [Transcription text or .txt/.srt files, with a concise Markdown response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local speech recognition; transcription language can be automatic or user-selected.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
