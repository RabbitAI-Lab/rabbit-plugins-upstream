## Description:

Image matting tool: separates foreground from background and returns transparent background URL, suitable for product image processing, character cutout, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use the skill to remove image backgrounds from product or people images and receive a transparent image for composition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags a mismatch between the image-processing purpose and the documented login/authentication commands.

Mitigation: Review the authentication and install steps and the linked CLI repository before installing or entering credentials.

Risk: The skill documentation says local image files are uploaded to dLazy media storage for processing.

Mitigation: Only provide images you are authorized to send to the hosted service.

## Reference(s):

- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, URLs, JSON]

**Output Format:** [JSON result with a URL to the transparent image asset]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The image asset is hosted by dLazy; local image paths supplied to the CLI are uploaded for processing.]

## Skill Version(s):

1.3.39 (source: server-resolved release; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
