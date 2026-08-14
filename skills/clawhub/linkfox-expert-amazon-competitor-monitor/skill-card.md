## Description:

亚马逊竞品动态监控专家。适用于周期性跟踪竞品 ASIN、价格变化、BSR 波动、评论变化、Listing 改动、定时提醒和竞品动态报告的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to monitor competitor ASINs, expand competitor pools from keywords or images, detect pricing, BSR, review, listing, and keyword anomalies, and produce Chinese reports or visual deliverables for follow-up action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses credential-bearing LinkFox calls and handles Amazon competitor data.

Mitigation: Install only when the publisher is trusted, keep API keys scoped appropriately, and point gateway or endpoint environment variables only at trusted LinkFox hosts.

Risk: The bundled workflow can create recurring monitoring tasks and paid-credit-consuming data collection runs.

Mitigation: Review credit estimates, recurring-task settings, notification destinations, and any payment-adjacent action before approving execution.

Risk: Generated local files can be uploaded and made publicly accessible.

Mitigation: Upload only reports, images, CSV files, or other artifacts that are safe to publish.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-amazon-competitor-monitor)
- [Competitor anomaly detection rules](skills/amazon-competitor-monitor/references/anomaly-rules.md)
- [Competitor monitoring data cleaning rules](skills/amazon-competitor-monitor/references/data-cleaning.md)
- [Credit usage alert rules](skills/amazon-competitor-monitor/references/credit-alert-rules.md)
- [Competitor monitoring report template](skills/amazon-competitor-monitor/references/report-template.md)
- [Visualization generation guide](skills/amazon-competitor-monitor/references/visualization-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance]

**Output Format:** [Chinese Markdown summaries, HTML reports or dashboards, CSV tables, and HTML slide decks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create scheduled-monitoring configurations and write report/data artifacts under session-scoped LinkFox paths.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
