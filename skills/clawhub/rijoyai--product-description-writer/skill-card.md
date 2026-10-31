## Description:

Generates SEO-optimized product descriptions for e-commerce stores from product specs, rough notes, feature lists, or competitor listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rijoyai](https://clawhub.ai/user/rijoyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce merchants, marketers, and operators use this skill to turn product details into product page copy, including SEO titles, descriptions, benefit-led bullets, meta descriptions, hooks, and mobile formatting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated product copy may include unsupported health, beauty, certification, or performance claims.

Mitigation: Review claims against source product evidence before publication, especially for regulated categories.

Risk: Helper scripts can read and write local files specified by the user.

Mitigation: Run helper scripts only with intended input and output paths, and review generated files before use.

Risk: The skill may activate for product-spec or competitor-listing rewrite requests where claims could be copied or overstated.

Mitigation: Confirm the requested output is product-page copy and verify that rewritten claims remain accurate and supportable.

## Reference(s):

- [Copy Patterns & Templates](references/copy_patterns.md)
- [Product Description Writer ClawHub release](https://clawhub.ai/rijoyai/skills/product-description-writer)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with titled sections, benefit-led bullets, SEO metadata, and optional formatting notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default description length is 300-500 words; default outputs include an SEO title, product description, highlights, and meta description.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
