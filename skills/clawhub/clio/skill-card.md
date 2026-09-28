## Description:

Clio is a write-capable API integration that uses managed OAuth through Maton to read, create, update, and delete Clio Manage legal-practice data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Legal-practice teams and their agents use this skill to inspect and manage Clio Manage records such as matters, contacts, activities, tasks, documents, calendar entries, time entries, and billing. It is intended for task-scoped Clio API work through Maton, with explicit approval before writes, deletes, new connections, functions, or triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clio records can contain privileged legal-practice data, and the skill can perform write and delete operations.

Mitigation: Use OAuth with narrow scopes, default to read/list calls, and require explicit user approval with specific resource identifiers before any write or delete.

Risk: Hosted functions and triggers can create persistent automation paths for Clio-derived data.

Mitigation: Use only user-authored or user-reviewed handlers, prefer DENY_ALL network policy, approve each destination and trigger, and remove automations when they are no longer needed.

Risk: The generic Clio API transport can reach endpoints beyond the reviewed examples if an agent constructs new paths.

Mitigation: Stay within the documented Clio paths for the task; require explicit approval for any exact method and endpoint outside the reviewed scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/clio)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Clio API Documentation](https://docs.developers.clio.com/api-reference/)
- [Clio Fields Guide](https://docs.developers.clio.com/api-docs/clio-manage/fields/)
- [Clio Rate Limits](https://docs.developers.clio.com/api-docs/clio-manage/rate-limits/)
- [Clio Permissions](https://docs.developers.clio.com/api-docs/permissions/)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly trigger reference](references/calendly/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [Google Mail trigger reference](references/google-mail/triggers.md)
- [HubSpot trigger reference](references/hubspot/triggers.md)
- [Linear trigger reference](references/linear/triggers.md)
- [Notion trigger reference](references/notion/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code examples, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved Clio authorization; write and automation actions require explicit approval.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
