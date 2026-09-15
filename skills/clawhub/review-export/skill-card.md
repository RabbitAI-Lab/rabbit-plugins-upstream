## Description:

review-export helps agents use ARI to collect Amazon reviews for a specified ASIN, export review CSV files, and produce Markdown or HTML review analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and operators use this skill to ask an agent for Amazon review collection, CSV export, VOC analysis, competitor comparison, trend review, and report export through ARI. It is suited to customer feedback analysis and BI workflows where users need review data and concise operational recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a user's ARI account, store an API key locally, contact ari.funewa.com, export files, and manage ARI review workflows.

Mitigation: Install only if those account and local-file permissions are acceptable, keep API keys out of chat and reports, and review schedule, watch, competitor, and autoconfirm changes before approving them.

Risk: Some ARI analysis flows may spend ARI credits automatically under server-controlled auto-confirm rules.

Mitigation: Tell the agent "只报价，不执行" for quote-only use or "以后每次扣点前先问我" before analysis when every credit-spending action should require confirmation.

Risk: Review analyses and trend claims depend on the ARI-collected sample and may not cover all Amazon reviews, all variants, or enough history for a reliable trend.

Mitigation: Report the sample scope, review window, and limitations with conclusions, and avoid treating limited samples or newly imported old reviews as current trends.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-export)
- [ARI CLI and API reference](references/reference.md)
- [User guide](使用说明.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with optional JSON or CSV file exports from ARI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save CSV, Markdown, or HTML exports locally and may include ARI report links when returned by the service.]

## Skill Version(s):

1.4.11 (source: server release evidence, frontmatter, _meta.json, and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
