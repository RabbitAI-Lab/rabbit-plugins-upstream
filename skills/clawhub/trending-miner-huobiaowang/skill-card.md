## Description:

Analyzes tender and award records to identify industry trends, leading purchasers, and frequently awarded projects through the Zhiliaobiaoxun service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, market analysts, and other external users can explore tender activity, compare purchasers and suppliers, and summarize market concentration and bidding trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account registration can send a MAC-hash-derived device identifier to an external bidding-data service.

Mitigation: Obtain informed user consent before registration; offer the manual key application route if declined.

Risk: An API key is stored in a local configuration file and used for service requests.

Mitigation: Protect the local key file and never expose the key in responses or shared output.

Risk: Company contacts and account or billing details are accessible beyond aggregate tender trends.

Mitigation: Request only data needed for the user's task, respect masked contact details, and avoid bulk contact exports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/trending-miner-huobiaowang)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Market analysis API reference](references/api-market.md)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Company registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Account registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summaries and linked result tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes query filters and source links when available; contact numbers may be masked for free accounts.]

## Skill Version(s):

2.1.7 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
