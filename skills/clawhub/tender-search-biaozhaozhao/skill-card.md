## Description:

Searches tender and award notices by keyword and returns concise results with project names, amounts, and links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and suppliers use this skill to find Chinese tender and award notices, review project details, and optionally explore company and market data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Service requests use an API key that may be saved in a local configuration file.

Mitigation: Configure your own ZLBX_API_KEY, protect locally stored credentials, and review service access before use.

Risk: Optional account registration sends a hashed device identifier to the service.

Mitigation: Obtain explicit consent before registration or provide an existing API key to skip it.

Risk: Company contact lookups could enable bulk extraction or unsolicited outreach.

Mitigation: Limit lookups to a specific legitimate need and avoid bulk exports or unsolicited contact.

Risk: Comment-based request instructions may be easy to overlook.

Mitigation: Review the complete skill text, including comments, before allowing service requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/tender-search-biaozhaozhao)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Company registry API reference](references/api-registry.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Optional account registration guide](references/auto-register.md)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise Markdown summaries and linked result tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include project amounts, publication dates, company records, and source links.]

## Skill Version(s):

1.0.8 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
