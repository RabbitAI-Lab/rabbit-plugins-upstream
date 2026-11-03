## Description:

Generates and edits ecommerce main-image candidates from approved product photos, with guidance for product-accurate compositions and single-variable A/B variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and creative teams use this skill to turn approved product photos into main-image candidates, including white-background baselines, lifestyle scenes, color variants, and controlled A/B sets. Review product accuracy and current marketplace rules before publishing; generated images alone do not guarantee sales.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to dLazy services, and provider data-retention practices are unverified.

Mitigation: Submit only approved images and prompts you are comfortable sending to dLazy.

Risk: The CLI uses an account API key and image-generation requests can incur costs, especially in batches.

Mitigation: Protect the stored key, review generation costs, and use the documented dry-run option to preview batch requests.

Risk: Generated images may alter product details or fall outside current marketplace rules.

Mitigation: Check product accuracy and the target channel’s current image requirements before publishing.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Image candidates, Shell commands, Guidance]

**Output Format:** [Generated image outputs plus Markdown guidance and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image candidates use approved product photos as references and should be reviewed for product accuracy and channel compliance.]

## Skill Version(s):

1.0.28 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
