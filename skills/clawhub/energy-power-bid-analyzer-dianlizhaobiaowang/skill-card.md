## Description:

能源电力采招分析仪-电力招标网，当查询词包含电网、电力、新能源、光伏、储能、风电时触发，需重点针对国网/南网等大型央企采购项目进行聚合，分析特定能源设备或工程的中标集中度。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, and market analysts use this skill to search and analyze energy and power bidding records, especially State Grid, China Southern Power Grid, new energy, photovoltaic, energy storage, and wind-power procurement activity. It supports bid search, company analysis, market concentration analysis, account status checks, and guided API-key setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic account setup may send a hardware-derived device identifier to the vendor.

Mitigation: Use a manually provisioned ZLBX_API_KEY when possible, or confirm user consent before any automatic registration flow.

Risk: Normal responses may include vendor referral or recharge links.

Mitigation: Review generated user-facing output for vendor links and disclose that they are vendor-provided account or recharge links.

Risk: The security verdict is suspicious.

Mitigation: Review the skill before installation, limit API-key permissions where possible, and monitor account usage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thuanlynham-stack/skills/energy-power-bid-analyzer-dianlizhaobiaowang)
- [Artifact skill definition](artifact/SKILL.md)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with tables, JSON API payloads, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY when available and may guide the user through API-key setup.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
