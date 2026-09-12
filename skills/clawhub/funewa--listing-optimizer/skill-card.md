## Description:

从 Amazon 买家评论中提炼痛点、购买动机和用户措辞，帮助运营人员优化标题、五点描述和 A+ 文案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce operators use this skill to turn ARI-collected Amazon review data into listing copy, VOC summaries, competitor comparisons, trend notes, and product improvement priorities. It is intended for review-driven marketplace operations and listing optimization workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI credit spending may occur under account auto-confirm rules.

Mitigation: Use "only quote, do not execute" for price checks, set autoconfirm off when confirmation is required for every paid action, and require explicit approval before confirmed paid commands.

Risk: The skill can alter future confirmation thresholds, monitoring state, or workbench state.

Mitigation: Review requested state changes with the user before execution and keep monitoring, autoconfirm, and workbench updates tied to explicit user intent.

Risk: Local exports can write files to user-provided paths.

Mitigation: Use explicit export paths only when overwriting is acceptable and review saved file locations after export.

Risk: Listing recommendations can be misleading when review samples, time windows, marketplace coverage, or variant coverage are limited.

Mitigation: Report the data range, sample limits, and trend window with recommendations, and avoid presenting unsupported inferences as data-backed findings.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/listing-optimizer)
- [ARI CLI 与 API 参考](references/reference.md)
- [ARI Amazon 评论智能助手使用指南](使用说明.md)
- [账号与授权管理](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [积点与套餐](https://ari.funewa.com/zh/billing)
- [在线报告](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with optional shell commands, online report links, and local CSV, Markdown, or HTML exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may use ARI credits for collection, analysis, monitoring, or workbench actions according to account confirmation settings.]

## Skill Version(s):

1.4.8 (source: server release, _meta.json, SKILL.md frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
