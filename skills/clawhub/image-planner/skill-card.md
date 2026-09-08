## Description:

根据 Amazon 商品详情和评论中的理解障碍，规划主图与辅图应表达的信息；仅用于图片信息规划，不生成图片文件、不投放广告、不自动发布。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operators use this skill to turn product details and review friction into main-image and secondary-image planning guidance. It helps decide what information product images should communicate, while leaving image generation, advertising actions, and Amazon page publishing outside scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access ARI account functions beyond image planning, including billing-related review analysis, exports, monitoring, alerts, and confirmation-policy changes.

Mitigation: Install only for users who intend to grant broad ARI account access, and review requested actions before enabling reports, exports, monitoring, competitor setup, or confirmation-policy changes.

Risk: Paid ARI operations may consume credits, and some small operations can be auto-confirmed according to server-side account policy.

Mitigation: Set autoconfirm to ask every time when per-charge approval is required, and verify quoted credits, ASIN, marketplace, and requestId before confirmed runs.

Risk: Interrupted paid operations may already have generated a report or consumed credits.

Mitigation: Check the existing operation status or latest reports before retrying any confirmed paid command.

Risk: Exports can write local report or review files.

Mitigation: Use deliberate export destinations and avoid arbitrary paths when saving Markdown, HTML, or CSV outputs.

## Reference(s):

- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [Amazon 商品图片规划 专属运营工作流](artifact/references/operation-workflow.md)
- [ARI Amazon 评论智能助手使用指南](artifact/使用说明.md)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/image-planner)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with concise analysis, image-planning guidance, and occasional shell commands for setup or troubleshooting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may reference ARI account state, credits, reports, review samples, and confirmation status returned by the service.]

## Skill Version(s):

1.4.8 (source: server release evidence, frontmatter, _meta.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
