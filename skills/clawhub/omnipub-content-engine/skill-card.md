## Description:

AI-driven content lifecycle management for topic research, generation, fact-checking, visual preparation, GEO optimization, WeChat/Toutiao publishing, and post-publication analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mikogeyu-cell](https://clawhub.ai/user/mikogeyu-cell)

### License/Terms of Use:

MIT

## Use Case:

Content teams, operators, and developers use this skill to manage a human-gated publishing workflow across WeChat official accounts and Toutiao. It helps prepare topics, drafts, checks, visuals, platform-ready HTML, publishing steps, and analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles live WeChat/Toutiao publishing credentials.

Mitigation: Use a dedicated low-privilege account or token, keep config.yaml and credential files out of version control, and review each publishing step before execution.

Risk: Publishing and draft-deletion commands can change platform state.

Mitigation: Require manual confirmation before Toutiao publishing or WeChat draft deletion, and verify the target account, article, and draft media ID before running those commands.

Risk: The CLI may print part of a token to logs.

Mitigation: Run publishing commands only in private terminals, avoid shared logs, and rotate credentials if token output is exposed.

Risk: Fact-check output may be mistaken for proof that facts were verified.

Mitigation: Treat fact-check reports as claim/source checklists and manually verify important claims against reliable sources before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mikogeyu-cell/skills/omnipub-content-engine)
- [README](artifact/README.md)
- [Skill entrypoint](artifact/SKILL.md)
- [阶段1 · 选题讨论方法论](artifact/references/01-topic-research.md)
- [阶段2 · 内容生成方法论（双平台双版本）](artifact/references/02-content-generation.md)
- [阶段3 · 数据源查证核实（用户红线，强制）](artifact/references/03-fact-checking.md)
- [阶段4 · 图表设计与 AI 信息图提示词](artifact/references/04-charts-infographics.md)
- [阶段5 · 文末模板引擎 + 风格主题系统](artifact/references/05-footer-styles.md)
- [阶段6 · GEO 优化（让文章被 AI 抓取引用）](artifact/references/06-geo-optimization.md)
- [阶段7 · 双平台发布](artifact/references/07-publishing.md)
- [阶段8 · 数据复盘与归因分析](artifact/references/08-analytics.md)
- [微信公众号 CSS 兼容性约束](artifact/references/wechat-css-constraints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, Shell commands, Configuration, Guidance, API Calls]

**Output Format:** [Markdown, HTML, JSON/YAML configuration, shell command guidance, and platform-specific publishing instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create previews, reports, footer fragments, prepared publishing packages, WeChat drafts, and Toutiao publishing instructions; live platform actions require credentials and user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
