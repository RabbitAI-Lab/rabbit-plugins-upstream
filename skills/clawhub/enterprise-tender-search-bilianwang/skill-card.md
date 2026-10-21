## Description:

Searches Chinese procurement and tender notices, supplier histories, company records, and market trends to support sourcing decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, and supplier-sourcing teams use this skill to find Chinese tender opportunities, examine company and supplier activity, and summarize purchasing trends.

### Deployment Geography for Use:

Global; procurement data focuses on China

## Known Risks and Mitigations:

Risk: Broad request routing may send procurement queries, company names, and source metadata to the third-party service.

Mitigation: Review which requests invoke the skill and avoid sending confidential procurement or company information without approval.

Risk: API keys can be stored locally and credentialed account checks can expose account details on shared devices.

Mitigation: Prefer your own ZLBX_API_KEY and review access to ~/.zlbx/config.json on shared machines.

Risk: Automatic registration sends a hashed device identifier to the vendor.

Mitigation: Obtain informed consent before registration; use the manual account option if device identification is unacceptable.

Risk: Operational callbacks may acknowledge an upgrade notice before the user has seen it.

Mitigation: Show any upgrade notice to the user before submitting a display acknowledgment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-tender-search-bilianwang)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Company registry data reference](artifact/references/api-registry.md)
- [Account registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and result tables with source links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an API key; some data queries consume account credits.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
