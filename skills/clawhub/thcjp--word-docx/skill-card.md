## Description:

创建检查编辑 helps agents create, inspect, and edit Microsoft Word DOCX documents with support for styles, numbering, and document workflow automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, business users, and automation teams use this skill to create, inspect, and edit DOCX files, including style, numbering, structure, and content changes. It is intended for document processing workflows and is not suitable for encrypted-file cracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local DOCX files may be modified or overwritten during create and edit workflows.

Mitigation: Use copies of important documents, provide explicit output paths, and review proposed file changes before allowing writes.

Risk: Sensitive document contents may be exposed if processed through external APIs or broad agent context.

Mitigation: Avoid sensitive files unless the agent's command and API behavior is understood, and redact confidential content before processing.

Risk: The skill can invoke local commands without tight scoping.

Mitigation: Run in a sandboxed workspace, review shell commands before execution, and grant only the file permissions required for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/word-docx)
- [SkillHub homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, JSON-style reports, shell commands, and generated or edited DOCX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and modify local DOCX files and may propose command or API-based workflows depending on the agent environment.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
