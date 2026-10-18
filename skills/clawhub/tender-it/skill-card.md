## Description:

协助查询和分析招投标公告、企业信息与市场数据，默认聚焦 IT、信息化及数字化项目。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

采购、销售和投标人员使用此技能查找招标及中标机会、跟踪项目进展，并分析企业、供应商、采购方及市场价格；IT 信息化只是默认行业范围，可按用户要求调整。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration can transmit a device fingerprint to the service.

Mitigation: Review the registration behavior and obtain user consent first; provide an existing ZLBX_API_KEY to avoid automatic registration.

Risk: An automatically issued API key can be stored locally and used for authenticated queries.

Mitigation: Protect the local credential, review authenticated requests before use, and remove ~/.zlbx/config.json when the stored credential is no longer wanted.

Risk: Markdown comments contain instructions for authenticated requests and acknowledgement actions that readers may overlook.

Mitigation: Review the full skill text, including comments, before installation or execution; confirm what requests and acknowledgements it may send.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-it)
- [Publisher profile](https://clawhub.ai/user/bailianai)
- [知了标讯服务](https://ai.zhiliaobiaoxun.com/?ch=s153)
- [标讯搜索 API 参考](artifact/references/api-search.md)
- [企业与工商 API 参考](artifact/references/api-registry.md)
- [市场分析 API 参考](artifact/references/api-market.md)
- [账户查询 API 参考](artifact/references/api-account.md)
- [自动注册与凭证配置说明](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown responses with search results, summaries and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the available tender-data service and the user's search scope.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
