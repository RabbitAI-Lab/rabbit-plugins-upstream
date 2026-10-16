## Description:

Searches Chinese tender and award notices and helps analyze procurement opportunities, companies, competitors, suppliers, and market trends using ZLBX data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and business-development teams use this skill to find Chinese tender opportunities, review award history, and assess suppliers, competitors, and purchasing trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and company queries are sent to the ZLBX service.

Mitigation: Avoid submitting sensitive queries unless sharing them with the service is acceptable.

Risk: Automatic trial registration shares a hashed device identifier and persists a service API key locally.

Mitigation: Prefer manually configuring ZLBX_API_KEY; use automatic registration only with consent and protect the stored credential.

## Reference(s):

- [ClawHub tender-search release](https://clawhub.ai/liu-jiapeng/skills/tender-search)
- [ZLBX skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Registration and account setup](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tender filters, company comparisons, and procurement statistics.]

## Skill Version(s):

2.1.9 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
