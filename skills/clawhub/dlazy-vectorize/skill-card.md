## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to convert raster images such as logos, icons, and flat illustrations into scalable vector artwork. It sends the image to dLazy's hosted conversion service and returns an asset URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images submitted from local paths are uploaded to dLazy's hosted service.

Mitigation: Submit only images you are comfortable sharing with the service.

Risk: The service requires an API key and may consume organization credits.

Mitigation: Protect the saved key or use the environment-variable option, and review the estimated cost before submitting work.

Risk: The example response shows a PNG MIME type despite the skill's SVG conversion description.

Mitigation: Check current command help and confirm the returned file is SVG before using it as vector artwork.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy website](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Files, URLs, JSON]

**Output Format:** [JSON result containing a generated image asset URL; the intended asset is SVG.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The asset can optionally be saved locally; asynchronous requests may initially return a task identifier. Verify the returned asset format before relying on it.]

## Skill Version(s):

1.2.32 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
