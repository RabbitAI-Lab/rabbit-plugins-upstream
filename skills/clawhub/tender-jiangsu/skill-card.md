## Description:

This skill helps agents query and analyze Jiangsu-focused tender, award, company, market, account, and procurement opportunity data through the Zhiliaobiaoxun API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development, procurement, bidding, and market analysis teams use this skill to search tender and award notices, inspect company bidding history, identify competitors or potential suppliers, and check account balance or usage. The skill defaults searches to Jiangsu when the user has not specified a region, while preserving user-specified regions and industries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional automatic registration may send platform, CPU architecture, and a hashed MAC-derived device identifier for trial-account deduplication.

Mitigation: Configure ZLBX_API_KEY manually to avoid automatic device-feature collection, or proceed only after the user has explicitly consented.

Risk: The skill may persist an API key in ~/.zlbx/config.json after successful automatic registration.

Mitigation: Treat ~/.zlbx/config.json as a credential file and avoid exposing API keys in chat, logs, or shared artifacts.

Risk: Broad company matching, regional defaults, and amount filters can affect search scope and business conclusions.

Mitigation: Report the actual filters used, surface fuzzy or broad matches when relevant, and review high-impact results before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/tender-jiangsu)
- [Zhiliaobiaoxun homepage](https://ai.zhiliaobiaoxun.com/?ch=s151)
- [Search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured summaries, tables, JSON request examples, REST API calls, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or consent-gated automatic registration before authenticated API use.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
