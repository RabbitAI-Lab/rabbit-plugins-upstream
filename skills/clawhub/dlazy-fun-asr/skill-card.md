## Description:

Transcribes recordings with Alibaba Bailian Fun-ASR, supporting multiple languages, automatic language detection, and speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to transcribe recordings and prepare subtitles or meeting notes, with optional speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recordings may be uploaded to dLazy's hosted service.

Mitigation: Use only recordings approved for cloud processing; avoid sending sensitive audio without authorization.

Risk: The dLazy CLI is a third-party npm dependency.

Mitigation: Review the CLI before installation when supply-chain assurance is required.

Risk: Signing in or setting an API key can store the key locally.

Mitigation: Protect local credentials and remove or revoke the key when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Transcription text or Markdown; the CLI can return JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports automatic language detection and optional speaker diarization.]

## Skill Version(s):

1.3.25 (source: ClawHub release; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
