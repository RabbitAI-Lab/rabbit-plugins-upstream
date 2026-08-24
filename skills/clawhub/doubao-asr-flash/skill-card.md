## Description:

Transcribes local audio or video files and public audio URLs with Volcengine Doubao ASR Flash, returning plain text, JSON with utterance timestamps, or SRT subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blackcorvu](https://clawhub.ai/user/blackcorvu)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agents use this skill to convert recordings, meetings, interviews, podcasts, video audio, and public audio URLs into transcripts, subtitles, or timestamped JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected audio or video content is uploaded to Volcengine for cloud transcription.

Mitigation: Use only when the user approves sending the content to Volcengine, and avoid sensitive recordings unless that upload is explicitly acceptable.

Risk: The security evidence reports that the script sends the API key as the default user identifier.

Mitigation: Prefer passing a non-secret --uid value or modifying the script so user.uid does not contain the API key.

Risk: Transcription uses a billed third-party cloud service.

Mitigation: Confirm the account has the needed Volcengine service enabled and that the user accepts the provider's billing terms before processing recordings.

## Reference(s):

- [Volcengine Doubao ASR Flash documentation](https://www.volcengine.com/docs/6561/1631584)
- [Volcengine Speech Console](https://console.volcengine.com/speech/app)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text transcript, JSON response with utterance timestamps, or SRT subtitle file; usage guidance is Markdown with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write transcript or subtitle files when an output path is supplied.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
