## Description:

Helps Amazon sellers compare competitor reviews across ASINs, identify repeated strengths and weaknesses, and produce competitive analysis reports with positioning and listing recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to collect and compare Amazon review data, generate VOC and competitor reports, monitor review changes and alerts, export review or report files, and plan listing or product improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI receives Amazon review and product-operations data during review analysis, export, paid analysis, and monitoring workflows.

Mitigation: Install and use the skill only when the user trusts ARI to process that data.

Risk: The ARI API key is stored locally and can authorize account actions.

Mitigation: Keep the API key private, avoid including it in reports or command examples, and prefer the documented local configuration or ARI_API_KEY environment variable.

Risk: Setting ARI_ALLOW_CUSTOM_BASE with a custom ARI_BASE_URL can send requests to a non-default destination.

Mitigation: Use the default ARI endpoint unless the user controls the destination and intentionally enables the custom base URL.

Risk: Paid analysis, collection, leaderboard, advice, operations, schedule, watch, or competitor-binding actions may consume credits or create ongoing monitoring costs.

Mitigation: Review quoted costs and require explicit user confirmation before paid or recurring actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-review)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI service](https://ari.funewa.com)
- [ARI API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI report center](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown-style analysis, CLI command guidance, local configuration steps, and exported Markdown, HTML, or CSV files when requested through ARI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid collection, analysis, leaderboard, operations, and advice workflows require explicit user confirmation before execution.]

## Skill Version(s):

1.4.3 (source: server evidence, skill frontmatter, _meta.json, and script constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
