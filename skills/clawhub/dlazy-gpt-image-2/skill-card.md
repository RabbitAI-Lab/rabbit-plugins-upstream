## Description:

Generate and edit images with GPT Image 2 from text prompts and reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers use this skill to generate images from text prompts or edit and synthesize images with up to five reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference media may be sent to dLazy services during generation.

Mitigation: Submit only prompts and media you are comfortable sending to those services.

Risk: ClawScan noted that the relationship between the image workflow and `dlazy login` is unclear, and that some service and installation details could not be resolved.

Mitigation: Review the CLI authentication and installation steps and confirm they match the intended workflow before use.

## Reference(s):

- [dLazy CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Image files with a JSON result containing image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional reference images; configurable size, format, and quality; supports asynchronous generation.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
