## Description: <br>
搜索全球企业信息、个人信息，用于全球贸易、跨境出口、海外采购商的线索开发。帮助出口贸易商、采购商、服务商、代理商及销售团队通过搜索，得到企业决策人信息、企业高管信息；寻找供应商，并加速海外客户获取。本产品提供企业注册信息、背景资料以及联系方式（邮箱、电话、WhatsApp）。适用于海外客户开发、企业背调、人才搜索等场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, sales teams, exporters, sourcing teams, and business developers use this skill to search global company and person records, find decision makers, retrieve company or person details, and obtain contact channels for B2B lead generation and supplier discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends searched company or person identifiers to a third-party contact-data service and may return personal contact data. <br>
Mitigation: Confirm the provider's privacy and legal terms before use, limit searches to lawful business purposes, and avoid bulk or unsolicited outreach that may violate applicable rules. <br>
Risk: The skill stores API keys in ~/.upkuajing/.env. <br>
Mitigation: Restrict file permissions for the local credential file or move the key into a managed secret store when operating in a shared or managed environment. <br>
Risk: API calls can incur charges and some searches may perform many calls. <br>
Mitigation: Review pricing with the provider and require explicit user confirmation before paid or bulk operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-global-company-people-search-zh) <br>
- [Publisher profile](https://clawhub.ai/user/upkuajing) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer portal](https://developer.upkuajing.com/) <br>
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Company list API reference](references/company-list-api.md) <br>
- [Person list API reference](references/human-list-api.md) <br>
- [Company detail API reference](references/company-detail-api.md) <br>
- [Person detail API reference](references/human-detail-api.md) <br>
- [Contact API reference](references/contact-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON, files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON API responses, and generated task result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; list searches may write task result data and contact-data responses may include personal information.] <br>

## Skill Version(s): <br>
1.0.8 (source: SKILL.md metadata, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
