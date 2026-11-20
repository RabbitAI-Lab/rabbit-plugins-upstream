## Description:

Enriches user-provided lead lists with business email contacts, available business phone details, source references, and email status labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[summerzb](https://clawhub.ai/user/summerzb)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, marketing, and business development users can enrich lawfully obtained company lead lists with work email contacts, available business phone numbers, source references, and clear status labels. The skill is intended for public or user-authorized sources and excludes personal mobile number collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill could be used on lead lists the user is not authorized to process.

Mitigation: Use it only for business contact enrichment on user-owned or lawfully obtained lists, and confirm ambiguous requests before proceeding.

Risk: Contact discovery could drift into scraping restricted platforms or bypassing access controls.

Mitigation: Use only public information and official or user-authorized channels; do not bypass logins, captchas, or platform restrictions.

Risk: Inferred email addresses may be inaccurate or unsuitable for direct outreach.

Mitigation: Label inferred addresses as unverified, use MX checks where permitted, and include the source or reasoning for each row.

Risk: Business contact enrichment can over-collect personal data.

Mitigation: Limit collection to work contact details and do not collect personal mobile numbers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/summerzb/skills/lead-enrichment)
- [Qichacha official MCP endpoint](https://mcp.qcc.com/basic/stream)
- [CNINFO announcement query endpoint](https://www.cninfo.com.cn/new/hisAnnouncement/query)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown table with source references, email status labels, and summary counts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rows include company, contact, email, email status, phone, and source; inferred emails are labeled separately from sourced emails.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
