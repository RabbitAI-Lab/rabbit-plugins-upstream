## Description:

This skill helps agents search, aggregate, and analyze Chinese tender and bid data for market research, competitive analysis, pricing trends, and company procurement or supplier insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, business analysts, market researchers, and sales teams use this skill to query tender and bid records, aggregate market trends, compare purchasers, suppliers, and brands, and review company bidding relationships through the provider's authenticated API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First use without a configured API key can create or recover an external trial account and send a stable hashed MAC-derived device identifier for deduplication.

Mitigation: Prefer configuring ZLBX_API_KEY explicitly; if auto-registration is used, require clear user consent before collecting device features or making the registration request.

Risk: The skill may store an API key in ~/.zlbx/config.json after auto-registration.

Mitigation: Protect the local configuration file, avoid sharing API keys in chat or logs, and use environment-based key management when available.

Risk: Paid account features may expose bid-project contact details.

Mitigation: Use contact data only for legitimate business purposes and apply privacy, compliance, and access-control review before exporting or sharing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/tender-bid-union-zhongzhaolianhe)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, API calls, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown responses with JSON API request and response data, plus occasional shell commands or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an API key from ZLBX_API_KEY or local configuration; first-use auto-registration may create or recover a trial account when no key is configured.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
