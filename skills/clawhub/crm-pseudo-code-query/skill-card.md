## Description: <br>
同花顺 CRM (crm.10jqka.com.cn) 批量查询用户伪码。此 skill 应在用户提供一批 userid 并需要查询对应的伪码（格式 #数字#，出现在客户详情页联系电话字段）时使用。通过 mTLS 客户端证书加密码三步认证登录 CRM，然后批量抓取客户详情页提取伪码。触发场景：用户说给我伪码、提供 userid 列表、提到同花顺 CRM 伪码查询。使用前需自行配置证书和密码。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenmiley](https://clawhub.ai/user/chenmiley) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Authorized CRM users use this skill to prepare mTLS credentials, authenticate to 同花顺 CRM, and batch query pseudo codes for provided user IDs. It is intended for approved internal workflows that require retrieving customer-linked pseudo-code values from CRM detail pages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles enterprise CRM credentials, client private keys, and customer-linked data. <br>
Mitigation: Install only for approved internal workflows, limit use to users authorized for the listed CRM accounts, and prefer managed mTLS credentials without exporting private keys. <br>
Risk: Passwords, cookie jars, and sensitive output files can be exposed if handled casually. <br>
Mitigation: Avoid passwords in command lines or URLs, clean up cookie jars and sensitive files, and write outputs only when explicitly requested. <br>
Risk: The workflow may bypass normal TLS validation during CRM access. <br>
Mitigation: Use trusted certificate configuration and validate TLS normally wherever the environment supports it. <br>


## Reference(s): <br>
- [CRM 认证流程详解](references/auth_flow.md) <br>
- [ClawHub skill page](https://clawhub.ai/chenmiley/skills/crm-pseudo-code-query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with command examples and local text result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can print a query summary and write pseudo-code query results to a local text file.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
