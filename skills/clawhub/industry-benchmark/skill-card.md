## Description:

Helps Amazon sellers use ARI to compare an ASIN against category star-rating and negative-review-rate benchmarks and, when authorized, run broader review analysis, reports, monitoring, alerts, exports, and operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to query ARI from an agent for category benchmarking, review analysis, VOC reports, competitor comparison, monitoring, alerts, and exports for Amazon ASINs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI analysis or leaderboard actions may spend credits under user authorization or service-side auto-confirm rules.

Mitigation: Use quote-only requests for pricing checks and ask the agent to require confirmation before each credit-spending action when you do not want auto-confirmed charges.

Risk: The skill stores an ARI API key locally and sends ASIN, review, and account-related requests to ari.funewa.com.

Mitigation: Authorize only with the intended ARI account, do not paste credentials into chat, and revoke or rotate the ARI key if it may have been exposed.

Risk: The skill can manage remote schedules, watches, competitors, alerts, workbench status, reports, and exports when asked.

Mitigation: Confirm target ASINs, watch IDs, report IDs, and requested state changes before execution, and review export destinations before using exported files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/industry-benchmark)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Amazon Review Assistant User Guide](使用说明.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Conversational text and Markdown reports, with occasional CLI commands and JSON/API-derived results summarized for the user.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an ARI API key, may call ari.funewa.com, and can initiate paid analysis when user authorization or service-side auto-confirm rules apply.]

## Skill Version(s):

1.4.11 (source: server release, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
