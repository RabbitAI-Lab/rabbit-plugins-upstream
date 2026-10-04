## Description:

Separates an image's foreground from its background and returns a transparent-background image URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to cut out product photos or people for image editing and compositions through the dLazy image segmentation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images supplied to the CLI may be uploaded to dLazy's hosted service.

Mitigation: Only submit media approved for processing by the service.

Risk: Authentication stores a dLazy API key locally.

Mitigation: Protect the local CLI configuration and rotate or revoke keys if compromised.

Risk: The skill's example uses --prompt, but the documented image segmentation option is --image.

Mitigation: Use --image for image input and check the CLI help before running commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI repository (declared in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URLs]

**Output Format:** [JSON response with an image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a transparent-background image URL; optional save downloads the image, while asynchronous requests return a task ID for polling.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
