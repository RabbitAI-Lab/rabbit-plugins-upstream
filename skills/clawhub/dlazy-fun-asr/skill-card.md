## Description:

Transcribes audio recordings with Alibaba Bailian Fun-ASR, supporting Chinese, English, and other languages, automatic language detection, and speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users who need to turn recordings into transcripts, subtitles, or meeting notes can submit audio for multilingual transcription and optionally request speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and did not inspect the external CLI package implementation; it also flagged the CLI login flow and incomplete evidence connecting the commands to transcription.

Mitigation: Before installing, review what `dlazy login` does and confirm the CLI is the service you intend to use. Avoid entering credentials unless you trust that service.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy service website](https://dlazy.com)
- [CLI source repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON transcription result containing generated output or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Speaker diarization and audio event tags are optional; asynchronous tasks can return a task ID, and result assets can be saved locally.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
