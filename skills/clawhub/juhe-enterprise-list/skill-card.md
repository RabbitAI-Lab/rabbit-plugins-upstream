## Description:

企业工商信息列表查询。根据企业名称关键字、注册号或统一社会信用代码模糊查询企业列表，返回公司名称、法人、成立日期、注册号、信用代码。使用场景：用户说"查企业"、"查公司"、"企业列表"、"工商信息"、"统一社会信用代码"、"查一下这家公司"、"模糊搜企业"等。通过聚合数据（juhe.cn）API 实时查询。

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up Chinese enterprise registration list records through Juhe by company keyword, registration number, or unified social credit code. It helps present company names, legal representatives, incorporation dates, registration numbers, and credit codes from the API response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paid Juhe API key may be exposed if passed on the command line or stored in a plaintext .env file.

Mitigation: Use a protected environment variable or secret manager for JUHE_ENTERPRISE_LIST_KEY, avoid the --key option, and keep scripts/.env out of shared or version-controlled directories.

Risk: Enterprise search terms are sent to Juhe when queries are executed.

Mitigation: Use the skill only with an appropriate Juhe business API entitlement and avoid submitting sensitive search terms unless that data sharing is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-list)
- [Juhe enterprise business information API documentation](https://www.juhe.cn/docs/api/id/192)
- [Juhe website](https://www.juhe.cn)
- [Juhe enterprise simpleList API endpoint](https://japi.juhe.cn/enterprise/simpleList)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance plus command-line output containing formatted text and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and JUHE_ENTERPRISE_LIST_KEY; API results are paginated with a maximum page size of 20.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
