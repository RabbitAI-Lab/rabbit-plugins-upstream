## Description:

Helps agents query Lubanlebiao/Zhiliaobiaoxun procurement data for construction materials, including bid notices, historical unit prices, top brands, suppliers, company records, contacts, and account status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, bidding, sales, and market-analysis users can ask an agent to search Chinese tender and award data, compare construction-material prices, identify major brands and suppliers, analyze companies, and check account usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use broader procurement, company, contact, account, and vendor-referral workflows than the construction-material description alone suggests.

Mitigation: Review the exposed workflows before installation and restrict use to approved procurement and market-analysis tasks.

Risk: Automatic registration can collect a MAC-address hash for device deduplication and store an API key locally.

Mitigation: Prefer supplying a manually created API key through a standard secret store; allow automatic registration only after users accept the device-tracking and local-credential behavior.

Risk: Security evidence marks the release as suspicious because requested access and setup behavior are broader than the description clearly supports.

Mitigation: Review before installing, especially in enterprise environments, and verify that API-key handling, quota use, and contact-data access match organizational policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thuanlynham-stack/skills/construction-material-bid-assistant-lubanlebiao)
- [Skill Definition](artifact/SKILL.md)
- [Bid Search API Reference](artifact/references/api-search.md)
- [Company Analysis API Reference](artifact/references/api-company.md)
- [Market Analysis API Reference](artifact/references/api-market.md)
- [Account API Reference](artifact/references/api-account.md)
- [Automatic Registration Reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with tables, JSON request examples, REST API calls, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local ~/.zlbx/config.json API key; some account and contact responses depend on service-side entitlement and quota.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
