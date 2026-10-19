## Description:

Analyzes a patent's backward and forward citations, supplementing incomplete citation data with clearly labeled similar patents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent researchers and analysts use this skill to trace prior patents cited by a target patent and later patents that cite it, with separately identified similar patents where citation coverage is sparse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent numbers, search terms, and technical descriptions may be sent to PatentMax/ip930.com.

Mitigation: Do not submit confidential invention details unless disclosure to this third party is acceptable.

Risk: API credentials and patent queries may be sent to a configurable external endpoint.

Mitigation: Avoid setting PATENTMAX_BASE_URL unless you deliberately control and trust that endpoint.

## Reference(s):

- [ClawHub release](https://clawhub.ai/ip930/skills/patent-citation-map)
- [PatentMax API reference](artifact/references/api-reference.md)
- [PatentMax search workflow](artifact/references/search-workflow.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Text analysis, CSV file]

**Output Format:** [Concise text summary and UTF-8 CSV with BOM]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates actual citations from similar patents and names PatentMax as the data source.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
