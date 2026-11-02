## Description:

根据公司与报告期生成中文财报点评初稿，覆盖业绩变化、科目勾稽、指引对照和盈利质量，并按包内规则进行格式检查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

投研人员可用它按公司和报告期整理财报复盘、研究底稿或晨会材料。产物是供人工核对和补充判断的初稿，不用于自动给出评级或目标价。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key may be exposed if authenticated requests use unchecked destinations or follow redirects that forward credentials.

Mitigation: Use the public-text workflow without an API key until destination and redirect handling are corrected. For authenticated use, require verified HTTPS destinations and prevent redirects from forwarding credentials elsewhere.

Risk: Documents supplied through Omni/Bridge may be transferred or retained by the connected service.

Mitigation: Clarify document transfer and retention before use, and grant access only to a dedicated folder containing selected public reports.

Risk: A checker PASS can be mistaken for confirmation that figures or sources are accurate.

Mitigation: Treat PASS as a formatting check and have a person verify figures against cited source material.

## Reference(s):

- [覆盖账本规范](references/coverage-ledger.md)
- [数据渠道说明](references/data-channels.md)
- [证据文件格式](references/evidence-format.md)
- [预期池使用说明](references/expectation-pool.md)
- [报告结构模板](references/report-skeleton.md)
- [Cue MCP 服务目录](https://cuecue.cn/api/mcp-catalog)
- [Cue MCP 服务说明](https://cuecue.cn/hub/mcp)
- [Cue Omni Reader 说明](https://cuecue.cn/hub/omni-reader)
- [Cue API 凭据说明](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, JSON, JSONL, Text]

**Output Format:** [中文 Markdown 报告，以及结构化 JSON/JSONL 台账、来源索引和运行记录]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [包含来源标注和待人工判断项；数字与来源的事实准确性仍需人工核对。]

## Skill Version(s):

0.3.45 (source: skill frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
