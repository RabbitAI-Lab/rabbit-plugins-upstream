## Description:

Siluzan CSO helps agents operate the Siluzan content operations workflow for copywriting, persona management, RAG-backed knowledge lookup, social publishing, account management, planning, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and content teams use this skill to guide agents through Siluzan CSO tasks including content creation workflows, persona handling, RAG lookup, media account operations, publishing, planning, and reporting. It is intended for authenticated CSO users who need structured agent assistance around the siluzan-cso CLI and related workflow documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the installer uses unsafe remote execution patterns and can make broad system and assistant-environment changes.

Mitigation: Review the installer before use, prefer a manually installed pinned CLI version, and register the skill only in the intended assistant environment.

Risk: The security guidance warns against persistent npm registry changes unless the user explicitly wants that mirror.

Mitigation: Check npm registry configuration before and after installation, and avoid accepting persistent registry changes unless they are required.

Risk: The skill handles authentication values such as API keys, auth tokens, and login codes.

Mitigation: Use interactive login where possible and avoid placing real API keys, tokens, or verification codes in command history or shared files.

Risk: The skill can upload media, submit publish tasks, and alter account groups when authenticated.

Mitigation: Confirm every upload, publish target, schedule, account, and account-group change with the user before executing write operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sigedev01-bit/skills/siluzan-cso)
- [Siluzan Homepage](https://www.siluzan.com)
- [Setup and Configuration](artifact/references/setup.md)
- [Publishing Workflow](artifact/references/publish.md)
- [RAG Knowledge Retrieval](artifact/references/rag.md)
- [Content Writer Workflow](artifact/three-lib-content-workflow/content-writer.workflow.md)
- [Platform Rules](artifact/references/platforms/platform-rules.md)
- [Content Validation](artifact/references/validate-content.md)
- [Account and Reporting Operations](artifact/references/list-accounts.md)
- [CSO Web Pages](artifact/references/web-pages.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local files, uploaded media identifiers, publish task IDs, reports, and RAG-backed content drafts when the CLI is authorized.]

## Skill Version(s):

1.1.45 (source: evidence.release.version and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
