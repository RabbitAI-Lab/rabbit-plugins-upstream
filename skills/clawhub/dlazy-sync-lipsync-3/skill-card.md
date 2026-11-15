## Description:

Uses fal.ai sync-lipsync v3 to align a speaker’s lip movements with supplied video and audio for dubbing, localization, and virtual presenters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, localization teams, and developers use the skill to synchronize a speaker’s mouth movements to supplied audio for dubbing, translated video, or virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that CLI login and API-key setup do not clearly match the lip-sync purpose, and that inspection coverage was partial.

Mitigation: Review the CLI authentication flow and credential handling before installation.

Risk: Local video and audio files provided as paths are uploaded to dLazy media storage for processing.

Mitigation: Use only media that is appropriate to send to the hosted service.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video asset with JSON result metadata]

**Output Parameters:** [2D (video and audio inputs)]

**Other Properties Related to Output:** [Returns a result URL; asynchronous runs may return a task ID.]

## Skill Version(s):

1.3.40 (source: target release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
