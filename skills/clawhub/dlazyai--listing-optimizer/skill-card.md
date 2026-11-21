## Description:

Creates controlled A/B sets of ecommerce main images, records a single-variable hypothesis for each variant, and provides a template for reviewing results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and listing teams use this skill to create comparable product-image variants, record why each variant may perform better, and prepare a review template for campaign results. Performance metrics must be supplied by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan has incomplete coverage, and its summary notes mismatches and unclear permissions.

Mitigation: Review whether the compliance-checking and repair capabilities and activation phrases fit the intended image-testing task before use.

Risk: Product images may be sent to external image services during generation.

Mitigation: Use only images you are comfortable sharing with the selected service, and avoid sending confidential customer or product material.

Risk: Image variants may imply unsupported product claims, and small or incomplete samples can lead to misleading conclusions.

Mitigation: Check each image for accuracy and platform compliance, record the hypothesis before testing, and avoid drawing conclusions from insufficient data.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider and image-data handling reference](artifact/references/provider-cli.md)
- [Platform compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand kit skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Images, Markdown, Analysis]

**Output Format:** [Generated listing image files with a Markdown A/B test plan and review template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each comparison should vary one selected factor. The user supplies campaign metrics; the skill does not determine statistical significance.]

## Skill Version(s):

1.0.30 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
