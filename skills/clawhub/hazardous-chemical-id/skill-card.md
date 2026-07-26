## Description: <br>
Identifies whether queried chemicals are regulated as hazardous chemicals under Chinese standards and produces structured classification, regulatory-status, safety-measure, and emergency-response reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[709571520](https://clawhub.ai/user/709571520) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Safety engineers, compliance teams, and emergency-management staff use this skill to check chemical names, aliases, CAS numbers, or English names against Chinese hazardous-chemical regulations and generate single or batch identification reports. <br>

### Deployment Geography for Use: <br>
Global; regulatory content is specific to China. <br>

## Known Risks and Mitigations: <br>
Risk: Hazardous-chemical classifications, regulatory lists, or physical-property details may be outdated, incomplete, or inconsistent with the applicable MSDS. <br>
Mitigation: Verify generated reports against current official Chinese regulations, the relevant MSDS, and authoritative chemical databases before making safety or compliance decisions. <br>
Risk: When the named knowledge base does not cover a query, supplemental public chemical-database lookup can introduce source-quality variation. <br>
Mitigation: Require generated reports to identify their data sources and prefer official or regulator-maintained sources for unresolved chemicals. <br>


## Reference(s): <br>
- [Identification Workflow](artifact/references/identification-workflow.md) <br>
- [Regulations and Catalogs](artifact/references/regulations-and-catalogs.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Markdown report or summary table] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single chemical reports include 19 fields; batch queries are summarized in a table.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
