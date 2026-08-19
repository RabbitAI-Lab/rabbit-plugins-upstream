## Description:

全国采招大数据中心-采招网 helps agents search Chinese procurement notices and combine bid search, company profile, market aggregation, competitor, supplier, brand, and price-trend APIs for cross-province and cross-industry analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve and analyze Chinese procurement, bidding, supplier, purchaser, brand, pricing, and company-profile data. It is suited to procurement research, market sizing, competitor analysis, supplier discovery, and project follow-up workflows.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill can create or reuse a vendor account and collect a hashed device identifier after user consent when no API key is configured.

Mitigation: Configure ZLBX_API_KEY before use to avoid the onboarding flow, or review the consent prompt before allowing account setup.

Risk: The skill can persist an API key in ~/.zlbx/config.json.

Mitigation: Use a dedicated key, protect the local config file, and rotate or remove the key when access should end.

Risk: When trial quota is exhausted, the skill can generate an auto-login recharge link for billing recovery.

Mitigation: Treat recharge links as account-access links and verify the destination before opening or sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/national-procurement-data-center-caizhaowang)
- [API overview and usage guide](artifact/SKILL.md)
- [Account setup guide](artifact/references/account-setup.md)
- [Account API reference](artifact/references/api-account.md)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown with JSON request examples and API-derived summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a consent-gated vendor account setup flow; API responses may include procurement records, company information, account balance details, and billing or quota guidance.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
