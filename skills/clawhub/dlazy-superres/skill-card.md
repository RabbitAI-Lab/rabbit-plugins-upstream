## Description:

Upscales images through the dLazy service and returns a link to the enhanced image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to improve the clarity and detail of low-resolution images and retrieve an enhanced image URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local images may be uploaded to dLazy, and enhanced images are hosted by dLazy.

Mitigation: Only submit media approved for third-party processing and review access to hosted results.

Risk: Signing in can save a dLazy API key locally.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: The example uses --prompt, although super-resolution requires --image.

Mitigation: Use --image with the image URL or local path and check command help before running.

Risk: Using a global third-party CLI installation retains executable software on the system.

Mitigation: Review the CLI before installation and prefer the pinned npx invocation when a global install is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and JSON result containing an enhanced image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the image locally or return an asynchronous task ID.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
