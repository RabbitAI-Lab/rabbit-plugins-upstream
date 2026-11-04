## Description:

Generate 4 MP raster images suitable for print and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:


## Use Case:

External users can create high-resolution raster artwork from text prompts, choose an aspect ratio, and save generated images for print or large-format design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media are sent to dLazy-hosted services, and local media is uploaded for processing.

Mitigation: Review prompts and files before submission; avoid sending sensitive content unless its use with the service is acceptable.

Risk: Image generation may incur charges.

Mitigation: Use the documented dry-run option to preview the payload and estimated cost before generating.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [PNG raster images and a JSON result containing output links or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image aspect ratio is configurable; images can be saved to a local path.]

## Skill Version(s):

1.3.37 (source: server-resolved release record)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
