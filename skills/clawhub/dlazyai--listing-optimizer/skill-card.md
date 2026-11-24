## Description:

Creates controlled main-image A/B variants from product images and selling points, records a hypothesis for each variant, and provides a template for reviewing results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers use the skill to compare product-listing main images while changing one visual variable at a time. It records the expected effect and provides a review table for users to fill with their own listing results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and noted a mismatch between the A/B testing purpose and the reported listing checker, so its review may not cover all behavior or confirm marketplace acceptance.

Mitigation: Review generated images and checker results against the current official marketplace requirements before publishing; treat the checker as a screening aid.

Risk: Broad activation phrases may start the workflow for an ambiguous request, and image generation uses an external provider.

Mitigation: Confirm the requested metric and experiment before generating, and use only product images and details you are comfortable sending to the selected provider.

Risk: A generated image could misrepresent the listed product and distort experiment results.

Mitigation: Inspect each variant for product accuracy and avoid claims or visual changes that overstate the item.

## Reference(s):

- [Platform image specifications](artifact/references/platform-specs.md)
- [Image provider CLI reference](artifact/references/provider-cli.md)
- [Platform compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand kit skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Image files, Markdown, Guidance]

**Output Format:** [Generated image variants with written hypotheses and a Markdown experiment review template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Users supply listing performance data; the skill does not connect to marketplace analytics or determine statistical significance.]

## Skill Version(s):

1.0.31 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
