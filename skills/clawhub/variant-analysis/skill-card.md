## Description:

亚马逊变体分析 Skill 对比同一父体下颜色、尺寸和规格变体的评论口碑，帮助识别拖低评分的问题变体和更适合主推的优势变体。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to analyze ARI-collected Amazon review data by ASIN, compare variant performance, and turn review themes into inventory, listing, monitoring, or product-improvement decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits for collection, VOC reports, analysis, leaderboard queries, or advice workflows.

Mitigation: Use quote-only requests for pricing, keep autoconfirm off or constrained, and require explicit approval before paid analysis or collection.

Risk: The skill can manage account monitoring, watch schedules, competitor bindings, exports, and confirmation preferences.

Mitigation: Require explicit user approval before schedule, watch, competitor, export, or autoconfirm changes, and summarize any recurring or downstream cost.

Risk: The skill requires ARI account access through an API key.

Mitigation: Use browser authorization or ARI_API_KEY only, never paste keys into chat or reports, and avoid custom API bases unless the user deliberately enables the documented custom-base guard.

Risk: Retrying after a network interruption can duplicate a paid operation if the server already completed and archived the report.

Mitigation: Check report or operation status before rerunning confirmed paid commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/variant-analysis)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [README](README.md)
- [使用说明](使用说明.md)
- [ARI CLI 与 API 参考](references/reference.md)
- [ARI API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise text summaries, with optional JSON CLI responses and exported CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection, analysis, monitoring, and export workflows may depend on account plan, balance, and explicit or account-level confirmation settings.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
