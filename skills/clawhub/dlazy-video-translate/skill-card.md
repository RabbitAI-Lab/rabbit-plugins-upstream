## Description:

Transcribes a video, translates its subtitles, burns them into the video, and optionally adds a timing-fitted dubbed audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and media teams use it to produce translated, subtitled MP4 videos with SRT files, optionally adding a dubbed audio track fitted to the original timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence flags possible silent replacement of existing files and a mismatch between the stated filesystem boundary and credential storage; it describes a review flag, not malicious intent.

Mitigation: Review file replacement behavior and credential storage before installation; use a dedicated working directory or copies, and confirm where credentials are stored.

## Reference(s):

- [dlazy CLI project page (metadata homepage)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dlazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files (MP4), Subtitle files (SRT)]

**Output Format:** [Translated MP4 video with SRT subtitle files; optionally a dubbed MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Subtitle language follows the user's request; dubbing is optional.]

## Skill Version(s):

1.0.34 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
