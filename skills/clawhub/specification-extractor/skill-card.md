## Description: <br>
Extract structured data from construction specifications. Parse CSI sections, requirements, submittals, and product data from spec documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction project managers, estimators, procurement teams, and developers use this skill to extract CSI sections, product requirements, submittals, referenced standards, and summary reports from construction specification documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read sensitive construction specification files supplied by the user. <br>
Mitigation: Point it only at intended project documents and avoid unrelated private files. <br>
Risk: Extracted reports or exported CSV, Excel, or JSON files may contain project-sensitive data or imperfect extraction results. <br>
Mitigation: Review generated outputs for accuracy and confidentiality before sharing. <br>
Risk: PDF extraction quality can vary with document formatting and text extraction behavior. <br>
Mitigation: Validate inputs, inspect parsing errors, and confirm key CSI sections, submittals, products, and standards against the source document. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/specification-extractor) <br>
- [Data Driven Construction homepage](https://datadrivenconstruction.io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance, Configuration] <br>
**Output Format:** [Markdown tables, structured text, Python code examples, and optional CSV, Excel, or JSON export guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read user-provided construction specification files; PDF extraction examples require python3 and pdfplumber.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata; artifact/claw.json lists 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
