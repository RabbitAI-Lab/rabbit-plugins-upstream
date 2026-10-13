## Description:

Helps agents find healthcare procurement notices, identify hospital purchasers and winning suppliers, and analyze a hospital's leading suppliers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Healthcare procurement teams and suppliers use this skill to search Chinese hospital bids, identify purchasing hospitals and winning companies, and compare a hospital's main suppliers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If no API key is configured, enrollment may use device-derived features and save a new account key locally.

Mitigation: Configure your own ZLBX_API_KEY to avoid device-linked registration; otherwise require informed consent and protect the locally stored key.

Risk: Company, contact, market, and account queries extend beyond the advertised hospital-bid focus and may expose sensitive contact details.

Mitigation: Limit queries to the user's request, preserve masked contact information, and avoid bulk contact exports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thuanlynham-stack/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account setup and registration](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Zhiliaobiaoxun API key; available details depend on the account and service responses.]

## Skill Version(s):

1.0.8 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
