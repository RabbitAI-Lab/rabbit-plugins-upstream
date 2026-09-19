## Description:

从 Amazon 评论中提炼买家画像、使用场景、购买动机、痛点、趋势、竞品差异和可导出的运营分析报告，并通过 ARI 授权账户执行相关查询与分析流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to turn ARI-collected review data for an ASIN into buyer personas, pain points, trend summaries, competitor comparisons, listing guidance, monitoring actions, and exportable reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits automatically when account rules allow paid report or analysis execution.

Mitigation: Use explicit instructions such as "only quote, do not execute" or "ask before every credit charge," and confirm quoted paid actions before allowing execution.

Risk: The skill can change account monitoring or review-analysis workflow state, including schedules, competitors, workbench status, autoconfirm settings, and watch deletion.

Mitigation: Verify the exact schedule, competitor, workbench, autoconfirm, or watch-delete action before allowing the skill to run it.

Risk: The skill requires an ARI API key for authenticated workflows.

Mitigation: Authorize through the browser setup flow or local configuration, and avoid pasting API keys into chat, reports, or command examples.

Risk: Reports and recommendations may be based on limited ARI-collected Amazon review samples rather than all reviews or all variants.

Mitigation: Review the stated sample range, site, collection window, and variant limitations before using conclusions for business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/user-persona)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI user guide](artifact/使用说明.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI report center](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Conversational text and Markdown summaries with optional report links, CSV/Markdown/HTML exports, and inline shell commands for setup or advanced use.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require an ARI API key and explicit confirmation for paid analysis, collection, leaderboard, or advice operations.]

## Skill Version(s):

1.4.13 (source: server release evidence, skill frontmatter, _meta.json, and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
