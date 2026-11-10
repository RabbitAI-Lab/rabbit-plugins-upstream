## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to convert raster logos, icons, and flat illustrations into scalable vector images. It sends an image to dLazy's hosted service and returns a URL for the generated asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial: some referenced paths or components were unavailable, and the review flagged authentication commands and whitespace padding.

Mitigation: Review the CLI setup and authentication guidance and inspect the available implementation before installing or running it.

Risk: Images provided as local paths are uploaded to dLazy media storage, and prompts are sent to its hosted API.

Mitigation: Only submit images and prompts that are appropriate to share with the hosted service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [SVG image, URL]

**Output Format:** [JSON result containing a hosted output asset URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated vector image is hosted on files.dlazy.com; asynchronous runs can return a task ID.]

## Skill Version(s):

1.2.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
