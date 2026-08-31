## Description:

Transcribes audio with Alibaba Bailian Fun-ASR, supporting Chinese, English, multiple languages, automatic language recognition, and speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Fun-ASR audio transcription workflow for subtitles, meeting notes, and other transcript generation tasks. It is useful when an agent needs to prepare or run CLI commands for cloud-based audio transcription with optional language selection and speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio content may be uploaded to the dLazy cloud service for transcription.

Mitigation: Use the skill only with audio the user is comfortable sending to the third-party service, and review the configured endpoints before execution.

Risk: A saved dLazy API key can remain in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-run authentication when persistent credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact includes a stale prompt-based example that does not match the documented audio transcription flags.

Mitigation: Prefer the documented fun-asr options such as --audio_url, --language_code, --diarize, and --num_speakers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON CLI responses with transcription outputs, plus Markdown guidance and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task identifiers when --no-wait is used; local audio paths may be uploaded to dLazy media storage for transcription.]

## Skill Version(s):

1.3.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
