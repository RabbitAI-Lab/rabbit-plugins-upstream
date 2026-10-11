## Description:

Transcribes and translates video speech, burns translated subtitles into a video, and optionally adds a synchronized dubbed audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and editors use this skill to translate video dialogue into timed subtitles and, when requested, produce a dubbed video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video or audio is sent to dLazy for cloud processing and may contain sensitive material.

Mitigation: Only submit media approved for external processing; review the selected content before running the skill.

Risk: Cloud transcription, translation, and optional per-cue dubbing can incur usage-based charges.

Mitigation: Review estimated charges with --dry-run where available before processing, especially for dubbing.

Risk: Saved or exposed API credentials can permit access to the user's dLazy organization.

Mitigation: For sensitive media or shared machines, prefer DLAZY_API_KEY over saved login credentials and rotate or revoke any exposed key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source (declared in skill metadata; release import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [SRT subtitles and MP4 video, with optional dubbed audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a subtitled MP4 and timed SRT; a dubbed MP4 is produced only when requested.]

## Skill Version(s):

1.0.19 (source: ClawHub server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
