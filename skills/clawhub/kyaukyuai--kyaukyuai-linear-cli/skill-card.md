## Description:

Use the linear-cli agent-native runtime to read and mutate Linear from Claude Code, Codex, or other agents. Use when the runtime needs default JSON output, startup discovery, dry-run previews, operation receipts, workflow-safe automation, or direct CLI control over Linear issues, projects, cycles, documents, notifications, webhooks, or related resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyaukyuai](https://clawhub.ai/user/kyaukyuai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to let Claude Code, Codex, Cursor, and similar agents inspect and update Linear workspaces through the external linear CLI. It is suited for issue, project, cycle, document, notification, webhook, user, label, schema, and raw GraphQL workflows where JSON output, dry-run previews, and operation receipts help keep automation reviewable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can perform broad Linear reads and writes, including destructive and bulk actions.

Mitigation: Use a least-privilege Linear token, preview writes with dry-run where available, keep interactive confirmation for destructive actions, and avoid --yes unless the operation has been reviewed.

Risk: Authentication tokens or workspace credentials could be exposed through logs, plaintext storage, shell history, or raw API use.

Mitigation: Prefer secure credential storage, verify the external CLI version and source before login, and never print or log Linear auth tokens.

Risk: File attachment and file-based content commands can upload local files or content that may contain secrets.

Mitigation: Review files before attachment or ingestion and do not attach local files that may contain credentials, private customer data, or other secrets.

Risk: Raw GraphQL and curl access can bypass higher-level command guardrails.

Mitigation: Prefer supported CLI commands, reserve raw API calls for reviewed gaps, and execute them with scoped credentials and explicit queries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyaukyuai/skills/kyaukyuai-linear-cli)
- [linear-cli install instructions](https://github.com/kyaukyuai/linear-cli?tab=readme-ov-file#install)
- [auth](references/auth.md)
- [issue](references/issue.md)
- [team](references/team.md)
- [project](references/project.md)
- [cycle](references/cycle.md)
- [document](references/document.md)
- [webhook](references/webhook.md)
- [schema](references/schema.md)
- [api](references/api.md)
- [capabilities](references/capabilities.md)
- [resolve](references/resolve.md)
- [organization-features](references/organization-features.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the installed external linear CLI and the authenticated Linear workspace permissions.]

## Skill Version(s):

3.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
