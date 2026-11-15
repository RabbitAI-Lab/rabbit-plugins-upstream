## Description:

Generates 4MP high-resolution raster images suitable for print-ready assets and large-scale use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate high-resolution raster images from text prompts, choose an aspect ratio, and save the resulting image locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign but incomplete and flags the authentication steps, pinned CLI installation details, and a whitespace finding for review.

Mitigation: Review the authentication flow, pinned @dlazy/cli version, and flagged whitespace before use.

Risk: Prompts and local media supplied to the skill are sent to dLazy's hosted service, and input files are uploaded for processing.

Mitigation: Send only prompts and files that are appropriate to share with the hosted service.

## Reference(s):

- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [PNG image assets with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 4MP; aspect ratio is selectable.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata; artifact frontmatter: 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
