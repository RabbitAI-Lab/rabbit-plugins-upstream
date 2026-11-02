## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers can convert raster logos, icons, and flat illustrations into scalable color SVG assets through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local images are uploaded to dLazy's hosted service for processing.

Mitigation: Submit only images and prompts you are comfortable sharing with the service.

Risk: Login stores an organization API key in the local CLI configuration.

Mitigation: Use the documented DLAZY_API_KEY environment variable when preferred, and rotate or revoke keys through the organization dashboard.

Risk: Vectorization requests may consume service credits.

Mitigation: Check the dry-run cost estimate and available credits before submitting a request.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [CLI source listed in skill metadata (provenance not server-resolved)](https://github.com/dlazy-ai/cli)
- [npm CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [SVG image asset, JSON result and task status]

**Output Format:** [SVG asset URL and JSON response, with optional local file save]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a generation ID before the asset is ready.]

## Skill Version(s):

1.2.35 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
