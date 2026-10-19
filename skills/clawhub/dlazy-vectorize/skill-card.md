## Description:

Helps agents convert raster images to vector assets with dLazy and retrieve hosted result URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to submit PNG or JPEG images for vectorization and retrieve a hosted result URL or save the returned asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts supplied to the dLazy CLI may be uploaded to dLazy's hosted service.

Mitigation: Use the service only when permitted to share the inputs; avoid private images, confidential prompts, and sensitive local paths.

Risk: The documentation claims SVG conversion but shows a PNG result.

Mitigation: Check the returned MIME type and downloaded file before relying on vector output.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and JSON result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted result can be saved locally; verify the returned asset type before assuming it is SVG.]

## Skill Version(s):

1.2.30 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
