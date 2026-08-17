## Description:

KingDoc helps agents create, edit, manage, compare, convert, and review WPS/Kingsoft Docs documents, spreadsheets, presentations, forms, diagrams, attachments, and related document workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and document-heavy teams use this skill to let an agent work with WPS/Kingsoft Docs files across creation, editing, cloud upload, sharing, permissions, version recovery, OCR, format conversion, compliance checks, and collaboration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can receive broad WPS/Kingsoft Docs read and write scopes, including cloud document changes.

Mitigation: Use a dedicated low-privilege WPS/Kingsoft Docs app and account, grant only needed scopes, and review requested file, account, and destination details before authorizing operations.

Risk: Delete, rollback, overwrite, permission, webhook, notification, upload, and download actions can alter documents, access, or external integrations.

Mitigation: Require explicit confirmation for sensitive operations and use dry-run or always-confirm safety modes for higher-risk work.

Risk: Setup or authentication tests may expose credentials in logged or shared terminals until token-printing behavior is fixed.

Mitigation: Run setup in a private terminal, avoid shared logs, rotate exposed credentials, and prefer a disposable low-privilege app secret during evaluation.

Risk: Local file and network behaviors can move data between the local machine, WPS/Kingsoft Docs, and external callback or notification URLs.

Mitigation: Confirm local paths, upload/download targets, webhook callback URLs, and notification destinations before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/kingdoc)
- [Kingsoft Docs Open Platform](https://developer.kdocs.cn)
- [KingDoc README](artifact/kingdoc/README.md)
- [Security design](artifact/kingdoc/references/security.md)
- [Workflow reference](artifact/kingdoc/references/workflows.md)
- [Office conversion and OCR reference](artifact/kingdoc/references/office_references.md)
- [Rate limit and performance reference](artifact/kingdoc/references/rate_limit.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured tool guidance with shell commands, configuration snippets, generated document content, and file-operation instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger local file generation, WPS/Kingsoft Docs API calls, uploads, downloads, permission changes, document rollback, webhook setup, OCR, and compliance-analysis workflows.]

## Skill Version(s):

3.6.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
