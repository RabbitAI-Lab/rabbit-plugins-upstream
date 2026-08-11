## Description:

Generate high-quality images with Vidu Q2, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Vidu Q2 image-generation service from an agent workflow, producing images from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image paths may be sent to dLazy's hosted API.

Mitigation: Use the skill only when cloud processing by dLazy is acceptable for the prompt content and selected files.

Risk: Local files passed as image, video, or audio inputs may be uploaded to dLazy media storage.

Mitigation: Review file paths before invocation and avoid passing confidential or regulated files unless the user's policy permits that upload.

Risk: The dLazy CLI may store an API key locally for future billable use.

Mitigation: Authenticate with an organization-scoped key, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation environment variables where persistent storage is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [JSON containing generated image URLs or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted image URLs, or a generation ID when invoked asynchronously.]

## Skill Version(s):

1.3.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
