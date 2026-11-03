## Description:

A股公告事件速读卡：把一份临时公告（回购/增减持/业绩预告/重大合同/处罚问询等）变成可核对的五段卡——逐字关键数+出处、影响链候选、同类对照、待核清单。评级与目标价一律[待人工]，不预测走势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT

## Use Case:

A股公告阅读者和分析人员可用它把单份临时公告整理成带出处、便于人工复核的五段事实卡；它不提供评级、目标价或投资建议。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The optional authenticated online setup has incomplete destination checks that could expose the API key.

Mitigation: Use supplied announcement text and local validation without a key until credential routing is hardened. Authenticated requests should validate authorized HTTPS destinations and reject redirects; for offline connectivity inspection, use --catalog-file and omit --post.

Risk: Private annotations may be exposed when content is sent to an external parsing service.

Mitigation: Remove private annotations before external parsing.

Risk: Figures or judgments in the generated brief may be inaccurate even when the local validation passes.

Mitigation: Manually verify figures and judgments against the original announcement.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/huhoo/skills/cue-event-brief-cn)
- [Cue data channel configuration](https://cuecue.cn/hub/mcp)
- [Cue document parsing configuration](https://cuecue.cn/hub/omni-reader)
- [Cue API key configuration](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown five-part announcement brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verbatim key figures with source anchors, candidate impact chains, peer-filing comparison, and items for human review.]

## Skill Version(s):

0.2.24 (source: frontmatter, CHANGELOG released 2026-10-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
