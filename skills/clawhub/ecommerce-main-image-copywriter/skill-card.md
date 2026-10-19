## Description:

Creates product main-image headlines, supporting copy, selling points, and visual suggestions from supplied product details or supported Douyin and Xiaohongshu product listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketing teams use this skill to draft evidence-based product main-image copy and visual suggestions from their product information or supported product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookups invoke an unpinned npm CLI with access to the SocialDataX API key.

Mitigation: Review and pin the package or use a trusted preinstalled CLI, and scope the API key to this service.

Risk: Product claims or changing prices may be inaccurate if source details are incomplete or outdated.

Mitigation: Use only supplied or retrieved product facts, flag missing details, and verify prices and promotional conditions before publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/ecommerce-main-image-copywriter)
- [SocialDataX product data service](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown table with copy variations and visual suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically three variations with headlines, subtitles, up to three selling points each, source facts, and items to verify; no image files.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
