## Description:

查询和分析招投标公告、项目进展、企业工商信息及采购市场数据，默认侧重 IT、信息化和数字化领域。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

采购和投标人员可检索招标与中标公告、跟踪项目阶段，并分析企业、供应商及市场趋势；IT / 信息化是默认检索方向，可按用户需求调整。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration may transmit a hashed device identifier.

Mitigation: Review and obtain consent before registration; set ZLBX_API_KEY manually to avoid the automatic registration path.

Risk: A service API key may be stored locally in ~/.zlbx/config.json.

Mitigation: Review local credential storage before enabling registration and protect the resulting key.

Risk: Company-name expansion or amount filters may lead to misleading business conclusions.

Mitigation: Verify matched company identities and amount filters before relying on results for business decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-it)
- [Service homepage](https://ai.zhiliaobiaoxun.com/?ch=s153)
- [Search API reference](artifact/references/api-search.md)
- [Account registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown with result summaries and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the search scope and filters used.]

## Skill Version(s):

1.0.3 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
