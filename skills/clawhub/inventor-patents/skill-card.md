## Description:

Finds a named inventor's published patents, separates namesakes by organization, identifies inventor order, and prepares an Excel-compatible patent list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, inventors, and applicants use this skill to compile public patent records for CVs, grant applications, and professional reviews, distinguishing people with the same name by organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventor names, organizations, patent queries, and technical search text are sent to PatentMax/ip930.com.

Mitigation: Use only when external API processing is acceptable; do not submit confidential technical details.

Risk: The included client exposes broader search, analytics, billing, and credential functions than inventor-list export alone.

Mitigation: Review the client before installing, limit use to the needed commands, and confirm potential charges before paid operations.

Risk: Changing PATENTMAX_BASE_URL can redirect requests and credentials to another destination.

Mitigation: Do not set PATENTMAX_BASE_URL unless you fully trust the destination.

Risk: People with the same name, including those at one organization, may be misattributed in a patent list.

Mitigation: Group results by organization, flag uncertain matches for the inventor to confirm, and check formal claims against official patent records.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/inventor-patents)
- [PatentMax API reference](references/api-reference.md)
- [PatentMax query syntax](references/query-syntax.md)
- [PatentMax client tools](references/tools.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [CSV files, Text summaries, Search queries]

**Output Format:** [UTF-8 CSV and Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes search scope, organization-based namesake handling, inventor order, and a source note; uncertain identity requires confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
