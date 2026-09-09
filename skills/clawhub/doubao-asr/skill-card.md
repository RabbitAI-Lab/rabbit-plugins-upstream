## Description:

Transcribes recorded audio files into text with speaker diarization and optional SRT or JSON output using ByteDance/Volcengine Doubao Seed-ASR 2.0.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vahnxu](https://clawhub.ai/user/vahnxu)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and end users use this skill to have an agent transcribe recorded meetings, voice memos, or supplied audio URLs. It supports speaker-separated transcripts plus subtitle or JSON outputs when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio content or supplied audio URLs are sent to Volcengine for transcription.

Mitigation: Use the skill only for recordings the user is comfortable sending to Volcengine, and avoid regulated or highly sensitive recordings unless the user's Volcengine account and policies permit it.

Risk: Uploaded audio can remain in the user's TOS bucket after transcription.

Mitigation: Use a dedicated TOS bucket with narrow read/write access and configure a lifecycle rule to delete uploaded audio.

Risk: Misconfigured storage permissions can expose audio or prevent the ASR service from reading uploaded files.

Mitigation: Grant only the required read/write bucket policy for the dedicated bucket and avoid broad IAM policies such as full object-storage access.

## Reference(s):

- [Volcengine Doubao audio file recognition documentation](https://www.volcengine.com/docs/6561/1354868)
- [ClawHub Doubao Asr listing](https://clawhub.ai/vahnxu/skills/doubao-asr)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text, Markdown guidance, JSON, SRT subtitles, or transcript files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local audio to the user's Volcengine TOS bucket or submit a supplied audio URL to Volcengine; transcript file writes are intended for the working directory or /tmp.]

## Skill Version(s):

0.23.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
