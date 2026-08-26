## Description:

核验电话号码真实有效性、号码类型以及 WhatsApp 注册状态，输出核验结果、号码分类、国家代码和 WhatsApp 启用情况，筛选无效联系方式，提升外贸客户触达效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams, recruiters, traders, and CRM operators use this skill to validate phone numbers, classify landline or mobile numbers, and check WhatsApp availability before outreach, screening, or contact-data cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Phone numbers are sent to Upkuajing's remote API for validation.

Mitigation: Use the skill only when sharing those phone numbers with Upkuajing is acceptable for the intended contact-cleanup or verification workflow.

Risk: The skill stores and uses an API key from the user's environment or ~/.upkuajing/.env.

Mitigation: Protect the API key file, avoid sharing credentials, and rotate the key if exposure is suspected.

Risk: Phone validation calls and recharge flows can involve paid API usage.

Mitigation: Confirm paid operations and recharge actions before running them, and use the pricing helper or pricing page for current costs.

Risk: Optional error reports may include troubleshooting context.

Mitigation: Send error reports only after user confirmation and exclude phone numbers, secrets, and full request or response bodies from report context.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/phone-validity-check-zh)
- [Upkuajing Homepage](https://www.upkuajing.com)
- [Upkuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [电话有效性检测 API](references/phone-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns phone validation status, phone type, country code, WhatsApp status, fee information, and request identifiers when available.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
