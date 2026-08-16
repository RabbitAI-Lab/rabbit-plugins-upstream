## Description:

Use for Notion API integration, pages, blocks, databases or data sources, comments, views, file uploads, workspace search, OAuth connections, and safe preview-first read or mutation workflows through @pontx/notion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to build or operate Notion integrations for pages, blocks, databases, comments, views, file uploads, search, OAuth, and webhook-related workflows while previewing mutations and protecting credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notion tokens or workspace content could be exposed through logs or unreviewed generated code.

Mitigation: Keep Notion tokens in secrets, avoid logging credentials or workspace content, and review generated code before running it.

Risk: Irreversible Notion actions such as deleting blocks, comments, views, or revoking tokens can affect user workspaces.

Mitigation: Preview the exact request and require explicit confirmation of target IDs and payloads before writes, deletes, or revocations.

Risk: Rate limits or service overload can cause failed or repeated operations.

Mitigation: Respect Retry-After, use exponential backoff with jitter, and retry server errors only for idempotent requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pontjs/skills/pontx-notion)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and code-oriented examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
