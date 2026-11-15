## Description:

Tracks data origin, transformations, and flow through construction systems for audit trails, compliance, and debugging data issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction)

### License/Terms of Use:

MIT

## Use Case:

Developers and construction data teams use this skill to create and explain data lineage tracking for project systems, including source registration, transformation records, upstream and downstream tracing, impact analysis, and audit-oriented reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exported lineage reports may expose internal system names, locations, owners, user identifiers, and operational workflow details.

Mitigation: Review reports before sharing and remove sensitive project, ownership, location, and workflow details that are not needed by the recipient.

Risk: The skill may need access to user-selected construction project data files.

Mitigation: Limit use to intended project files and confirm the data is appropriate for the agent session before processing.

## Reference(s):

- [DataDrivenConstruction homepage](https://datadrivenconstruction.io)
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/data-lineage-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown with structured tables, Python code, Mermaid diagrams, and JSON-style export examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize lineage statistics, validation issues, upstream or downstream traces, impact analysis, and export options.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
