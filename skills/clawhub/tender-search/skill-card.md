## Description:

tender-search helps agents search and analyze Chinese tender, bid award, procurement, supplier, competitor, market, and pricing data through the ZhiLiao BiaoXun API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to retrieve procurement notices, company bid history, supplier and competitor intelligence, market aggregates, expiring projects, proposed projects, and account status from the ZhiLiao BiaoXun service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender queries, company names, and related procurement search terms are sent to the vendor's external API.

Mitigation: Install only where that data sharing is acceptable, and avoid submitting sensitive procurement plans or confidential identifiers.

Risk: If no API key is configured, the skill can request consent for device-based trial registration and store a reusable API key in ~/.zlbx/config.json.

Mitigation: Prefer manually configuring ZLBX_API_KEY; if auto-registration is used, confirm user consent first and protect the local config file.

Risk: The skill may display vendor recharge, referral, promotional, or update links during account and quota flows.

Mitigation: Review the skill before deployment and make external vendor links clear to users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/tender-search)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow](references/auto-register.md)
- [ZhiLiao BiaoXun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with REST request guidance, JSON examples, shell commands, and concise result tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based vendor auto-registration before data calls.]

## Skill Version(s):

2.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
