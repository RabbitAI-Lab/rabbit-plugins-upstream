## Description:

Guides an agent to synchronize a speaker's lip movements in a video with supplied audio using the dLazy-hosted sync-lipsync-3 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate lip-synced videos for dubbing, localization, and virtual presenters from a source video and audio track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local video and audio files are uploaded to dLazy-hosted endpoints.

Mitigation: Confirm the files are appropriate to upload and trust the dLazy service before submitting them.

Risk: Installing and running the dLazy CLI or exposing an API key may affect the user's environment or account.

Mitigation: Review the pinned CLI package before installation and prefer the documented login flow or a protected API-key environment variable.

Risk: The skill's example uses a --prompt flag that does not match its documented video and audio inputs.

Mitigation: Use the documented --video_url and --audio_url flags and check the CLI help before running.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON results, Video URLs]

**Output Format:** [Markdown guidance and CLI commands; the service returns JSON with a generated media URL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task ID or save the generated media locally.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
