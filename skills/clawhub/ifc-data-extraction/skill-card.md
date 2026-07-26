## Description: <br>
Extract structured data from IFC (Industry Foundation Classes) files using IfcOpenShell. Parse BIM models, extract quantities, properties, spatial relationships, and export to various formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, BIM specialists, and construction data teams use this skill to extract structured project, element, quantity, material, geometry, and spatial relationship data from IFC models for analysis and reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The database export path can write to SQL tables and replace existing table contents when a connection string is provided. <br>
Mitigation: Prefer local CSV, Excel, JSON, pandas, or local SQLite exports; use database credentials only when table replacement is intended and acceptable. <br>
Risk: IFC model exports may contain sensitive building, project, or asset information. <br>
Mitigation: Use this skill only with IFC files and output destinations approved for the model data being extracted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/ifc-data-extraction) <br>
- [Publisher profile](https://clawhub.ai/user/datadrivenconstruction) <br>
- [IfcOpenShell](https://ifcopenshell.org) <br>
- [buildingSMART Industry Foundation Classes](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/) <br>
- [Data Driven Construction](https://datadrivenconstruction.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python code examples and structured extraction guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides local IFC parsing and exports to pandas DataFrames, CSV, Excel, JSON, and optional SQL tables.] <br>

## Skill Version(s): <br>
2.0.0 (source: artifact/claw.json and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
