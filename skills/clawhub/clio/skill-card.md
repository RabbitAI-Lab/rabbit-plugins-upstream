## Description:

Clio API integration with managed OAuth for reading, creating, updating, and deleting legal practice data in Clio Manage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Legal-practice operators, attorneys, and agents with an approved Clio connection use this skill to query and manage Clio Manage matters, contacts, activities, tasks, calendar entries, documents, users, and bills. It is intended for read-first workflows and write actions only after explicit user approval with specific resource identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive legal practice and client data in a connected Clio account.

Mitigation: Install only when Maton is trusted with that account, use OAuth where possible, choose the narrowest available Clio scopes, and revoke unused connections promptly.

Risk: Create, update, and delete operations can modify or remove legal-practice records, including matters, contacts, billing records, tasks, documents, and calendar entries.

Mitigation: Default to read/list calls, require the agent to show exact records and payloads before any write or delete, and proceed only after explicit approval with specific resource identifiers.

Risk: Multiple Clio connections or Maton profiles can cause actions to target the wrong account.

Mitigation: Specify the intended connection or profile when more than one exists, and verify the target account before proposing write operations.

Risk: Long-lived API keys or provider-issued tokens can leak if printed, logged, persisted, or passed through command lines.

Mitigation: Prefer OAuth, keep credentials in the managed credential store, never print or persist token values, and rotate any key that was exposed.

Risk: Content returned from Clio may contain untrusted instructions that could influence later calls.

Mitigation: Treat Clio response content as data only; do not let it choose endpoints, methods, recipients, shell commands, or follow-up requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/clio)
- [Maton Homepage](https://maton.ai)
- [Clio API Documentation](https://docs.developers.clio.com/api-reference/)
- [Clio Fields Guide](https://docs.developers.clio.com/api-docs/clio-manage/fields/)
- [Clio Rate Limits](https://docs.developers.clio.com/api-docs/clio-manage/rate-limits/)
- [Clio Permissions](https://docs.developers.clio.com/api-docs/permissions/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval for connection creation and write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
