## Description:

Analyzes Amazon competitor reviews to compare ASINs, identify recurring strengths and weaknesses, and produce evidence-based opportunity, positioning, and product-operations guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to inspect collected review data, compare their ASINs with competitors, understand pain points and buying motives, and prepare listing, product, monitoring, and response actions. The skill can also help with paid ARI reports, exports, alerts, benchmarking, and operational workflows when the user's account and credits allow them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI collection and analysis can consume account credits without a fresh local confirmation when server-side auto-confirm rules apply.

Mitigation: Before running paid reports, ask for quote-only behavior or require confirmation before every charge, and review returned credit usage before continuing.

Risk: The skill works with Amazon ASINs, review data, reports, and an ARI account key.

Mitigation: Install and use it only when the user trusts ARI/funewa with that data, and keep API keys in the supported local configuration or environment variable rather than in chat or reports.

Risk: Monitoring and competitor-binding actions can create ongoing remote behavior and future collection costs.

Mitigation: Confirm the target ASIN, competitor relationship, schedule, and cost before enabling or changing monitoring, and use read-only commands when the user is only asking to inspect data.

Risk: A network interruption during a paid report flow may happen after the server has already charged credits and archived a report.

Mitigation: Check the latest reports or operation status before retrying a paid command so the same work is not charged twice.

Risk: Review samples, collection windows, variant coverage, and account permissions can limit the reliability of conclusions.

Mitigation: Report the data scope, sample size, site, time window, and any missing or partial data, and avoid presenting unsupported trends or competitor comparisons as settled facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-review)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [README](README.md)
- [User guide](使用说明.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Concise text summaries and Markdown reports, with JSON CLI responses and optional CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Some collection, report, leaderboard, operations, and advice flows may spend ARI credits under the user's account confirmation settings.]

## Skill Version(s):

1.4.13 (source: frontmatter, _meta.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
