## Description:

Helps agents source medical devices and consumables by querying Zhilia bidding data for notices, winning prices, purchaser and supplier details, brand rankings, and price trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research medical-device and consumable procurement opportunities, compare brands and models, inspect award prices, and review relevant purchaser, supplier, and company records from the Zhilia bidding data service.

### Deployment Geography for Use:

Global; data coverage and examples are focused on Chinese procurement and bidding records.

## Known Risks and Mitigations:

Risk: The skill handles API keys and can read or write local account configuration.

Mitigation: Configure ZLBX_API_KEY manually when possible, do not paste keys into chat, and review any local configuration before reuse or sharing.

Risk: The optional trial registration flow sends device-derived fields, including a MAC-address hash, to support account creation.

Mitigation: Use auto-registration only after explicit consent; choose manual account setup if device-derived registration is not acceptable.

Risk: Contact lookup and account links can expose sensitive business contact or account information.

Mitigation: Treat generated login, recharge, and contact data as sensitive; preserve masked contacts as returned and avoid bulk contact export.

Risk: The security scan verdict is suspicious due to broad credential, device, contact, and referral-link behavior.

Mitigation: Review the skill before installation and limit use to deployments that need the broad Zhilia procurement-intelligence integration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thuanlynham-stack/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [API Overview and Tool List](SKILL.md)
- [Bid Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Auto-Registration Flow](references/auto-register.md)
- [Zhilia API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Manual Account and Recharge Portal](https://ai.zhiliaobiaoxun.com/?ch=s37)
- [Zhilia Business Agent](https://agent.zhiliaobiaoxun.com?utm_source=skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with result tables, JSON request examples, REST command guidance, and configuration notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or local configuration; optional trial registration is consent-gated and may create local account configuration.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
