## Description:

Finds relevant, currently valid invention patents held by universities and research institutes, then groups and shortlists them for potential transfer, licensing, or research collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Businesses and technology-transfer teams use this skill to identify university and research-institute patents relevant to a technical need, compare promising institutions, and prepare a shortlist for transfer or licensing discussions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Technical searches and descriptions are sent to an external patent-search service.

Mitigation: Avoid including confidential formulas, source code, trade secrets, or unpublished invention details unless their transmission is authorized.

Risk: Changing the configured service endpoint can route searches and credentials to an untrusted destination.

Mitigation: Keep PATENTMAX_BASE_URL unset unless the alternative endpoint is fully trusted.

Risk: Exported CSV content may trigger spreadsheet formulas when opened.

Mitigation: Treat exported CSV files as untrusted spreadsheet content and review or sanitize cells before opening them.

Risk: Patent ownership and legal status may change, and search results cannot establish whether licensing has already occurred.

Mitigation: Confirm current legal status against official patent records and verify licensing arrangements before transfer discussions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/university-patent-transfer)
- [Search workflow](artifact/references/search-workflow.md)
- [PatentMax API reference](artifact/references/api-reference.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Text, CSV files, Guidance]

**Output Format:** [Markdown summary and Excel-compatible UTF-8 CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Groups shortlisted patents by institution and highlights candidates for follow-up.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
