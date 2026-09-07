## Description:

亚马逊评论趋势监控 tracks Amazon review volume, rating, sentiment, and complaint topics over time to identify reputation inflection points and warn about quality or competitor-impact changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and marketplace analysts use this skill to monitor ASIN review trends, surface rating or sentiment shifts, compare competitors, and turn review evidence into reports or operational guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credit-backed analysis or collection commands may spend ARI credits, including account-approved auto-confirmed flows.

Mitigation: Use quote-only requests for estimates, set the account to ask before each paid action when desired, and require explicit confirmation before commands that report confirmationRequired.

Risk: Persistent approval settings can change whether future paid actions ask before spending credits.

Mitigation: Review and reset the autoconfirm setting before production use, and document any account-level spending threshold for operators.

Risk: Monitoring and competitor bindings can create continuing review collection activity and future costs.

Mitigation: Create, resume, or change monitoring schedules only after the user confirms the ASIN, cadence, eligibility, and cost note returned by the service.

Risk: Exports can write review CSV or report files to local paths.

Mitigation: Export only to new, non-sensitive destinations and review paths before sharing or uploading generated files.

Risk: Custom ARI endpoint environment variables could route requests away from the intended service.

Mitigation: Avoid custom ARI_BASE_URL values unless the endpoint is controlled and uses HTTPS, and require explicit local confirmation before enabling a custom base URL.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [ARI Amazon Review Assistant Usage Guide](使用说明.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-trend)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline shell commands; exported reports may be Markdown or HTML, and review exports may be CSV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include sampled review evidence, trend judgments, report links, credit usage, account status, and local export paths when requested.]

## Skill Version(s):

1.4.7 (source: server evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
