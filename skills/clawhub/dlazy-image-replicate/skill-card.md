## Description:

Analyzes a reference image’s composition, colors, lighting, and style, then creates a prompt for generating a similar image with Seedream 4.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and content creators can use this skill to analyze a reference image and generate a new image with a similar visual style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images are sent to the external dLazy service, and the skill relies on an external CLI.

Mitigation: Review the CLI and service details before use, and avoid sending credentials or images you are not comfortable sharing with the service.

## Reference(s):

- [CLI project link in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image URL with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [With asynchronous execution, the result may initially contain a task identifier instead of an image.]

## Skill Version(s):

1.3.44 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
