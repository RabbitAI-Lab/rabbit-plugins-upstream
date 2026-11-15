## Description:

Guides agents in creating ecommerce product-image candidates and single-variable A/B test sets from approved product photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and creative teams use the skill to prepare product-image candidates from approved product photos, including white-background, scene, color-variant, and visual-difference images. It also guides single-variable image tests and checks that generated images preserve product facts and meet the selected channel's requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found incomplete evidence and an unresolved mismatch between the image-generation purpose and the CLI login step.

Mitigation: Before installing, check that the login step and account requirements fit the image workflow, and review that prompts and local product photos are sent to dLazy services for generation.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Generated product-image candidates and Markdown guidance with inline Bash CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image candidates are generated from user-provided product photos; A/B groups and color variants require repeated image-generation requests.]

## Skill Version(s):

1.0.31 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
