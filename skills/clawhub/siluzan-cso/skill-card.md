## Description:

Siluzan CSO helps agents create and revise marketing content, manage personas and RAG-backed knowledge, and operate social publishing workflows for CSO media accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

External content operations teams use this skill to create platform-aware drafts, retrieve brand knowledge, manage persona guidance, upload assets, publish to social media accounts, and review CSO operational reports. It is intended for authenticated Siluzan CSO workflows rather than advertising account management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can modify Node/npm setup, npm registry configuration, and assistant skill directories.

Mitigation: Install only from a trusted publisher, prefer manual installation when practical, and review target paths before running installer scripts.

Risk: The skill can guide uploads, publishing, persona saves, task deletion, and content-library changes.

Mitigation: Require explicit user confirmation before state-changing CSO operations or external social publishing actions.

Risk: Local snapshots, configuration files, and credentials may expose sensitive account or content data.

Mitigation: Avoid saving sensitive snapshots in shared folders and prefer interactive login or API key handling over commands that place tokens in shell history.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/sigedev01-bit/skills/siluzan-cso)
- [Siluzan homepage](https://www.siluzan.com)
- [Setup and authentication](references/setup.md)
- [Publishing workflow](references/publish.md)
- [RAG knowledge retrieval](references/rag.md)
- [Content writer workflow](three-lib-content-workflow/content-writer.workflow.md)
- [Persona management](references/persona.md)
- [CSO web pages](references/web-pages.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON configuration examples, and generated content drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated siluzan-cso CLI for account, publishing, reporting, and RAG operations.]

## Skill Version(s):

1.1.44 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
