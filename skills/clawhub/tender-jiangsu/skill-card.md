## Description:

协助检索和分析招投标公告、企业信息与采购市场数据，默认聚焦江苏省，并可按用户指定范围查询。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

采购、投标和市场分析人员可查询招标及中标公告、潜在项目、企业工商信息和采购趋势。默认搜索江苏省，但用户可以指定其他地区或行业。

### Deployment Geography for Use:

Global (Jiangsu Province is the default search scope, not a deployment restriction)

## Known Risks and Mitigations:

Risk: Procurement queries are sent to the Zhiliaobiaoxun service.

Mitigation: Avoid including confidential details in queries and review the service before use.

Risk: If no API key is configured, automatic registration may collect device characteristics and create an account.

Mitigation: Require informed consent before registration, or preconfigure ZLBX_API_KEY to avoid device-based registration.

Risk: An automatically obtained API key may be saved in ~/.zlbx/config.json.

Mitigation: Protect the local credential file and do not disclose the API key in chat or logs.

Risk: Account checks can receive upgrade notices and send display acknowledgements.

Mitigation: Review the package/version acknowledgement behavior before installation and acknowledge notices only after showing them to the user.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-jiangsu)
- [知了标讯服务](https://ai.zhiliaobiaoxun.com/?ch=s151)
- [标讯检索接口说明](references/api-search.md)
- [企业分析接口说明](references/api-company.md)
- [工商数据接口说明](references/api-registry.md)
- [市场分析接口说明](references/api-market.md)
- [账户接口说明](references/api-account.md)
- [自动注册说明](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [States the actual search scope; availability and account credits depend on the service.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
