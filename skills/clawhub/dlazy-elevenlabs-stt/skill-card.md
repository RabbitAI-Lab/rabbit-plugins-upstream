## Description:

ElevenLabs scribe_v1 speech-to-text with auto language detection and optional speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external users use this skill to invoke dLazy's ElevenLabs speech-to-text wrapper for audio transcription, optional speaker diarization, subtitle preparation, and meeting-note workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a third-party SaaS CLI and may send prompts, parameters, and audio inputs to dLazy endpoints.

Mitigation: Use it only with audio files or URLs you are comfortable uploading to dLazy and review the dLazy CLI source or package provenance before installation if you do not already trust it.

Risk: Authentication can persist a dLazy API key in the local user configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when you do not want the key stored on disk, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Global installation of the dLazy CLI adds a persistent executable to the user environment.

Mitigation: Prefer npx or an isolated environment over a global install when evaluating or limiting exposure.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy product site](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, JSON, Guidance]

**Output Format:** [Markdown instructions with bash examples and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local or remote audio inputs, automatic language selection between zh and en, optional speaker diarization, asynchronous task polling, and saving returned assets.]

## Skill Version(s):

1.3.16 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
