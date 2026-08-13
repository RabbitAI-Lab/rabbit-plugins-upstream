## Description:

KingDoc lets an agent create, edit, manage, compare, and collaborate on Kingsoft/WPS online documents, with local document generation, OCR, compliance checks, and WPS AI-style assistance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use KingDoc to automate WPS/Kingsoft document workflows, including document creation, editing, sharing, version recovery, comparison, compliance checks, OCR, and collaboration. The skill is intended for agents that help users manage cloud documents and selected local files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad document-management access can affect WPS/Kingsoft files, sharing settings, versions, webhooks, notifications, and selected local files.

Mitigation: Review each requested operation before execution, use the least-privileged account or scope available, and prefer read-only or short-lived sharing links.

Risk: Deletion, overwrite, permission, rollback, batch, and webhook changes can cause data loss or unintended exposure.

Mitigation: Require explicit confirmation for dangerous actions, inspect the target file list and impact, and use dry-run behavior when available.

Risk: Cloud OCR fallback and uploads may send document or image contents to external services.

Mitigation: Use local OCR and local generation when possible, avoid sensitive local paths, and confirm before cloud processing or upload.

Risk: Credential and configuration files can expose WPS/Kingsoft access if mishandled.

Mitigation: Protect config.json, avoid committing credentials, and rotate App ID or App Secret if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/kingdoc)
- [Publisher profile](https://clawhub.ai/user/fyniujin)
- [Kingsoft Developer Platform](https://developer.kdocs.cn)
- [SKILL.md](SKILL.md)
- [Authentication reference](references/auth.md)
- [Security design](references/security.md)
- [Rate limit and hardware adaptation](references/rate_limit.md)
- [Office conversion and OCR reference](references/office_references.md)
- [Common workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, structured text, JSON-like tool arguments, shell commands, and generated document content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or perform document operations through WPS/Kingsoft APIs and local file-processing tools.]

## Skill Version(s):

3.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
