## Description:

Guides agents in using dLazy's CLI to synchronize a speaker's lip movements in a video with supplied audio for dubbing and localization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide audio-to-video lip synchronization for dubbing, localization, and virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external CLI and submitting local video or audio can expose selected media to dLazy cloud services.

Mitigation: Review and trust the CLI package before installing; upload only media you are comfortable sending to dLazy.

Risk: The skill's prompt example and image output example do not match the lip-sync video workflow.

Mitigation: Use --video_url and --audio_url and expect a video result rather than relying on those examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI project (skill metadata homepage)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The external service returns a generated video URL; asynchronous requests may return a task ID.]

## Skill Version(s):

1.3.27 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
