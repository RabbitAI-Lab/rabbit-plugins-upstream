## Description:

Explains a single patent in plain language, including its claims, reported legal status, and similar patents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent researchers, inventors, and other users can supply a patent number to receive a plain-language explanation of its claims, reported legal status, and comparable patents. The skill also creates an Excel-compatible patent summary card; it does not make infringement determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent identifiers, search queries, technical descriptions, and API credentials may be sent to a configurable remote service.

Mitigation: Confirm the service endpoint before use and share confidential invention details only when that data transfer is acceptable.

Risk: Trial keys, task state, cached patent data, and generated reports may remain on disk.

Mitigation: Review and remove local patent data and credentials when they are no longer needed.

Risk: Reported legal status and estimated expiry may be incomplete or mistaken for legal advice.

Mitigation: Check the official patent register and seek qualified advice for legal or infringement decisions.

## Reference(s):

- [Patent explainer release](https://clawhub.ai/ip930/skills/patent-explainer)
- [PatentMax API reference](references/api-reference.md)
- [PatentMax search workflow](references/search-workflow.md)

## Skill Output:

**Output Type(s):** [Text, CSV file]

**Output Format:** [Plain-language response and UTF-8 CSV (Excel-compatible)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes claim feature breakdowns, reported legal status, estimated expiry year, similar patents, and source labels.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
