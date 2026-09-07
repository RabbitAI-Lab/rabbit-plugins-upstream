## Description:

采集指定 Amazon ASIN 的评论，聚焦 1-3 星负面反馈，按频次拆解质量、物流、描述不符和使用困惑等差评根因，并给出降低退货的产品与文案改进建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to analyze low-star reviews for a specific ASIN, identify recurring complaint themes, compare competitors, and turn review evidence into product, listing, monitoring, and response actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auto-confirmed analysis or report generation can spend ARI credits under the account's configured rules.

Mitigation: Set auto-confirm to always ask or request quote-only behavior before running paid review analysis.

Risk: Monitoring and competitor-tracking changes can create recurring review collection activity and related costs.

Mitigation: Approve schedule, ASIN, site, competitor, and cost details explicitly before enabling or changing recurring monitoring.

Risk: Exports can write Amazon review data to local files that may later be shared outside the intended audience.

Mitigation: Use deliberate export locations, inspect exported files before sharing, and avoid including sensitive account or customer context.

Risk: The skill requires an ARI API key and sends Amazon review data to ARI services.

Mitigation: Install only when ARI is trusted for the intended product data, and avoid pasting API keys into chat transcripts or reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/bad-review)
- [Usage guide](artifact/使用说明.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Release changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise natural-language summaries with optional shell commands and report/export links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ASIN and site scope, sample window, report identifiers, report URLs, credit usage, and clear notes when sample size or trend coverage is limited.]

## Skill Version(s):

1.4.7 (source: server release, frontmatter, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
