## Description:

Generates bilingual Chinese–English SRT subtitles from audio and video by transcribing speech and translating timestamped segments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bjbook](https://clawhub.ai/user/bjbook)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to transcribe Chinese or English audio and video, translate each segment, and produce timestamped bilingual subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Initial setup may install faster-whisper and download a speech model from a configured mirror.

Mitigation: Preinstall a reviewed faster-whisper version in an isolated Python environment and assess whether you trust the model mirror.

Risk: Transcripts may contain sensitive information that the agent's translation provider receives.

Mitigation: Use a translation provider whose data handling is appropriate for the transcript before processing sensitive recordings.

Risk: Rerunning the workflow may replace existing subtitle files.

Mitigation: Preserve existing subtitle files before rerunning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bjbook/skills/zhz-subtitle)
- [Skill homepage](http://openclaw.bjbook.net/)

## Skill Output:

**Output Type(s):** [Files, Text, JSON]

**Output Format:** [SRT subtitle files, JSON transcript and translation data, and a completion summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Timestamped bilingual Chinese–English subtitle entries; the skill supports language, model-size, and subtitle-order options.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
