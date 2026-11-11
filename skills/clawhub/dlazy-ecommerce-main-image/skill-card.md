## Description:

Guides ecommerce sellers in planning main-image candidates from approved product photos and creating controlled single-variable A/B test variants with dLazy CLI examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and creative teams use the skill to plan accurate marketplace main images, keep product details tied to approved photos, and prepare one-variable image tests across marketplace channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a benign verdict with medium confidence and partial coverage; it flagged that observed behavior appears to run dLazy login rather than the described image workflow.

Mitigation: Before installation, check that the observed CLI login behavior fits your needs and review the setup and account requirements.

Risk: The documented workflow sends prompts to dLazy and uploads local reference images to its hosted media service.

Mitigation: Use only approved product photos and review the prompts and images before sending them to the service.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)

## Skill Output:

**Output Type(s):** [Image outputs, Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance and shell command examples; generated image results are provided as hosted image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image candidates use approved product photos as references; the skill describes single-variable A/B variants and does not guarantee sales outcomes.]

## Skill Version(s):

1.0.30 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
