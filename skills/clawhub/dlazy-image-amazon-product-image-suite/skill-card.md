## Description:

Creates Amazon product listing image plans and generates main, secondary, and A+ content images through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and e-commerce creative teams use this skill to plan and generate a consistent product detail page image set, including a main image, secondary images, and A+ content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan found an unclear connection between the image-generation purpose and a CLI login command, and it could not inspect some CLI package details.

Mitigation: Review and trust the dLazy CLI and its installation source before installing or logging in.

Risk: The skill describes sending prompts and supplied media to dLazy hosted APIs for processing.

Mitigation: Avoid sending sensitive prompts or media unless that cloud processing is acceptable, and follow the skill’s confirmation flow for each generation step.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI repository listed by the skill](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image assets, Guidance, Markdown]

**Output Format:** [Markdown image plans and generated image URLs or assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image sets can include a main image, secondary images, and A+ content modules; the requested scope determines the deliverables.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
