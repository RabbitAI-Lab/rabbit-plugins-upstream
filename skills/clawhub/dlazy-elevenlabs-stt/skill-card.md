## Description:

ElevenLabs scribe_v1 speech-to-text with auto language detection and optional speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to transcribe audio with ElevenLabs scribe_v1 through the dLazy CLI, with optional language selection, speaker diarization, async polling, and saved results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected audio or audio URLs are processed by dLazy-hosted cloud services for transcription.

Mitigation: Use this skill only for recordings approved for cloud processing, and use dry-run when appropriate to inspect the request before submitting it.

Risk: The skill depends on a pinned third-party dLazy CLI and stores API keys in local CLI configuration unless an environment variable is used.

Mitigation: Use the pinned @dlazy/cli@1.2.3 install path, restrict local credential access, and rotate or revoke dLazy API keys from the dashboard when needed.

Risk: The release evidence notes documentation copy-paste inconsistencies around example arguments.

Mitigation: Use the documented --audio_url option and the command help output for real audio transcription requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, Files]

**Output Format:** [JSON responses containing transcription output, task status, or saved result references, usually summarized for the user in concise text or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports audio_url input, language_code selection, optional speaker diarization, dry-run cost checks, async no-wait polling, timeout control, and saving result assets to a local path.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
