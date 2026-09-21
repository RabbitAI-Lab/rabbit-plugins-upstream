## Description:

KingDoc lets agents create, edit, manage, search, convert, compare, and govern Kingsoft Docs documents through local helpers and Kingsoft/WPS API workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, teams, and employees use KingDoc to automate Kingsoft Docs document lifecycle tasks, including document generation, cloud upload, permissions, version history, OCR, search, compliance scans, and collaboration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change, share, automate, delete, and retain document-related data across Kingsoft Docs workflows.

Mitigation: Use a dedicated, least-privileged Kingsoft app or test account and review planned operations before enabling workflows.

Risk: Uploads, sharing links, permission changes, version rollback, AirScript execution, and permanent delete can affect data access or integrity.

Mitigation: Require explicit user confirmation before those operations and keep dry-run or review steps enabled where available.

Risk: Generated config.json and optional memory-bridge or template-refresh workflows may persist sensitive local or integration data.

Mitigation: Protect config.json and avoid enabling memory-bridge or template-refresh workflows unless local persistence and external integrations are approved.

## Reference(s):

- [KingDoc README](artifact/README.md)
- [KingDoc Skill Definition](artifact/SKILL.md)
- [KingDoc Security Design](artifact/references/security.md)
- [KingDoc Workflows](artifact/references/workflows.md)
- [KingDoc Rate Limit and Hardware Strategy](artifact/references/rate_limit.md)
- [Kingsoft Open Platform](https://developer.kdocs.cn)
- [Kingsoft OpenAPI Reference](https://developer.kdocs.cn/api/v1/openapi)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline commands, configuration snippets, and generated document content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate local file generation and Kingsoft Docs API workflows when configured.]

## Skill Version(s):

4.2.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
