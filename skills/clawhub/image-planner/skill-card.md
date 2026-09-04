## Description:

根据 Amazon 商品详情和评论中的理解障碍，规划主图与辅图应表达的信息；不生成图片文件、投放广告或自动发布页面。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to turn product-detail fields and review pain points into a planned information structure for main and supporting product images. It is intended for image planning and listing guidance, not image generation, ad execution, or automatic publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags a broad paid review-operations toolkit under a narrow image-planning label.

Mitigation: Install only when ARI account access beyond image planning is intended, and review available commands before use.

Risk: Some operations can consume ARI credits, including analysis runs, collection, leaderboard queries, and review advice.

Mitigation: Require a quoted cost and explicit user confirmation before paid operations unless the user has deliberately configured autoconfirm.

Risk: Autoconfirm settings and recurring collection or watch features can change when charges occur.

Mitigation: Review the autoconfirm threshold, recurring schedules, watch settings, competitor monitoring, and billing state before enabling or continuing automated workflows.

Risk: Exports and report links may expose product, review, or account-associated analysis data.

Mitigation: Share exported files and report URLs only with intended recipients and verify that they belong to the correct ARI account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/image-planner)
- [ARI API and CLI reference](references/reference.md)
- [Amazon 商品图片规划 专属运营工作流](references/operation-workflow.md)
- [ARI API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI products](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report links, cost and balance summaries, report identifiers, sample-window notes, and command traces when returned by the ARI service.]

## Skill Version(s):

1.4.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
