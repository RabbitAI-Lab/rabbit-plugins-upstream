## Description:

Transcribes recordings with Fun-ASR for subtitles and meeting notes, with language selection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to transcribe recordings for subtitles, transcripts, and meeting notes, optionally identifying speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected recordings may contain sensitive voices or confidential content and are uploaded to dLazy-hosted services.

Mitigation: Confirm permission to share the audio and review dLazy data-handling terms before uploading.

Risk: Installing the CLI or saving an API key locally may persist software or credentials on the device.

Mitigation: Review the pinned @dlazy/cli package before installation; use npx for on-demand execution and a per-invocation DLAZY_API_KEY to avoid a saved key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Transcript text or Markdown; CLI results are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker labels; asynchronous requests can return a task ID before results are available.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release; bundled frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
