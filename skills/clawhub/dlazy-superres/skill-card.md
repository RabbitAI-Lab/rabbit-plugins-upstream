## Description:

Enhances low-resolution images and returns a URL for the upscaled result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to upscale low-resolution images through dLazy's hosted service and retrieve an enhanced image URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and media are uploaded to dLazy's hosted service.

Mitigation: Send only media approved for processing by an external service.

Risk: The skill installs and runs an external CLI and stores a dLazy API key.

Mitigation: Review the CLI before installation, use the on-demand npx option if preferred, and rotate or revoke the key when needed.

Risk: The documented example uses --prompt, but the listed super-resolution option is --image.

Mitigation: Check dlazy superres -h and pass the supported image option before running a request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URL, Image file (optional)]

**Output Format:** [JSON response with an enhanced-image URL; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of an image URL until complete.]

## Skill Version(s):

1.3.24 (source: ClawHub release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
