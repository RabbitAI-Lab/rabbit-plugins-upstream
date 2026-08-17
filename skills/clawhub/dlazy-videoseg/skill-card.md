## Description:

Creates same-length black-and-white human segmentation mask videos for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and video workflow agents use this skill to submit a video to dLazy and receive a mask video for compositing or matting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos passed to the command may be uploaded to dLazy's hosted service for processing.

Mitigation: Use only media approved for hosted processing and review dLazy service terms before submitting sensitive videos.

Risk: Login may save a dLazy API key in the local CLI configuration.

Mitigation: Use npx or DLAZY_API_KEY for less persistent setup when appropriate, and rotate or revoke the key from dLazy if needed.

Risk: Generated outputs are returned as URLs hosted by dLazy media storage.

Mitigation: Treat returned URLs as hosted artifacts and avoid sharing confidential outputs unless approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON responses containing hosted output URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local video paths may be uploaded to dLazy media storage for processing.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
