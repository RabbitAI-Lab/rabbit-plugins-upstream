## Description:

Guides agents in using dLazy's sync-lipsync-3 service to align a speaker's lip movements in a video with supplied audio for dubbing and localization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, localization teams, and developers use this skill to generate lip-synced videos from existing video and audio for dubbing or virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local video and audio files may be uploaded to dLazy's cloud service.

Mitigation: Get permission before uploading media and avoid submitting sensitive files without approval.

Risk: Signing in may save an API key in local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke keys if exposed.

Risk: Some examples describe outdated prompt and image inputs rather than video and audio.

Mitigation: Check `dlazy sync-lipsync-3 -h` and use the documented `--video_url` and `--audio_url` flags.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI project (tool reference; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The external service returns a generated media URL or an asynchronous task ID; the CLI can optionally save the result locally.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
