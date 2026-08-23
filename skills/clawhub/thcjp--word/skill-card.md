## Description:

Word文档工具 helps an agent control Word sessions, documents, selections, comments, export, and review workflows through local Word automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers can use this skill to automate Word document handling tasks such as session control, export, review state checks, comments, and document editing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests local command and file-write authority for Word automation.

Mitigation: Run it only in an agent environment whose command and file-write approvals you trust, and review proposed commands or overwrite actions before approval.

Risk: Automation may modify or overwrite local Word documents.

Mitigation: Use copies of important documents and confirm the target file path before allowing edits, exports, or saves.

Risk: Sensitive document contents may be exposed to the agent session.

Mitigation: Avoid sensitive files unless the environment provides containment and access controls you trust.

Risk: The security summary flags weak and partly misleading safety boundaries.

Mitigation: Treat the skill as requiring extra review before deployment and rely on explicit approval gates for command execution and file writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/word)
- [Artifact homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown or text guidance with optional shell commands and generated document files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, modify, export, or overwrite local Word-related files depending on the approved agent action.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
