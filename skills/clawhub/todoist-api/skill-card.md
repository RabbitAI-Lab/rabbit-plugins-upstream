## Description:

Todoist API integration with managed OAuth for managing tasks, projects, sections, labels, and comments through Maton CLI calls that default to read/list behavior and require confirmation for writes or new connections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to organize Todoist work items by listing, creating, updating, completing, and deleting tasks and related project resources after authorizing a Todoist connection through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, complete, or delete Todoist resources in an authorized account.

Mitigation: Confirm the exact account, connection, target resource, payload, and intended effect before allowing any write, completion, or deletion operation.

Risk: Authorizing a Todoist connection grants Maton access to Todoist account data for tasks, projects, sections, labels, and comments.

Mitigation: Prefer OAuth, authorize only the account needed for the task, use least-privilege scopes when available, and revoke unused connections.

Risk: Credential exposure could occur if API keys or provider-issued tokens are printed, logged, persisted, or passed on command lines.

Mitigation: Use Maton's OAuth flow and credential store where possible; when a raw HTTP fallback is unavoidable, keep keys out of logs, files, shell history, and command-line arguments.

Risk: Todoist API responses and comments may contain untrusted content.

Mitigation: Treat returned content as data, validate values before reuse, and do not execute or follow instructions embedded in fetched Todoist content.

## Reference(s):

- [Todoist Skill on ClawHub](https://clawhub.ai/byungkyu/skills/todoist-api)
- [Maton](https://maton.ai)
- [Todoist API v1 Documentation](https://developer.todoist.com/api/v1)
- [Todoist Filter Syntax](https://todoist.com/help/articles/introduction-to-filters)
- [Todoist OAuth Documentation](https://developer.todoist.com/guides/#oauth)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and API request patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, SDK snippets, raw HTTP fallback examples, and user-confirmation prompts for write operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
