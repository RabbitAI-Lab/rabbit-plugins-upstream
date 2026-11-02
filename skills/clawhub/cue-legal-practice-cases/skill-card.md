## Description:

围绕用户提出的中国法律争议，检索公开裁判文书、监管问答与实务案例，并整理裁判观点和带来源的实务参考报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向遇到民事、刑事或合规问题的个人及律师，检索并比较中国公开类案，梳理争议焦点、裁判口径及证据和行动参考。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: API 密钥可能因粘贴到聊天或不安全存放而暴露。

Mitigation: 通过受保护的本地文件或受支持的密钥管理方式配置密钥；已分享的密钥应轮换。

Risk: 案件问题可能包含保密或可识别个人的信息，并会发送给 Cue 服务处理。

Mitigation: 提交前移除机密和身份信息，并确认适用的数据处理要求。

Risk: Runner 更新及报告链接访问范围可能影响敏感材料的使用。

Mitigation: 用于敏感材料前先审查 Runner 更新，并核实报告链接的访问权限。

## Reference(s):

- [Cue Playbook](https://cuecue.cn/playbook)
- [中国裁判文书网](https://wenshu.court.gov.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文结构化 Markdown 报告]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [案例条目包含案号和来源链接（如检索结果提供）；覆盖以公开资料为主，内容不构成法律意见。]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
