## Description:

核验域名可用性、安全状态以及风险标记，输出域名验证结论、校验失败原因和敏感标签，清理风险域名，优化外贸邮件列表并降低邮件退信概率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, marketing, recruiting, procurement, and research users use this skill to validate company domains before outreach, CRM cleanup, vendor checks, or list hygiene. It helps agents identify valid, invalid, unknown, and sensitive domain status through the Upkuajing OpenAPI service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages a local Upkuajing API key and may store it in ~/.upkuajing/.env.

Mitigation: Protect the local credential file, avoid sharing API keys, and use environment-level secret controls where available.

Risk: Domain validation calls can incur charges, and bundled account commands can create recharge orders.

Mitigation: Review pricing, account balance, and billing actions before approving paid validation or recharge operations.

Risk: Diagnostic error reporting can send request context to the vendor service.

Mitigation: Submit diagnostic reports only after user confirmation and avoid including sensitive customer data in error context.

Risk: The skill contacts Upkuajing services and performs version-check behavior.

Mitigation: Install only if the user trusts the Upkuajing service and accepts outbound requests to the vendor API.

## Reference(s):

- [Domain validation API reference](references/domain-api.md)
- [Skill error reporting API reference](references/skill-error-report-api.md)
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/domain-validity-check-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON response summaries with concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Domain validation results can include domain status, invalidity reason, sensitivity flag, total count, fee information, and request ID when returned by the API.]

## Skill Version(s):

1.0.2 (source: server evidence, SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
