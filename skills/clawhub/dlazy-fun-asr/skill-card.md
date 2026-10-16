## Description:

Helps agents transcribe audio recordings with Fun-ASR, including language selection and speaker diarization for subtitles and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and teams use this skill to turn audio recordings into transcripts for subtitles, transcriptions, and meeting notes, with optional speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files or URLs are sent to dLazy cloud services for transcription.

Mitigation: Only submit recordings you are authorized to share and review the service's data-handling terms.

Risk: Using an external CLI introduces package trust and stored API-key exposure concerns.

Mitigation: Review the CLI package before installing; consider the pinned on-demand npx command or a per-invocation DLAZY_API_KEY instead of persistent setup.

Risk: A documentation example uses a stale --prompt flag for audio transcription.

Mitigation: Check dlazy fun-asr -h and use --audio_url for the recording input.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of the dLazy CLI; transcription results are returned as JSON by the service.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; embedded skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
