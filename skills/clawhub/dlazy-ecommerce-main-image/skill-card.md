## Description:

Generates and edits ecommerce main-image candidates from approved product photos, covering white-background baselines, visual-difference images, content-commerce scenes, color SKU sets, and single-variable A/B test variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and operators use this skill to create main-image generation guidance and dLazy CLI commands from approved product photos. It helps prepare marketplace-ready image candidates and A/B test groups while preserving product facts and platform constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and generated outputs are processed by dLazy cloud endpoints.

Mitigation: Upload only product images the user is allowed to send to dLazy, and avoid sensitive or unauthorized material.

Risk: Authentication stores a dLazy API key locally or uses the DLAZY_API_KEY environment variable.

Mitigation: Keep the key scoped to the intended organization, rely on OS user permissions for local config, and rotate or revoke the key from dLazy when needed.

Risk: Bulk generation can consume credits quickly if parameters or prompts are wrong.

Mitigation: Use dry-run before bulk jobs and verify image size, aspect ratio, and prompt constraints before submitting a batch.

Risk: Generated ecommerce images can accidentally alter product facts or imply unsupported claims.

Mitigation: Compare each output with approved product photos and reject images that change structure, color, quantity, logos, or visual claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with bash commands; dLazy CLI responses are JSON containing generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires approved product images and dLazy authentication; supports dry-run estimation and asynchronous generation.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
