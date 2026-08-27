## Description:

Converts Markdown or text into Chinese official-document Word files that follow GB/T 9704-2012 formatting conventions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sereinone](https://clawhub.ai/user/sereinone)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document authors use this skill to turn Markdown, text, or older Word drafts into Chinese official-document DOCX files and to correct hierarchy markers, fonts, indentation, tables, page numbers, and cleanup issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The post-processing step can overwrite a Word document in place without creating a backup.

Mitigation: Keep source files and important DOCX files backed up before running the postprocessor.

Risk: The skill may apply Chinese official-document formatting too broadly when used for ordinary reports or generic Word cleanup.

Mitigation: Use it only when GB/T 9704-2012 or Chinese official-document formatting is explicitly desired.

## Reference(s):

- [Workflow Reference](artifact/references/workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/sereinone/skills/gongwen-docx)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Code, Guidance]

**Output Format:** [DOCX files generated from Markdown, with Markdown guidance and shell commands for generation and post-processing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Node docx package for generation and a Python post-processing step for font and layout fixes.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
