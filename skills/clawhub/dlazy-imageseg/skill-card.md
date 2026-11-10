## Description:

Separates an image foreground from its background and returns a URL for the transparent result, for product images, portraits, and compositing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill to separate subjects from image backgrounds and retrieve transparent image results for product imagery, portraits, or compositing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports incomplete coverage and a mismatch between the image-matting description and the demonstrated login setup.

Mitigation: Review the CLI’s current help and verify the image-processing flow with a non-sensitive sample before relying on its results.

Risk: The skill requires installing the named CLI and uploading local image paths to dLazy media storage for processing.

Mitigation: Review the pinned @dlazy/cli package and submit only images approved for processing by the dLazy service.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [JSON result containing a hosted URL for a transparent image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented output is an image URL; asynchronous runs may initially return a task identifier without an image.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
