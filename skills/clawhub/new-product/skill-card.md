## Description:

This agent skill helps Amazon sellers validate pre-launch product demand by using ARI-collected review data from comparable products to summarize buyer pain points, purchase motives, saturated selling points, trends, competitor gaps, and listing or product-improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to validate a new product idea before launch by analyzing comparable Amazon reviews, competitor weaknesses, demand signals, and evidence-backed listing or product changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits or change future spending and monitoring behavior.

Mitigation: Use pricing-only requests for quotes, set the account to ask before paid actions when needed, and review schedule, watch, competitor, and autoconfirm changes before approval.

Risk: The skill stores and uses an ARI API key on the local machine and sends Amazon review data to ARI services.

Mitigation: Install only when ARI/funewa is trusted for this data, keep API keys out of chats and reports, and revoke or recreate the key if access is no longer needed.

Risk: Review samples, variant coverage, or time windows may be incomplete and can lead to overconfident product decisions.

Mitigation: Report the sample size, site, collection window, and known coverage limits, and treat small samples or short time spans as directional evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/new-product)
- [ARI API reference](artifact/references/reference.md)
- [ARI user guide](artifact/使用说明.md)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI online reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with optional shell commands, report links, and exported CSV, Markdown, or HTML artifacts when supported by the ARI account.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may run ARI workflows that consume credits or change future monitoring settings after the applicable confirmation flow.]

## Skill Version(s):

1.4.7 (source: server release metadata, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
