## Description:

Operates Kdocs/WPS cloud documents, including creating, reading, editing, searching, sharing, organizing, and summarizing documents, spreadsheets, PDFs, presentations, forms, multidimensional sheets, and knowledge-base content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kdocs-app](https://clawhub.ai/user/kdocs-app)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to work with Kdocs/WPS cloud documents through an agent, including document creation, content extraction, editing, file search, sharing, PDF/PPT workflows, and knowledge-base organization. Developers may also use it to route document tasks to the required kdocs-cli commands and reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate with broad Kdocs/WPS account and document access.

Mitigation: Install it only for trusted accounts and review requested document operations before allowing the agent to proceed.

Risk: Credential handling can expose a raw token if users paste it into chat or logs.

Mitigation: Prefer browser-based login or a secure secret flow, and avoid placing tokens in conversation text, command output, comments, or files.

Risk: Sharing, delete, overwrite, role-change, webhook, and AI/cloud-generation actions can affect document confidentiality or integrity.

Mitigation: Require explicit user review before these actions and confirm target files, recipients, roles, and visibility settings.

Risk: The skill includes remote CLI installation and skill update behavior.

Mitigation: Review the publisher and update source before installing or upgrading the CLI or skill package.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kdocs-app/skills/kdocs-skill)
- [Kdocs latest](https://www.kdocs.cn/latest)
- [Skill instructions](artifact/SKILL.md)
- [Authentication reference](artifact/references/auth.md)
- [Drive reference](artifact/references/drive.md)
- [Sheet reference](artifact/references/sheet.md)
- [WPS document reference](artifact/references/wps.md)
- [Presentation reference](artifact/references/wpp.md)
- [PDF reference](artifact/references/pdf.md)
- [Knowledge-base reference](artifact/references/kwiki.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and references to local documentation files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to create temporary JSON payload files, run kdocs-cli commands, and return Kdocs document links or command results.]

## Skill Version(s):

2.6.17 (source: server release evidence; artifact frontmatter reports 2.6.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
