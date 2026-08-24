## Description:

全域电商经营专家团 v1.5.10 supports ecommerce store diagnosis, weekly/monthly/annual business reporting, operating reviews, single-platform growth, advertising ROI and profit optimization, content/live-commerce diagnosis, and action planning using authorized business data as the evidence source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gzbarry1980-bot](https://clawhub.ai/user/gzbarry1980-bot)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand owners, and operations teams use this skill to turn scoped store, platform, content, advertising, and fulfillment data into auditable diagnostics, reports, action lists, and delivery-ready report artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive ecommerce store exports, platform data, customer scope details, and report artifacts.

Mitigation: Use it only with an explicit client scope, platform, time period, and permitted file list; keep the artifact's client-scope isolation and pre-release leak checks in force.

Risk: Broad business-plan triggers may activate the skill when the user did not intend to run an ecommerce reporting workflow.

Mitigation: Narrow activation triggers where possible and confirm the ecommerce use case before reading files or producing reports.

Risk: Incomplete cost, margin, refund, inventory, attribution, or PDF rendering evidence can lead to overconfident reports.

Mitigation: Apply the PASS/WARN/BLOCKED data-quality gate, label unsupported conclusions as assumptions or data gaps, and withhold formal delivery until review and rendering checks pass.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gzbarry1980-bot/skills/omni-ecom-skill)
- [沐风｜主理人 / 全域经营操盘总监](artifact/references/team-lead.md)
- [沈数清｜电商数据分析专家](artifact/references/data-analyst.md)
- [梁运通｜平台运营专家](artifact/references/platform-ops.md)
- [洪涨声｜内容与直播增长专家](artifact/references/content-live-growth.md)
- [罗效盈｜投流与利润优化专家](artifact/references/ad-profit-optimizer.md)
- [韦交达｜交付复核专家](artifact/references/delivery-review.md)
- [数据质量闸门与证据规范](artifact/references/data-quality-gate.md)
- [报告交付与图表化 PDF](artifact/references/report-delivery.md)
- [客户隔离、版本与修订](artifact/references/privacy-and-versioning.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, guidance]

**Output Format:** [Markdown reports with structured JSON report data, action tables, and optional PDF delivery artifacts when the host supports file generation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are scoped to authorized client data and should include evidence notes, data-quality gate status, role participation, version, report revision, and delivery review status.]

## Skill Version(s):

1.5.10 (source: server release evidence, manifest.yaml, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
