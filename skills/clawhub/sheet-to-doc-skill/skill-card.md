## Description: <br>
Generate Word documents from Word templates and JSON data. Supports basic placeholder replacement ({field} format) and placeholder extraction for data validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[he-yang](https://clawhub.ai/user/he-yang) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operations teams, and document automation users can generate .docx files from Word templates and JSON data, extract template placeholders, and validate data keys before generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated documents include Sheet-to-Doc footer attribution and modified document metadata. <br>
Mitigation: Use the skill only when that attribution and metadata behavior is acceptable for the document workflow. <br>
Risk: The generation script can overwrite the output path provided by the agent or user. <br>
Mitigation: Write outputs to a dedicated folder or use new filenames before distributing generated documents. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/he-yang/skills/sheet-to-doc-skill) <br>
- [Publisher Profile](https://clawhub.ai/user/he-yang) <br>
- [Sheet-to-Doc Homepage](https://sheet-to-doc.wtsolutions.cn) <br>
- [Sheet-to-Doc Documentation](https://sheet-to-doc.wtsolutions.cn/en/latest/index.html) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JavaScript API examples, shell commands, JSON examples, and generated .docx files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated documents include Sheet-to-Doc footer attribution and modified document metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
