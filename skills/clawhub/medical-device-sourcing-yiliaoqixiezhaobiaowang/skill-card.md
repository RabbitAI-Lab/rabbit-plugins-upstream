## Description:

Helps agents query Zhiliaobiaoxun procurement APIs for medical-device and consumables sourcing, including bid search, company intelligence, purchaser and supplier rankings, brand analysis, and price trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement analysts use the skill to source medical devices and related supplies, compare historical winning bid prices, identify purchasing units and suppliers, and analyze company or market activity in Chinese procurement data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The published medical-device sourcing description under-discloses a broader procurement, company-intelligence, contact lookup, account registration, and referral workflow.

Mitigation: Review the skill before installation, disclose the broader connector scope to users, and restrict use to intended procurement-intelligence tasks.

Risk: Auto-registration can collect device-derived features and store a vendor API key in ~/.zlbx/config.json.

Mitigation: Prefer a user-managed ZLBX_API_KEY, require explicit consent before auto-registration, and check local config file permissions if auto-registration is used.

Risk: The skill can query contact and procurement data that may be sensitive or account-tier restricted.

Mitigation: Use returned contact fields as provided, respect masking and account limits, and avoid enriching masked contact data from other channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thuanlynham-stack/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, JSON, guidance]

**Output Format:** [Markdown summaries with JSON request and response details when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bid tables, company and market analysis, account status, and concrete API request examples.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
