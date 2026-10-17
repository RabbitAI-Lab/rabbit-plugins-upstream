## Description:

Guides ecommerce sellers in creating product-image candidates and single-variable A/B variants from approved product photos while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and creative teams use this skill to prepare compliant product main-image concepts, color variants, and controlled A/B tests for online storefronts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts are sent to a third-party hosted service.

Mitigation: Upload only approved photos that you are authorized to share with dLazy.

Risk: The locally stored API key could be disclosed or misused.

Mitigation: Protect the credential like any other service key and rotate or revoke it if compromised.

Risk: Generated images may misrepresent product details or violate marketplace image rules.

Mitigation: Compare each output with the approved SKU photos and check the target channel's current rules before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with bash commands and JSON image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images require product-accuracy and channel-rule review before publication.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
