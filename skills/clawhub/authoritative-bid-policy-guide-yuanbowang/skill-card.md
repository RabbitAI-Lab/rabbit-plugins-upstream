## Description:

Helps analyze Chinese procurement notices, major infrastructure projects, and public-sector purchasing trends using bid-search and aggregation data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement analysts and business users use this skill to find bid notices, examine companies and market activity, and prepare sourced market briefs for Chinese public procurement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration sends device-derived characteristics to the provider for trial-account deduplication.

Mitigation: Obtain explicit consent before registration; users can configure their own ZLBX_API_KEY to skip device collection.

Risk: An automatically issued API key is stored on the local device.

Mitigation: Protect access to ~/.zlbx/config.json, avoid disclosing the key in chat, and prefer a manually configured key if local persistence is unwanted.

Risk: Contact lookup and account or billing actions may expose sensitive contact data or incur charges.

Mitigation: Ask before contact lookup or account and billing actions; preserve masked contact details and confirm paid queries before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/authoritative-bid-policy-guide-yuanbowang)
- [Bid search API reference](artifact/references/api-search.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Account and consumption API reference](artifact/references/api-account.md)
- [Registration and credential handling reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include search filters, bid counts, dates, and amounts in ten-thousand-yuan units.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
