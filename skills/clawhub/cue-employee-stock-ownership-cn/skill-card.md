## Description:

把一份 A 股员工持股计划草案或公告拆成八项逐字条款卡，并标出缺失信息与需人工判断的事项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT

## Use Case:

面向需要快速核对 A 股员工持股计划草案或公告条款的员工与审阅者，用于逐项查看原文和来源锚并发现缺项；参与价值、价格公允性与税务判断留待人工处理。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags a mismatch between the skill's stated purpose and MCP service discovery, as well as unpinned installation commands.

Mitigation: Review why MCP services are contacted and use a pinned, reviewed installer and source revision before installation.

Risk: Private document attachments may be processed through an external service, and the security guidance calls for confirming where the API key is sent.

Mitigation: Confirm the service and credential handling before enabling the API key; do not share private attachments until their processing path is understood.

## Reference(s):

- [ESOP 条款参照](references/esop-terms.md)
- [Cue 数据通道配置](https://cuecue.cn/hub/mcp)
- [Cue 附件解析配置](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown 条款卡，含原文引句、来源锚、缺项清单和待人工事项]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [按八项员工持股计划条款组织；缺失内容明确标注。]

## Skill Version(s):

0.1.0 (source: release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
