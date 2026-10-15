## Description:

Guides an agent to synchronize a speaker's lip movements in a video to supplied audio using dLazy's hosted sync-lipsync v3 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, localization teams, and developers use this skill to align a presenter's lip movements with a supplied audio track for dubbing or virtual-presenter videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill delegates execution to an external CLI package.

Mitigation: Review the pinned @dlazy/cli package before installing it.

Risk: Local video and audio files may be uploaded to dLazy's hosted service.

Mitigation: Confirm upload permission and avoid sending sensitive media without authorization.

Risk: Copy-paste errors in the documentation may lead to failed or confusing invocations.

Mitigation: Use the documented video_url and audio_url parameters instead of the mistaken --prompt example, and check the returned media type.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service returns a generated-video URL; the CLI can save the result locally.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; bundled skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
