## Description:

Twenty CRM API integration with managed authentication for managing companies, people, opportunities, notes, tasks, workflows, and workspace members.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to read and manage Twenty CRM data through Maton, including contacts, companies, deals, activities, workflows, and workspace members. It is intended for CRM workflows where account context, least-privilege access, and explicit confirmation before writes matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change live Twenty CRM records through Maton.

Mitigation: Default to read and list calls, confirm the exact account or connection before writes, and review every create, update, delete, workflow, or member-access action before it runs.

Risk: Broad or ambiguous authorization can expose more CRM data than the current task requires.

Mitigation: Use OAuth where possible, choose the narrowest available scopes, specify the intended connection when multiple connections exist, and revoke unused connections.

Risk: Long-lived Maton API keys can leak when the CLI is unavailable and raw HTTPS requests are used.

Mitigation: Prefer OAuth and the Maton credential store; when an API key is unavoidable, never print, log, persist, or pass it on the command line, and send it only to api.maton.ai.

Risk: CRM API responses may contain personal or sensitive customer data.

Mitigation: Extract only the fields needed for the task and avoid dumping full responses into logs, files, or user-visible output unless explicitly requested.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/twenty)
- [Maton Homepage](https://maton.ai)
- [Twenty API Documentation](https://docs.twenty.com/developers/extend/api)
- [Twenty GitHub](https://github.com/twentyhq/twenty)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include Maton CLI commands, raw HTTPS request examples, SDK snippets, and guidance for handling CRM API responses.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
