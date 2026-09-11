## Description:

Provides Chinese bidding and procurement search, company analysis, competitor discovery, market statistics, and account lookup guidance through the Zhiliao Biaoxun API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, market-analysis, and channel-development users use this skill to search Chinese bid notices, analyze companies and competitors, identify expiring or proposed opportunities, and summarize purchasing trends.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Procurement, company, supplier, competitor, and market-analysis queries are routed to a third-party service.

Mitigation: Install and use the skill only when users are comfortable sending those query terms to Zhiliao Biaoxun.

Risk: Auto-registration collects a stable MAC-derived device hash and stores a bearer API key locally.

Mitigation: Prefer a manually configured ZLBX_API_KEY; when auto-registration is needed, obtain user consent before collecting device features and protect the stored key.

Risk: Generated auto-login or recharge links and API keys can grant account access.

Mitigation: Treat links and keys as sensitive secrets, do not echo API keys to users, and avoid sharing generated login links outside the active session.

Risk: Contact details may be intentionally masked for free or trial accounts.

Mitigation: Display masked contacts as returned, explain the account limitation once, and do not use other channels to reconstruct masked phone numbers.

Risk: Responses may include occasional affiliated-service recommendations.

Mitigation: Keep such recommendations separate from the requested procurement analysis and avoid presenting them as neutral evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/china-national-bidding-zhongguozhaobiao)
- [Skill instructions](artifact/SKILL.md)
- [Bidding search API details](artifact/references/api-search.md)
- [Company analysis API details](artifact/references/api-company.md)
- [Market analysis API details](artifact/references/api-market.md)
- [Account lookup API details](artifact/references/api-account.md)
- [Auto-registration workflow](artifact/references/auto-register.md)
- [Zhiliao Biaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliao Biaoxun AI platform](https://ai.zhiliaobiaoxun.com/?ch=s52)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with concise tables, REST request examples, JSON payloads, and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY; may use a local ~/.zlbx/config.json API key and consent-gated auto-registration when no key is configured.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
