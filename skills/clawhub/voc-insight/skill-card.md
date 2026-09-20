## Description:

VOC洞察 extracts voice-of-customer signals from Amazon reviews, including personas, purchase drivers, usage scenarios, sentiment, unmet needs, listing recommendations, product improvement ideas, competitive analysis, monitoring, alerts, and report exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and agents use this skill to analyze Amazon review data for customer pain points, buying motivations, trends, competitor comparisons, listing copy improvements, product changes, alerts, and exportable reports. It requires an ARI API key and works through the ARI service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send Amazon review and ARI account data to ari.funewa.com.

Mitigation: Install and use it only when the user accepts ARI service processing; keep API keys out of chat and use the documented official HTTPS endpoint.

Risk: Some VOC and analysis reports may consume ARI credits automatically under account auto-confirm rules.

Mitigation: Use quote-only mode or require per-action confirmation before paid analyses when avoiding surprise credit use is important.

Risk: The skill can change persistent ARI account settings, including auto-confirm behavior and monitoring schedules.

Mitigation: Make persistent setting or monitoring changes only after explicit user direction, then restate the resulting rule or schedule.

## Reference(s):

- [VOC洞察 README](README.md)
- [ARI Amazon 评论智能助手使用指南](使用说明.md)
- [ARI CLI 与 API 参考](references/reference.md)
- [VOC洞察 ClawHub listing](https://clawhub.ai/funewa/skills/voc-insight)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands; generated reports may include Markdown, HTML, CSV, JSON-derived summaries, and online report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Some report workflows can consume ARI credits under account auto-confirm rules.]

## Skill Version(s):

1.4.13 (source: frontmatter, release evidence, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
