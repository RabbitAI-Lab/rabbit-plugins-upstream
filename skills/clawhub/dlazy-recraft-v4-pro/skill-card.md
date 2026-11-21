## Description:

Generates 4MP high-resolution raster images for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate high-resolution raster images from prompts for print-ready assets and large-format projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial; the pinned CLI package and some referenced material were not inspected.

Mitigation: Review the pinned @dlazy/cli package and relevant linked material before installing; treat the benign verdict as limited to the scanned files.

Risk: Prompts and supplied local media are sent to dLazy-hosted services.

Mitigation: Send only content approved for that service, and review dLazy's terms and data handling before use.

Risk: Using the skill requires a dLazy API key, which may be saved in the local CLI configuration.

Mitigation: Keep credentials private and rotate or revoke exposed keys through the dLazy organization dashboard.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Raster images, JSON]

**Output Format:** [PNG image with a JSON result envelope and hosted output URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [4MP image generation; selectable aspect ratio; optional asynchronous task ID.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
