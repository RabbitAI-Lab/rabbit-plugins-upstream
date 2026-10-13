## Description:

Helps analyze transit and infrastructure procurement notices, bidders, suppliers, brands, and market trends using the vendor's procurement data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and market analysts use this skill to find transit and infrastructure tenders, assess potential bidders and suppliers, and compare awarded brands, prices, and market activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement and company queries are sent to a third-party service.

Mitigation: Avoid sending sensitive business queries unless the vendor's data handling is acceptable.

Risk: First-use auto-registration can use device fingerprints and persist an account key locally.

Mitigation: Configure your own ZLBX_API_KEY before first use to avoid device fingerprint auto-registration, and review local key storage.

Risk: Company expansion, contact lookup, and web enrichment can widen the scope of a query beyond transit procurement.

Mitigation: Review those lookups before sensitive workflows and verify any supplemental information against its source.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/smart-transit-rail-bid-analyzer)
- [Procurement search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account registration and privacy notes](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports applied filters and distinguishes available procurement data from supplementary web information.]

## Skill Version(s):

1.0.7 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
