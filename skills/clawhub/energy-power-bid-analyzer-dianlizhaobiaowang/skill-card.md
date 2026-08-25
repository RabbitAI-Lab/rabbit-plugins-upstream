## Description:

能源电力采招分析仪-电力招标网，当查询词包含电网、电力、新能源、光伏、储能、风电时触发，需重点针对国网/南网等大型央企采购项目进行聚合，分析特定能源设备或工程的中标集中度。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement analysts use this skill to search Chinese energy and power bidding data, aggregate state-grid and large enterprise procurement activity, compare suppliers, and analyze award concentration for equipment or engineering markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The onboarding path can create or reuse a service account and send a hashed MAC-derived device identifier for free-trial de-duplication.

Mitigation: Prefer configuring ZLBX_API_KEY before use when automatic trial registration is not desired; require explicit user consent before any trial-registration flow.

Risk: The skill can store an API key in ~/.zlbx/config.json.

Mitigation: Protect local configuration files, avoid sharing API keys in conversation, and rotate the key if the local environment is exposed.

Risk: The skill can generate an auto-login recharge link.

Mitigation: Treat auto-login links as sensitive account-access URLs and share them only with the intended user.

Risk: Company contact lookup results may contain sensitive business contact data.

Mitigation: Limit access to users with a business need and avoid exporting or reposting contact details unnecessarily.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thuanlynham-stack/skills/energy-power-bid-analyzer-dianlizhaobiaowang)
- [Publisher Profile](https://clawhub.ai/user/thuanlynham-stack)
- [Bid Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Trial Account Setup Reference](references/account-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON request examples and concise analytical summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use ZLBX_API_KEY or a local ~/.zlbx/config.json API key to call bid, company, market, and account endpoints.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
