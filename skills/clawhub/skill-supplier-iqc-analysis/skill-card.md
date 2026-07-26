## Description: <br>
Analyzes supplier IQC Excel workbooks to calculate quality metrics, compare suppliers, rate risk, and generate Markdown and HTML reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Enterprise SQE and quality teams use this skill to inspect incoming quality control Excel files, confirm field mappings, calculate pass rates, PPM, defect distributions, supplier benchmarks, and supplier-facing improvement reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML reports may render spreadsheet-derived text as active HTML. <br>
Mitigation: Prefer Markdown output for review; sanitize or escape spreadsheet-derived fields before sharing or opening HTML reports, and use trusted Excel sources when possible. <br>


## Reference(s): <br>
- [Source repository](https://github.com/duding-engicool/skill-supplier-iqc-analysis) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-supplier-iqc-analysis) <br>
- [Data schema and field mapping reference](references/data-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [JSON analysis output, Markdown report, HTML report, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an Excel input and may require a JSON field mapping; generated HTML should be treated as untrusted when it contains supplier-provided data.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence; artifact frontmatter lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
