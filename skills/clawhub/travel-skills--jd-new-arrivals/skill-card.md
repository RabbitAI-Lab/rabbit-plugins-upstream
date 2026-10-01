## Description:

Queries newly listed JD self-operated products, with filtering by category, price, discount, and minimum favorable review rate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping assistants use this skill to find recently listed JD self-operated products, compare effective prices and discounts, and retrieve purchase links for further review. It provides product information only and does not place orders or modify account data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping queries and filter parameters are sent to the configured Tencent SCF proxy.

Mitigation: Install only if comfortable with that proxy path; keep PROXY_URL pointed at the intended trusted service and treat PROXY_TOKEN as a scoped service credential.

Risk: Product data and purchase links are informational and may become stale or inaccurate.

Mitigation: Review product details on JD before purchase decisions; the skill does not place orders or change account data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/jd-new-arrivals)
- [JD self-operated super deals companion skill](https://clawhub.ai/cn-shopping/jd-super-deals)
- [JD self-operated historical lowest price companion skill](https://clawhub.ai/cn-shopping/jd-lowest-price)
- [Shopping price comparison companion skill](https://clawhub.ai/cn-shopping/best-price)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [JSON string containing a summary and product item data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product names, prices, discounts, ratings, images, shop details, and purchase links.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
