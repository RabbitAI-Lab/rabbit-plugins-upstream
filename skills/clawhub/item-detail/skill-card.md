## Description:

Helps ecommerce teams create Chinese-language product-detail image modules from product photos and verified selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and creative teams use this skill to turn product photos and selling points into Chinese-language banners, feature panels, and other product-detail images for review before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and selling-point copy are sent to the chosen cloud image provider.

Mitigation: Choose an approved provider, use dry-run to check the request, and avoid confidential unreleased assets unless provider terms allow them.

Risk: Generated Chinese text or product claims may be incorrect or misleading.

Mitigation: Proofread every image and verify product claims against supplied information before publishing.

## Reference(s):

- [ClawHub item-detail release](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider and CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and commands; generated product-detail image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are produced as separate modules for proofreading and assembly.]

## Skill Version(s):

1.0.21 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
