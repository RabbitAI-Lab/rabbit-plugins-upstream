## Description:

Generates Amazon product listing images and A+ brand content through the dLazy image-generation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce teams use the skill to plan and generate Amazon product detail-page imagery, including main images, secondary images, and A+ modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence notes a mismatch between the Amazon imagery description and the supplied dLazy CLI login operation, and says some referenced material was unavailable for inspection.

Mitigation: Review the linked CLI and package, and confirm its login flow is expected before installing it or providing an API key.

Risk: The skill says prompts are sent to dLazy's hosted service and local media may be uploaded for model processing.

Mitigation: Send only product details and media you are permitted to share with the service; review its handling terms before sending sensitive material.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI project link in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Guidance, Shell commands]

**Output Format:** [Generated image URLs with Markdown planning and delivery summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation depends on product details and access to the dLazy service; input media may be uploaded for model processing.]

## Skill Version(s):

1.3.40 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
