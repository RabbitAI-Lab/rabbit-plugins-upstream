## Description:

核验邮箱地址的真实可用状态，逐条返回邮箱验证结果以及判定原因，清理无效邮箱数据，降低外贸邮件群发退信概率，完成邮件列表合规清洗。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, recruiting, marketing, CRM operations, and procurement teams use this skill to validate email address status before outreach, list cleaning, supplier checks, or candidate screening. The skill helps reduce bounce risk by returning per-address validation status and reasons from Upkuajing's external API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email addresses are sent to Upkuajing's external API for validation.

Mitigation: Use the skill only for email data that is approved for third-party processing, and avoid submitting sensitive or unapproved lists.

Risk: API calls can incur paid usage charges.

Mitigation: Confirm cost-bearing operations before execution and use the pricing command or pricing page to review current charges.

Risk: The skill can create or use an API key and store it locally in ~/.upkuajing/.env.

Mitigation: Prefer manually provisioning the credential, restrict file access to the local key, and rotate or remove the key when it is no longer needed.

Risk: Recharge and account-management flows may affect a paid API account.

Mitigation: Review account and recharge commands before use, and require explicit user approval before opening or acting on payment flows.

Risk: The skill may write a local version cache at ~/.upkuajing/version_cache.json.

Mitigation: Review local state written under ~/.upkuajing and remove cached data if local persistence is not desired.

## Reference(s):

- [邮件有效性检测 API](references/email-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API results and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python, an UPKUAJING_API_KEY credential, and access to Upkuajing's external API.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
