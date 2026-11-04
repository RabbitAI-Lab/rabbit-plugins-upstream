## Description:

Generate cinematic videos with Google Veo 3.1 from text prompts and images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short cinematic videos from prompts and reference images, or extend an existing video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image or video inputs are sent to dLazy, and generation can spend account credits.

Mitigation: Submit only material you intend to share; use the dry-run option to review the payload and cost estimate before generation.

Risk: The CLI stores an API key locally, and the external CLI and hosted service have not been fully audited.

Mitigation: Review the pinned CLI before installation and use the documented DLAZY_API_KEY environment variable if you prefer not to save the key in the local config.

## Reference(s):

- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Hosted video asset with JSON generation metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-video, image-guided generation, and video extension; outputs can be saved locally.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
