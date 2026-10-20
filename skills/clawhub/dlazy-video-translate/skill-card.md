## Description:

Guides an agent to transcribe and translate video speech, burn in translated subtitles, and optionally add a time-aligned dub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and editors use this skill to guide video transcription, subtitle translation and burn-in, with optional dubbed audio when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video-derived audio and supplied media are uploaded to dLazy for processing.

Mitigation: Use the service only for media you are comfortable uploading.

Risk: CLI authentication can store an API key in local configuration.

Mitigation: Use DLAZY_API_KEY for one-off use if you do not want the key saved locally.

Risk: Transcription, translation and optional per-cue dubbing incur service charges.

Mitigation: Check credit estimates with --dry-run before processing, especially for dubbing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source (declared in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides creation of an MP4 with translated subtitles and SRT files; optionally a dubbed MP4.]

## Skill Version(s):

1.0.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
