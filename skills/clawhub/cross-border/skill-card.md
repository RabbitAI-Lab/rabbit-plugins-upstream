## Description:

Helps cross-border e-commerce sellers compare Amazon review feedback across eight supported marketplaces to identify localized product, messaging, and listing improvements; requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, marketplace operators, and agent users use this skill to run ARI-backed Amazon review collection, VOC analysis, cross-market comparison, alerts, exports, and product or Listing improvement planning for ASINs across supported sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI API keys are used for authenticated network requests and are stored locally or supplied by environment variable.

Mitigation: Use only the local user configuration or ARI_API_KEY path described by the skill, do not paste keys into reports or examples, and avoid custom ARI endpoints unless the endpoint is intentionally trusted.

Risk: Paid collection, analysis, advice, leaderboard, monitoring, and competitor workflows can consume credits or create ongoing collection costs.

Mitigation: Review the quoted cost and balance details before confirming paid commands, and require explicit user approval before running commands with --confirm or enabling recurring collection.

Risk: Review insights may be incomplete when samples are small, collection windows are narrow, or one side of a competitor comparison lacks enough reviews.

Mitigation: State sample size, site, reporting window, report ID, and credits used in outputs, and label small-sample or incomparable results before giving operational recommendations.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/cross-border)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Report Center](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance and reports, JSON-like CLI responses, and optional CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid collection, analysis, advice, leaderboard, and monitoring-related operations require quoted costs and explicit user confirmation before execution.]

## Skill Version(s):

1.4.3 (source: evidence.json release.version, artifact/SKILL.md frontmatter, artifact/_meta.json, and artifact/scripts/ari.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
