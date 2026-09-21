## Description:

亚马逊新品验证帮助卖家在上架前用同类 Amazon 评论评估需求、痛点、差异化机会和运营风险，并通过 ARI 生成评论分析、VOC、趋势、竞品对比和导出结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce operators use this skill to validate new Amazon product ideas before launch, estimate demand from review evidence, compare competitors, and turn collected reviews into product, listing, keyword, monitoring, and customer-response guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger paid ARI credit use under account auto-confirm rules.

Mitigation: Set autoconfirm off or explicitly ask for only a quote before running paid review collection, VOC, analysis, leaderboard, or advice workflows.

Risk: Schedule, watch, competitor, and autoconfirm changes can persist beyond the current chat.

Mitigation: Confirm the target ASIN, site, cadence, and cost before enabling persistent monitoring or changing account confirmation settings.

Risk: Reports can be misleading if samples are small, stale, or do not cover all variants.

Mitigation: Use the skill's sample-range and limitation statements when making decisions, and avoid treating absent or partial review data as complete market evidence.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/new-product)
- [ARI Usage Guide](artifact/使用说明.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown and text responses with optional shell commands, JSON summaries, CSV exports, and Markdown or HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish direct data from inference and recommendations; reports are based on ARI-collected Amazon review samples and may include links to archived web reports.]

## Skill Version(s):

1.4.13 (source: frontmatter, _meta.json, release evidence, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
