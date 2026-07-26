## Description: <br>
Organizes Word documents by formatting text, generating a table of contents, cleaning redundant content, and applying academic, business, or minimal style templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to standardize local Word documents, apply document templates, generate a table of contents, and clean redundant formatting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can overwrite the original Word document when output_path is not provided. <br>
Mitigation: Provide a separate output_path and review the generated file before replacing the original document. <br>
Risk: The skill may install the python-docx package at runtime. <br>
Mitigation: Run it in an isolated Python environment and require approval before any package installation. <br>
Risk: ClawScan reports that the skill under-discloses package installation and overwrite behavior. <br>
Mitigation: Review the commands before execution, keep backups, and avoid running it on shared or locked-down machines without approval. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/word-document-organizer) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Guidance] <br>
**Output Format:** [Markdown instructions with bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May modify or create .docx files based on document_path, operations, style_template, and output_path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
