## Description:

Helps analyze Chinese government procurement notices, awards, suppliers, buyers, market trends, and upcoming opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement analysts and business development teams use the skill to find Chinese public-sector tenders and awards, assess buyers and suppliers, and examine pricing and market trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration transmits a persistent hashed MAC-derived device identifier to the procurement-data service for trial deduplication.

Mitigation: Review the privacy behavior and consent before auto-registration; configure ZLBX_API_KEY yourself to avoid the automatic registration flow.

Risk: Automatic registration stores the returned API key locally in ~/.zlbx/config.json.

Mitigation: Prefer a trusted secret mechanism for ZLBX_API_KEY; if auto-registration is used, review the local configuration and treat the stored key as a secret.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bigdata-analyzer)
- [Publisher skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Procurement search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Company registry API reference](artifact/references/api-registry.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration and privacy guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance]

**Output Format:** [Markdown with linked results and summary tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results state applied filters and monetary units; data access requires an API key and may use account credits.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
