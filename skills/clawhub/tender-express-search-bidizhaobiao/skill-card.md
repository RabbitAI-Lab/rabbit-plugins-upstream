## Description:

Searches local Chinese procurement notices by province, city, or region and returns recent announcements with available budget amounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and other external users search Chinese provincial and city-level tender announcements with location filters, review recent opportunities and budgets, and optionally investigate companies or market trends.

### Deployment Geography for Use:

Global (search coverage focuses on Chinese provincial and city-level procurement)

## Known Risks and Mitigations:

Risk: Search and optional registration information is sent to the Zhiliaobiaoxun/Bidizhaobiao service.

Mitigation: Review the destination and submitted data before use; avoid sharing sensitive search or registration details.

Risk: Automatic registration uses device-derived identifiers and stores an API key locally.

Mitigation: Ask for consent before registration; set ZLBX_API_KEY manually to avoid device-based registration and protect the local key.

Risk: Company, contact, account, and market features extend beyond local tender search and may consume credits.

Mitigation: Use only the requested features and check credit costs before making additional queries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/tender-express-search-bidizhaobiao)
- [Provider skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](artifact/references/api-search.md)
- [Automatic registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with tender summaries and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Location-filtered results are presented newest first, with budget amounts when available.]

## Skill Version(s):

2.0.5 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
