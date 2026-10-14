## Description:

Searches tender and award notices with combined keywords, exclusions, amounts, and other filters, then summarizes relevant results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and business-development users search tender notices, compare suppliers and companies, and review market activity using the vendor's data service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration sends a hashed device identifier to the vendor and saves an API key locally.

Mitigation: Ask for informed consent before registration; configure ZLBX_API_KEY beforehand to avoid automatic registration, and review ~/.zlbx/config.json for saved credentials.

Risk: Authenticated requests expose queries and package/source identity to the vendor; version checks add account calls.

Mitigation: Use the skill only if the vendor's receipt of authenticated requests and package metadata is acceptable; review requests and account activity.

Risk: Paid queries may consume credits and tender or company records may be incomplete or outdated.

Mitigation: Limit requests to the user's intended search, check credit usage, and verify consequential findings against original records.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/massive-tender-smart-search-biao800)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Business registry API reference](references/api-registry.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the vendor API and available account credits; contact numbers may be masked for trial accounts.]

## Skill Version(s):

1.0.9 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
