## Description:

Guides an agent through transcribing and translating video, burning in subtitles, and optionally adding a timed dubbed audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and editors use this skill to translate a video's speech into timed subtitles and, when requested, a dubbed track. The workflow produces a subtitled MP4 and SRT files, with an optional dubbed MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media and generated text are sent to dLazy services.

Mitigation: Obtain permission before uploading sensitive video or audio and review dLazy's service terms.

Risk: Transcription, translation and optional per-cue dubbing use billable API credits.

Mitigation: Check the estimate with dry-run where available and confirm whether dubbing is needed before making paid calls.

Risk: The translation example defaults to Simplified Chinese, which may not match the requested language.

Mitigation: Confirm the target language before translation and adjust the prompt accordingly.

## Reference(s):

- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage and service terms](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and commands; generated MP4 video and SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dubbed audio is optional and generated only when requested.]

## Skill Version(s):

1.0.21 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
