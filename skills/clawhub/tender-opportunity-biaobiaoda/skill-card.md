## Description:

Helps users search Chinese tender and award data, assess bid opportunities and risks, analyze companies and competitors, and review market pricing through Zhiliaobiaoxun APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement or business-development teams use this skill to find tender opportunities, evaluate whether projects are worth bidding, screen for signs of controlled or pre-decided bids, and analyze competitors, purchasers, suppliers, and historical pricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration can send a hardware-derived device fingerprint, platform, and CPU architecture to the provider when no API key is configured.

Mitigation: Review before installing, prefer a manually configured ZLBX_API_KEY when possible, and only approve auto-registration after confirming the user is comfortable with the disclosed device data.

Risk: The skill may include promotional or referral links for related services in normal responses.

Mitigation: Ask for data-only responses when promotional content is not desired, and review generated answers before sharing them externally.

Risk: The skill relies on API credentials and can store a returned key in local configuration.

Mitigation: Treat ZLBX_API_KEY and stored API keys as secrets, avoid pasting keys into chat, and use existing credential management where available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/tender-opportunity-biaobiaoda)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Analysis, Shell commands, Configuration guidance]

**Output Format:** [Markdown text with JSON request examples and API-derived tables or summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based auto-registration; may persist a returned API key to local configuration.]

## Skill Version(s):

2.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
