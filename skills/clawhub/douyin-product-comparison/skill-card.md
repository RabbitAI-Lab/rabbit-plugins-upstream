## Description:

Compares two to five user-selected Douyin products in a sourced table of specifications, price conditions, selling points, and missing information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and product researchers compare selected Douyin listings to assess visible differences and identify details that need verification before choosing a product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unpinned CLI package may change after review.

Mitigation: Pin socialdatax-skills to a reviewed exact version before execution.

Risk: The CLI receives the SOCIALDATAX_API_KEY credential at runtime.

Mitigation: Run only where sharing that key with the reviewed CLI is acceptable.

Risk: Different SKUs or promotional prices can make comparisons misleading.

Mitigation: Label specifications and price conditions separately; do not rank products without comparable evidence.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/douyin-product-comparison)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown comparison table with brief analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links or product IDs, price conditions, missing fields, and follow-up checks.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
