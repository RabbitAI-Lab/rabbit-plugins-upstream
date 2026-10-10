## Description:

Transcribes audio recordings with Fun-ASR for subtitles, transcripts, and meeting notes, with language detection and speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing subtitles, transcripts, or meeting notes can submit selected audio recordings for cloud transcription and optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected recordings and prompts are sent to dLazy cloud services.

Mitigation: Confirm the material is suitable for upload; use explicit file paths or --dry-run to review what will be submitted.

Risk: CLI authentication saves an API key on the local device.

Mitigation: Use a per-run DLAZY_API_KEY instead if local key storage is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI project linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and JSON transcription results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include speaker labels; asynchronous tasks may initially return a task ID.]

## Skill Version(s):

1.3.27 (source: server-resolved ClawHub release; source frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
