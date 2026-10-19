## Description:

Searches Chinese healthcare procurement notices and analyzes hospital buyers, awarded suppliers, and supplier trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Healthcare procurement and sales teams use this skill to find Chinese tender opportunities, identify hospital buyers and winning suppliers, and compare supplier activity.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Automatic trial registration sends device-derived information to a third-party service.

Mitigation: Review the registration terms and obtain consent first; configure your own ZLBX_API_KEY to avoid device-based registration.

Risk: Automatic registration stores an API key in a local configuration file.

Mitigation: Prefer setting ZLBX_API_KEY yourself and protect any locally stored credentials.

Risk: Contact and company-intelligence lookups may consume account credits.

Mitigation: Check the account balance and applicable credit charges before making those lookups.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [Skill installation documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Company API reference](artifact/references/api-company.md)
- [Market API reference](artifact/references/api-market.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available procurement records and account credits.]

## Skill Version(s):

1.0.10 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
