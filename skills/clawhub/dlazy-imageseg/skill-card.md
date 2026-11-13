## Description:

Image matting tool: separates foreground from background and returns a transparent-background URL for product image processing, character cutout, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and image-processing users can submit an image for foreground separation and use the returned transparent-background image URL in product photography, character cutouts, or compositing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the image-processing description is not demonstrated by the supplied command material, and the referenced external CLI was not assessed.

Mitigation: Review the CLI package and confirm its image-processing behavior and image data handling before installing it or submitting images.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Image, JSON, URL]

**Output Format:** [JSON result containing a URL to the transparent-background image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The image result is hosted by dLazy; asynchronous requests may return a task identifier before the result is ready.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
