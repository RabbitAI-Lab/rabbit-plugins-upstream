## Description:

Tender Search helps agents query and analyze tender and bid data, including notices, awards, expiring projects, company profiles, competitors, suppliers, purchasers, brands, and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, and sales or business development teams use this skill to search tender opportunities, analyze companies and competitors, and summarize market activity from Zhiliaobiaoxun data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auto-registration collects persistent device-identifying metadata for trial account creation.

Mitigation: Prefer a manually configured ZLBX_API_KEY; if auto-registration is used, require clear user consent before collecting platform, CPU architecture, or MAC hash data.

Risk: The returned API key may be stored locally and used for paid vendor API access.

Mitigation: Store the key in a protected local configuration or environment variable, avoid exposing it in chat or logs, and rotate it if disclosure is suspected.

Risk: Recharge and referral links may direct users into vendor billing or account flows.

Mitigation: Show the destination clearly, use only documented Zhiliaobiaoxun URLs, and let users decide whether to continue with billing or account recovery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/tender-search)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)
- [Zhiliaobiaoxun data API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account portal](https://ai.zhiliaobiaoxun.com/?ch=s21)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown text with JSON request examples, REST/API call guidance, and summarized query results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY for live API calls; may include tender, company, account, and market data returned by the vendor service.]

## Skill Version(s):

2.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
