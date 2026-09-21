## Description:

Helps agents query and analyze Guangdong-focused tender, award, company, market, account, and procurement opportunity data through Zhiliaobiaoxun APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, bid, sales, and market-analysis users use this skill to search Chinese tender and award notices, inspect company bidding activity, find opportunities, and analyze Guangdong-centered procurement markets. The skill can also help agents check account balance and guide API key setup for the Zhiliaobiaoxun service.

### Deployment Geography for Use:

Global; data workflows are focused by default on Guangdong, China.

## Known Risks and Mitigations:

Risk: The skill may call Zhiliaobiaoxun APIs and use or create a vendor API key.

Mitigation: Configure an existing ZLBX_API_KEY when available, and do not ask users to paste or disclose API keys in chat.

Risk: The automatic registration flow may collect limited device features and store the resulting API key in ~/.zlbx/config.json.

Mitigation: Run automatic registration only after user consent, and offer manual key setup through the vendor portal as an alternative.

Risk: Procurement and company-contact outputs can contain business-sensitive or paid-account data.

Mitigation: Review returned contact and account information before sharing it externally, and follow the user's organization policy for procurement intelligence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/tender-guangdong)
- [Zhiliaobiaoxun portal](https://ai.zhiliaobiaoxun.com/?ch=s150)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Configuration guidance]

**Output Format:** [Markdown responses with API-backed summaries, tables, links, JSON request examples, and setup guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or consent-gated account setup; responses may include procurement records, company facts, market aggregates, account status, and follow-up query guidance.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
