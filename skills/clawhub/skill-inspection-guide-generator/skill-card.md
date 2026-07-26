## Description: <br>
Generates standardized SIP inspection-guide spreadsheets from product technical files, using a valid uploaded Excel or Word template when available and a general format otherwise. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality engineers, manufacturing teams, and supplier-quality reviewers use this skill to turn product specifications, test reports, quality requirements, and optional templates into a structured inspection guide. It is intended for workflows that need inspection items, methods, standards, frequencies, and related notes organized into an Excel SIP file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Input technical documents and templates may contain confidential product, supplier, pricing, or quality data. <br>
Mitigation: Review and redact user-provided files before processing, and only include details needed for the inspection guide. <br>
Risk: Generated spreadsheets are saved to the local output directory and may be left in an unintended location. <br>
Mitigation: Choose an appropriate working directory, restrict file access as needed, and review the generated file path before sharing. <br>
Risk: Some inspection standards may be unclear in the source documents and require human confirmation. <br>
Mitigation: Keep entries marked as needing confirmation and have a qualified reviewer verify standards before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-inspection-guide-generator) <br>
- [Server-resolved GitHub source](https://github.com/duding-engicool/skill-inspection-guide-generator) <br>
- [Inspection guide format](references/inspection_guide_format.md) <br>
- [Template requirements](references/template_requirements.md) <br>
- [Inspection guide generator script](scripts/generate_inspection_guide.py) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Files, Guidance] <br>
**Output Format:** [Markdown guidance with structured JSON input, optional shell command, and a generated local .xlsx spreadsheet path.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated spreadsheet files are saved locally as {product_name}_检验指导书_{YYYYMMDD}.xlsx; uncertain standards are marked as needing confirmation.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence; artifact frontmatter says 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
