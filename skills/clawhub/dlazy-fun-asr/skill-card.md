## Description:

Transcribes recording files with Alibaba Bailian Fun-ASR, supporting Chinese, English, other languages, automatic language detection, and speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Fun-ASR CLI for cloud transcription of audio recordings into subtitles, transcripts, and meeting-note workflows. It is suited for agent workflows that can provide an audio URL or local audio path and use a dLazy API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files and request data passed to the CLI can be uploaded to dLazy hosted infrastructure.

Mitigation: Use the skill only for recordings approved for dLazy cloud processing, and avoid sensitive recordings unless that matches the user's privacy requirements.

Risk: A dLazy API key may be saved in the user's local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return completed JSON outputs or an asynchronous generateId for later polling.]

## Skill Version(s):

1.3.8 (source: ClawHub release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
