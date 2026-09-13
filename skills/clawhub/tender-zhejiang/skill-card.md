## Description:

Helps agents query and analyze Zhejiang-default tender notices, award results, procurement opportunities, company records, market statistics, price trends, and account status through Zhiliaobiaoxun data APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, bidding, sales, and market-analysis users can use this skill to search Zhejiang-default bid data, inspect company participation, identify expiring or proposed opportunities, compare purchasers, suppliers, brands, and prices, and check API account usage. The skill can also guide API request construction for agents that need structured tender and company data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary states that the skill can register a trial account from the runtime and send device-derived identifiers.

Mitigation: Require explicit user consent before auto-registration and prefer a managed ZLBX_API_KEY secret when available.

Risk: The security summary states that the skill creates and persists account credentials under ~/.zlbx/config.json.

Mitigation: Review local file permissions, avoid shared home directories for stored keys, and never print or ask users to paste API keys in chat.

Risk: The security guidance notes that users should expect occasional vendor links or referrals in responses.

Mitigation: Review outbound vendor links before following them and clearly distinguish data results from account, recharge, or referral links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/tender-zhejiang)
- [Zhiliaobiaoxun homepage](https://ai.zhiliaobiaoxun.com/?ch=s152)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON request examples, REST command guidance, and summarized API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a user-approved auto-registration flow; account and contact data may vary by account status.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
