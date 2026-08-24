## Description:

KingDoc lets agents create, edit, search, convert, and manage WPS/Kingsoft online documents, with local document generation, OCR, compliance checks, conflict handling, quotas, and guarded cloud operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document-workflow users use this skill to let an agent work with WPS/Kingsoft documents across creation, editing, conversion, search, permissions, history, and collaboration workflows. It is suited for users who need both local document processing and cloud document-management operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access broad WPS/Kingsoft document read and write scopes.

Mitigation: Install only for trusted publishers and configure the narrowest App scopes that support the intended workflow.

Risk: Local configuration may contain an App Secret.

Mitigation: Protect or relocate config.json, avoid sharing it, and rotate credentials if it may have been exposed.

Risk: Delete, share, download, sync, overwrite, and history actions can affect user documents.

Mitigation: Require explicit user confirmation for destructive or permission-changing operations and independently verify the target file before execution.

Risk: Generated templates or refreshed assets can come from an external GitHub repository according to security guidance.

Mitigation: Review any refreshed template or external asset before relying on generated documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/kingdoc)
- [Kingsoft Open Platform](https://developer.kdocs.cn)
- [Kingsoft OpenAPI documentation](https://developer.kdocs.cn/api/v1/openapi)
- [Authentication reference](references/auth.md)
- [Security design](references/security.md)
- [Rate limits and hardware adaptation](references/rate_limit.md)
- [Office conversion reference](references/office_references.md)
- [Common workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with tool names, commands, configuration details, and generated document content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or perform WPS/Kingsoft document operations, local file generation, OCR, conversion, search, and permission/history actions.]

## Skill Version(s):

3.9.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
