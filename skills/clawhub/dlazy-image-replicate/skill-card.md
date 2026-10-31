## Description:

Analyzes a reference image’s composition, colors, lighting, and style, then creates a prompt and uses Seedream 4.5 to generate a similar image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams can use this skill to create new images guided by a reference image’s visual style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are sent to dLazy, and local image files are uploaded to its media storage.

Mitigation: Use only images and prompts you are comfortable sharing with the service; avoid sensitive or confidential material.

Risk: Image generation can incur paid usage.

Mitigation: Run with --dry-run and review the cost estimate before submitting a generation request.

Risk: The CLI can persist an API key in a local configuration file.

Mitigation: Protect the local config, use a key you can rotate, and revoke it if exposed.

Risk: Installing the external npm CLI requires trusting that package.

Mitigation: Review the CLI package and install only if you trust it; the skill specifies version 1.2.3.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Text, JSON]

**Output Format:** [Generated image with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may run asynchronously; output images are hosted by dLazy.]

## Skill Version(s):

1.3.37 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
