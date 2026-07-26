## Description: <br>
Track data origin, transformations, and flow through construction systems. Essential for audit trails, compliance, and debugging data issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction data teams, developers, and analysts use this skill to trace project data origins, transformations, and downstream dependencies for audit trails, compliance reviews, issue resolution, and change impact analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lineage exports may expose internal systems, owners, locations, and data-flow relationships. <br>
Mitigation: Review exported lineage data before sharing and store it using the same access controls used for sensitive project records. <br>
Risk: The skill may work with user-selected project data and filesystem paths. <br>
Mitigation: Use only intended project inputs, validate file paths before processing, and avoid granting access to unrelated directories. <br>
Risk: Server release metadata lists version 2.1.0 while artifact configuration lists 2.0.0. <br>
Mitigation: Verify the release version and provenance before relying on exact version identity for compliance or audit records. <br>


## Reference(s): <br>
- [Data Driven Construction homepage](https://datadrivenconstruction.io) <br>
- [Data Lineage Tracker on ClawHub](https://clawhub.ai/datadrivenconstruction/skills/data-lineage-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured tables, Python code snippets, JSON-style export guidance, and optional Mermaid lineage diagrams] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include summary statistics, key findings, validation issues, and export suggestions for CSV, Excel, or JSON when relevant.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
