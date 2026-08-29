## Description:

Fetches transcripts from YouTube videos, public podcast episodes including Xiaoyuzhou, other public single-item media links, and local audio or video files, preferring existing captions or official transcripts before approved VoiceFlow ASR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[niuzb](https://clawhub.ai/user/niuzb)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content analysts use this skill to obtain transcripts from supported public media links or local media files. The skill can also support transcript-grounded summaries, answers, or information extraction when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved media files, filenames, content type, and size may be sent to the VoiceFlow/AudioFlow transcription service for ASR.

Mitigation: Use existing captions or official transcripts first, and run remote ASR only after the user approves the external-processing disclosure.

Risk: Downloading a managed media tool modifies the local cache and introduces an external executable into the workflow.

Mitigation: Ask for separate approval before caching the pinned, SHA-256-verified yt-dlp release, or direct the user to manual installation.

Risk: VoiceFlow credentials could be exposed if copied into command arguments, logs, or repository files.

Mitigation: Use VOICEFLOW_TOKEN or browser authorization, avoid echoing tokens, and keep saved credentials in the user configuration directory.

## Reference(s):

- [Transcribe Media Skill Page](https://clawhub.ai/niuzb/skills/transcribe-media)
- [Transcribe a Xiaoyuzhou Episode](references/xiaoyuzhou.md)
- [VoiceFlow Dashboard](https://audioflow123.com/dashboard)
- [yt-dlp Installation](https://github.com/yt-dlp/yt-dlp/wiki/Installation)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text transcript or Markdown response; script output may be text or JSON containing transcript text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers existing captions or official transcripts; remote ASR and managed tool downloads require explicit user approval.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
