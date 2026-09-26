## Description:

录音转写 Fun ASR transcribes audio with Alibaba Bailian Fun-ASR, supporting Chinese, English, language detection, and speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit audio URLs or local audio files to dLazy's hosted Fun-ASR workflow for transcription, subtitles, and meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files, supplied URLs, and task parameters are processed by dLazy cloud services.

Mitigation: Review dLazy's CLI and service terms before use, and avoid sending sensitive audio unless the intended cloud processing is approved.

Risk: The dLazy API key may be saved in the local CLI configuration.

Mitigation: Rely on OS user permissions, rotate or revoke keys when needed, and use the DLAZY_API_KEY environment variable for per-invocation credentials when preferable.

Risk: The artifact example shows --prompt even though the security guidance says to use --audio_url for transcription.

Mitigation: Invoke transcription with --audio_url and set --language_code explicitly when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI homepage and source](https://github.com/dlazy-ai/cli)
- [dLazy service homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Files, Configuration guidance]

**Output Format:** [JSON response with transcription output and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication; asynchronous runs can return a task identifier for polling.]

## Skill Version(s):

1.3.20 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
