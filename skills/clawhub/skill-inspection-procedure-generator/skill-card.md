## Description: <br>
Generates product inspection procedure Word documents from user-provided control plans, test reports, drawings, and written product requirements, with structured data validation and missing-field handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality engineers, manufacturing teams, and developers use this skill to extract inspection information from product materials, organize it as JSON, and generate incoming inspection procedures, IQC specifications, or product quality inspection standards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes generated JSON and .docx files to local paths, which could overwrite an existing file if the output path is reused. <br>
Mitigation: Review the JSON and .docx output paths before running the document generator. <br>
Risk: Incomplete product information can lead to draft inspection procedures with unresolved fields. <br>
Mitigation: Ask for missing critical product and inspection data, mark unresolved fields as "待确认", and review the generated summary before using the document. <br>
Risk: Product and quality documents may contain sensitive business or engineering information. <br>
Mitigation: Use the skill only with product and quality documents that are appropriate to process locally. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-inspection-procedure-generator) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-inspection-procedure-generator) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>
- [Data schema reference](references/data-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON data structures, shell command examples, and generated .docx files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write JSON input files and Word .docx output files to user-specified local paths.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
