## Description:

Siluzan CSO helps agents support CSO content operations, persona management, RAG-backed copywriting, media account workflows, publishing, reporting, and planning for supported social platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT

## Use Case:

External CSO operators and developers use this skill to draft and revise marketing content, manage personas and RAG sources, upload media, create publishing tasks, and review operational reports for supported social channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authenticate to CSO, read account, persona, and RAG data, upload media, and submit public publishing tasks.

Mitigation: Install only for users who are comfortable granting those permissions, and review generated publish configurations and dry-runs before submission.

Risk: The installer and workflows can make persistent system or platform changes, including npm or assistant-directory changes, account-group edits, persona saves, and content-library edits.

Mitigation: Prefer manual, scoped installation, review installation changes, and require explicit confirmation before uploads, publishes, account-group edits, persona saves, or persistent content-library updates.

## Reference(s):

- [Siluzan CSO on ClawHub](https://clawhub.ai/sigedev01-bit/skills/siluzan-cso)
- [Siluzan Homepage](https://www.siluzan.com)
- [Setup Guide](references/setup.md)
- [Publish Guide](references/publish.md)
- [RAG Guide](references/rag.md)
- [Content Writer Workflow](three-lib-content-workflow/content-writer.workflow.md)
- [Platform Rules](references/platforms/platform-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON configuration, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local draft, validation, media, and publish configuration files when workflows require them.]

## Skill Version(s):

1.1.43 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
