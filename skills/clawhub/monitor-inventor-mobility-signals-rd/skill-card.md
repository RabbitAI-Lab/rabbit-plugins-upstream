## Description:

Monitors public patent records for inventor identity, organizational-association, and technical-adjacency signals that authorized IP or R&D teams can review in an evidence-backed HTML briefing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized IP, legal, and R&D teams use this skill to scope public patent-record monitoring, resolve inventor identities from evidence, classify review priority, and render a reviewed HTML briefing without inferring employment, resignation, misconduct, or legal risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Named-inventor monitoring can be misused for employee scoring, surveillance, or adverse employment decisions.

Mitigation: Use only for authorized IP, R&D, or legal workflows after confirming lawful purpose, jurisdictions, access limits, retention and deletion controls, and a qualified human review path.

Risk: Patent records can be misread as proof of employment, resignation, misconduct, ownership, or legal risk.

Mitigation: Present outputs only as public-record review priorities, keep non-employment and non-legal disclaimers prominent, and route material decisions to qualified IP, legal, HR, or employment reviewers.

Risk: Publication lag, incomplete coverage, same-name inventors, and unresolved identities can make patent-record signals incomplete or misleading.

Mitigation: Document cutoff dates, search coverage, pagination, identity status, counterevidence, and uncertainty; use insufficient_evidence when identity or retrieval cannot support a review priority.

## Reference(s):

- [Inventor Mobility Signals Workflow](references/workflow.md)
- [Inventor Mobility Signal Report Schema](references/data_schema.json)
- [PatSnap Patent Search MCP Server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP Server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, Files]

**Output Format:** [Text research protocol and schema-validated HTML briefing generated from reviewed JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires reviewed JSON matching references/data_schema.json; generated HTML escapes supplied content and refuses overwrite unless forced.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
