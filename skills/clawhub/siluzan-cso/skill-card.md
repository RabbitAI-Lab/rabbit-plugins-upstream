## Description:

Siluzan CSO helps agents create and validate marketing content, manage personas and account groups, publish to social platforms, query CSO RAG knowledge bases, and retrieve planning, task, and reporting data through siluzan-cso-cli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and content teams use this skill to route CSO content creation, persona management, RAG-backed drafting, social publishing, task follow-up, account operations, planning, and reporting through documented workflows and CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer execution can make persistent local changes, including npm configuration changes, global CLI installation, assistant skill registration, and local credential setup.

Mitigation: Review the installer before use and prefer a pinned, manual install path when possible instead of running curl-to-bash or irm-to-iex blindly.

Risk: Publishing, upload, account-group, and task commands can modify external CSO or social publishing state.

Mitigation: Confirm every publish, upload, account, retry, stop, delete, or scheduling change with the user before executing it.

Risk: JSON snapshots, logs, credentials, and generated drafts may contain operational or customer-sensitive content.

Mitigation: Store snapshots and logs outside shared or version-controlled folders, and avoid exposing local CSO config or token material.

Risk: Content-generation workflows can create polarizing or high-impact messaging if used without review.

Mitigation: Use the polarizing content pattern only when explicitly appropriate and reviewed by the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sigedev01-bit/skills/siluzan-cso)
- [Siluzan homepage](https://www.siluzan.com)
- [Setup and authentication](references/setup.md)
- [Publishing workflow](references/publish.md)
- [RAG workflow](references/rag.md)
- [Content writer workflow](three-lib-content-workflow/content-writer.workflow.md)
- [Persona management](references/persona.md)
- [Planning workflow](references/planning.md)
- [Task management](references/task.md)
- [Reporting workflow](references/report.md)
- [CSO web pages](references/web-pages.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON configuration examples, and local files when workflows require saved drafts or snapshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local draft files, JSON snapshots, publish configs, extracted cover images, and CLI commands that require user confirmation for write actions.]

## Skill Version(s):

1.1.42 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
