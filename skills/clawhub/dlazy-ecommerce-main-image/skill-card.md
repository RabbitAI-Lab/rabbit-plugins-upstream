## Description:

Generates and edits ecommerce product main-image candidates from approved product photos, including white-background baselines, lifestyle scenes, color variants, and single-variable A/B sets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and product marketers use the skill to create product-image candidates from approved product photos, prepare consistent color and scene variants, and plan single-variable image tests while checking that product details remain accurate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts are sent to dLazy services for image generation, and API access uses an organization key.

Mitigation: Upload only images you are authorized to use, protect the saved organization API key, and revoke it when it is no longer needed.

Risk: Generated candidates may not preserve product details or may not satisfy the target marketplace's current image rules.

Mitigation: Review each candidate against the approved product photo and the marketplace's current requirements before publishing.

Risk: Batch image generation can use credits.

Mitigation: Review credit estimates before batch generation.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy CLI source repository (listed in the skill documentation)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Generated image URLs and Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image candidates are based on approved product photos; the skill does not guarantee sales performance.]

## Skill Version(s):

1.0.26 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
