## Description:

Clio API integration with managed OAuth for reading, creating, updating, and deleting legal-practice data in Clio Manage, including matters, contacts, activities, tasks, documents, calendar entries, time entries, and billing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Legal operations users, law firm staff, and agents acting with user approval use this skill to work with Clio Manage records through Maton OAuth. It supports read-first workflows and explicitly approved writes for matters, contacts, activities, tasks, documents, calendar entries, time entries, and bills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive legal-practice and client data through a connected Clio account.

Mitigation: Install only when the publisher is trusted, use OAuth with the narrowest available Clio scopes, retrieve only task-relevant records, and avoid forwarding Clio data to third-party hosts.

Risk: Write, delete, billing, automation, or connection changes could affect real legal practice records.

Mitigation: Default to read/list calls, verify exact resource identifiers and current state, summarize the intended effect, and require explicit user approval before each modifying action.

Risk: Multiple Clio connections or Maton profiles can make the target account ambiguous.

Mitigation: Specify the intended connection and profile when more than one exists, and list connections before high-impact writes or deletes.

Risk: Hosted functions and trigger destinations can create persistent automation or data forwarding.

Mitigation: Use user-authored or user-reviewed handlers, prefer DENY_ALL network policy, keep destinations on api.maton.ai or *.maton.app unless the user approves an exact external host, and delete automation when it is no longer needed.

Risk: Using MATON_API_KEY directly can expose a long-lived credential through logs, shell history, child processes, or copied output.

Mitigation: Prefer CLI OAuth; when the API key fallback is unavoidable, never print, log, persist, or pass the key on a command line, and send it only to api.maton.ai.

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
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Clio API calls and hosted automation examples; write, delete, connection, trigger, and deployment actions require explicit user approval.]

## Skill Version(s):

1.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
