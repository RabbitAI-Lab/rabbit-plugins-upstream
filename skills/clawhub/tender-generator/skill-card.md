## Description: <br>
智能项目文档生成器，通过对话收集信息，自动填充模板生成全套项目文档。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mama1234421](https://clawhub.ai/user/mama1234421) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and project teams use this skill to collect project, company, pricing, and technical inputs through conversation, fill user-prepared document templates, self-check required fields, and package a complete project document set for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process sensitive company, pricing, bank, identity, and contact information during document generation. <br>
Mitigation: Provide only the information needed for the document set, avoid uploading unnecessary ID or bank documents, review generated documents and archives before sharing, and delete temporary outputs when no longer needed. <br>
Risk: Generated project documents may be incomplete, contain unfilled placeholders, or require signed and stamped source documents before formal use. <br>
Mitigation: Use the skill's self-check output and perform a human review of every generated file before submission or external distribution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mama1234421/skills/tender-generator) <br>
- [README](artifact/README.md) <br>
- [Default Project Document Template README](artifact/templates/默认/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Conversational text and Markdown checklists, with generated project document files packaged as a ZIP archive when templates are available.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-prepared .docx templates and human review before formal use.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
