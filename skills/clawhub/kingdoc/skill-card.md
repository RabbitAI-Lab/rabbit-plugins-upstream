## Description:

KingDoc lets an agent create, edit, convert, search, share, and manage Kingsoft/WPS online documents, with local document generation, OCR, form analytics, history, and collaboration helpers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use KingDoc to automate Kingsoft/WPS document workflows, including document creation, editing, upload, conversion, OCR, search, permissions, history recovery, form analysis, and collaboration tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, modify, share, overwrite, synchronize, and delete Kingsoft/WPS documents.

Mitigation: Use least-privilege app credentials and require host-level confirmation before delete, overwrite, share, sync, permission, and batch actions.

Risk: Document activity may be retained through the memory bridge.

Mitigation: Disable or avoid the memory bridge unless long-term retention of document activity is intended.

Risk: Setup and bridge features can operate on local paths and subprocesses.

Mitigation: Review configured paths before running setup or bridge features, and avoid running them in sensitive directories.

## Reference(s):

- [KingDoc Skill Page](https://clawhub.ai/fyniujin/skills/kingdoc)
- [Kingsoft Open Platform](https://developer.kdocs.cn)
- [WPS OpenAPI Base URL](https://developer.kdocs.cn/api/v1/openapi)
- [Security Design](references/security.md)
- [Authentication Reference](references/auth.md)
- [Rate Limit and Performance Reference](references/rate_limit.md)
- [Office Conversion Reference](references/office_references.md)
- [Workflow Reference](references/workflows.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured tool guidance with inline shell commands, code snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to create, modify, convert, upload, share, synchronize, or delete documents through Kingsoft/WPS workflows.]

## Skill Version(s):

4.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
