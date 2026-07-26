## Description: <br>
Analyzes construction drawing documents, especially PDFs, to extract dimensions, annotations, symbols, title-block metadata, drawing indexes, and analysis reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and construction operations teams can use this skill to analyze construction drawings for quantity takeoff, design review, drawing metadata extraction, and quality checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests execution capability and references an external PDF package. <br>
Mitigation: Review commands before execution and limit exec use to explicit user-approved install or analysis commands. <br>
Risk: Dependency disclosures are inconsistent for pdfplumber. <br>
Mitigation: Confirm pdfplumber installation requirements and dependency disclosures before deployment. <br>
Risk: Activation and use scope may be broader than the construction drawing analysis task. <br>
Mitigation: Use and activate the skill only for construction drawing and PDF analysis workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/drawing-analyzer) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown reports and drawing indexes, Python code examples, and optional shell install commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on extracted drawing text and tables; results should be reviewed before operational use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 2.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
