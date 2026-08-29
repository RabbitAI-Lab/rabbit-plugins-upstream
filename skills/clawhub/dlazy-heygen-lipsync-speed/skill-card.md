## Description:

HeyGen Lipsync Speed is a dLazy-hosted fast lip-sync skill for generating lip-synced media from video and audio inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted HeyGen Lipsync Speed API from an agent workflow, supplying video and audio inputs and receiving generated lip-sync result URLs or saved media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected media files and request parameters are sent to dLazy's hosted API and media storage.

Mitigation: Review media sensitivity before running the skill and use only files appropriate for third-party processing.

Risk: The dLazy CLI can store a revocable API key in the local user configuration.

Mitigation: Use the per-run DLAZY_API_KEY environment variable when persistent local storage is not acceptable, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI command guidance and JSON API result containing hosted media URLs; optional saved media file via --save.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; uploads user-selected video and audio files to dLazy endpoints; async tasks can return a generateId for polling.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
