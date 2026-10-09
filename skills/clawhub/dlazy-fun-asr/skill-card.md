## Description:

Transcribes recordings with Fun-ASR, with multilingual recognition and optional speaker diarization for subtitles and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating subtitles, transcripts, or meeting notes can submit recordings for speech recognition and optional speaker diarization through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected recordings are uploaded to a third-party hosted service.

Mitigation: Submit only recordings approved for cloud processing and avoid sensitive audio unless authorized.

Risk: Installing and running the third-party CLI and storing a service API key expose software and credentials.

Mitigation: Review the pinned CLI package before running it, use on-demand installation if preferred, and keep API keys revocable.

Risk: Saving returned assets to an unintended path can disclose or overwrite local data.

Mitigation: Check the destination before using the --save option, especially with sensitive files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON response containing transcription output; text can be used for subtitles or notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization; asynchronous tasks may return an identifier for later retrieval.]

## Skill Version(s):

1.3.26 (source: ClawHub release evidence; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
