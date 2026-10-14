## Description:

Searches Chinese procurement notices and company records to answer cross-region bidding, supplier, and market-analysis questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement analysts use this skill to find Chinese bidding notices, research companies and suppliers, and compare purchasing activity across regions and industries.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Automatic registration collects device-derived identifiers, creates a third-party account, and stores an API key locally.

Mitigation: Prefer a manually provided API key; require informed user consent before automatic registration and protect the stored key.

Risk: The skill performs account and update checks and may acknowledge notices after displaying them.

Mitigation: Review these requests before installation, disclose update notices to the user, and acknowledge only notices actually displayed.

Risk: Data requests can consume paid credits and company or contact information may be incomplete or masked.

Mitigation: Limit queries to the user's request, monitor credit use, and report only returned records without filling in masked details.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/national-procurement-data-center-caizhaowang)
- [Procurement search API](references/api-search.md)
- [Company analysis API](references/api-company.md)
- [Company registry API](references/api-registry.md)
- [Market analysis API](references/api-market.md)
- [Account and usage API](references/api-account.md)
- [Automatic registration and privacy guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available API data and account credits; contact details may be masked.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
