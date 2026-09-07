## Description:

Helps agents search Chinese tender data, assess bid opportunities, identify incumbent-control risks, analyze suppliers and competitors, and summarize market and pricing signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, procurement, and bid teams use this skill to find Chinese tender opportunities, investigate buyer and supplier relationships, compare competitors, estimate pricing from historical awards, and prepare concise bid/no-bid guidance from tender-data API results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party tender-data service receives tender, company, competitor, and pricing queries.

Mitigation: Review organizational data-sharing rules before use and avoid submitting confidential project details unless that service is approved.

Risk: Automatic account creation can collect limited device features after user consent when no API key is configured.

Mitigation: Prefer a preconfigured ZLBX_API_KEY from a secure mechanism; if auto-registration is used, confirm consent before any collection.

Risk: The auto-registration flow can persist an API key in ~/.zlbx/config.json.

Mitigation: Restrict local file permissions and rotate or remove the key when it is no longer needed.

Risk: Paid accounts may receive full project contact phone numbers.

Mitigation: Display returned contact data only as needed, preserve masked values, and do not enrich or bulk export contact information.

Risk: Responses may include publisher referral or recharge links.

Mitigation: Review user-facing output for promotional content and make service links clear when they are operationally required.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/liu-jiapeng/skills/tender-opportunity-biaobiaoda)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries with JSON REST payload examples and links to source tender records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tabular tender results, company analysis, market aggregates, account status, and setup guidance for ZLBX_API_KEY or local API-key configuration.]

## Skill Version(s):

2.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
