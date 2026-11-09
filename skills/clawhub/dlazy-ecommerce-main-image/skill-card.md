## Description:

Creates e-commerce listing image candidates and controlled A/B test sets from approved product photos while preserving product facts and channel rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and marketing teams use this skill to create listing-image candidates from approved product photos, including white-background, lifestyle, color-variant, and visual-difference options. It also helps prepare single-variable A/B test sets for marketplace listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local product photos are sent to dLazy-hosted services for generation.

Mitigation: Use only approved images and prompts suitable for hosted processing.

Risk: The security review was partial, and use requires the dLazy CLI login flow.

Mitigation: Review unresolved referenced materials and the CLI login flow before installing and using the skill.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)

## Skill Output:

**Output Type(s):** [Images, Prompts, Shell commands, Guidance]

**Output Format:** [Generated image URLs and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image candidates are generated remotely; verify product details and marketplace requirements before use.]

## Skill Version(s):

1.0.29 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
