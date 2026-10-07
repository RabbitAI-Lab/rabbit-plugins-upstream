## Description:

Transcribes video, translates and burns in subtitles, and optionally adds a timing-aligned dubbed audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and editors use this skill to translate video speech into timed subtitles and, when requested, produce a dubbed video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media is uploaded to dLazy for processing.

Mitigation: Send only media you are comfortable sharing with dLazy.

Risk: API-backed transcription, translation, and dubbing may incur charges.

Mitigation: Review cost estimates with dry-run before paid calls.

Risk: The CLI can store an API key locally and requires installing a third-party package.

Mitigation: Review the pinned CLI package before installation; use a one-off DLAZY_API_KEY when local key storage is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source (skill metadata link; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files]

**Output Format:** [MP4 video and SRT subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Burned-in translated subtitles; optional timing-aligned dub track.]

## Skill Version(s):

1.0.17 (source: ClawHub release evidence; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
