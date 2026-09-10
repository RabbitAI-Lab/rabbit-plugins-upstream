## Description:

Extracts evidence-backed user use cases, constraints, and experience signals from Amazon reviews and product details through ARI review-analysis workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to turn ARI-collected review and product-detail evidence into use-case reports, constraints, trends, and product-improvement opportunities. It is scoped to evidence-based product operations and excludes unsupported demographic inference, ad bidding, and ungrounded marketing claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an ARI account and stores an ARI API key on the local machine.

Mitigation: Install only for users comfortable with ARI account access, use the browser authorization flow or approved local configuration, and do not share API keys in chat or reports.

Risk: Some workflows can spend ARI credits or use account auto-confirmation rules.

Mitigation: Set auto-confirm to off when every paid action should require approval, use quote-only flows for pricing checks, and proceed with paid runs only after clear user confirmation or documented account rules.

Risk: Natural-language requests can lead to persistent changes such as schedules, watches, competitor tracking, exports, or workbench status updates.

Mitigation: Review requests before creating or changing monitoring, competitor tracking, exports, or workbench state, and keep read-only checks separate from management actions.

Risk: Outputs may be over-read if review samples, collection windows, variants, or marketplace coverage are limited.

Mitigation: Report the data range, sample limits, site, ASIN, and evidence basis, and avoid unsupported demographic claims, ad-bidding claims, or ungrounded marketing promises.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/use-case-miner)
- [README](artifact/README.md)
- [Operation workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [User guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise text or Markdown reports, with CLI commands and configuration guidance when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report links and, when requested and permitted by the ARI account, exported Markdown, HTML, or CSV files.]

## Skill Version(s):

1.4.8 (source: server release, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
