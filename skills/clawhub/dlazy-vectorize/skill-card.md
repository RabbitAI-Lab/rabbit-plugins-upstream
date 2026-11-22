## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to convert raster logos, icons, and flat illustrations into scalable vector graphics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found login and authentication instructions that do not clearly match the image-conversion purpose.

Mitigation: Check the CLI package and its authentication steps before granting access; use an API key you can rotate or revoke.

Risk: The skill documentation says prompts and supplied local images are sent to dLazy's hosted API and media storage.

Mitigation: Avoid submitting sensitive images or prompts unless you are comfortable processing them through the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, API Calls]

**Output Format:** [JSON result containing a hosted vector image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result may be retrieved asynchronously or downloaded to a local path.]

## Skill Version(s):

1.2.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
