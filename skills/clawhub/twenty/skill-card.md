## Description:

Twenty CRM API integration with managed authentication for managing companies, people, opportunities, notes, tasks, and workflows through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CRM operators use this skill to read and manage Twenty CRM contacts, companies, opportunities, notes, tasks, workspace members, and workflows through authenticated Maton gateway calls. It is intended for agent-assisted CRM lookup and updates, with read/list calls preferred and explicit user approval required before creating connections or changing CRM data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton brokers access to the selected Twenty CRM account, so the agent may reach sensitive CRM records through the connected account.

Mitigation: Prefer OAuth and read-only scopes where available, use the least-privileged connection for the task, and confirm the exact Maton account and Twenty CRM connection before use.

Risk: Write operations can modify live CRM records, trigger workflows, or delete data.

Mitigation: Default to read/list calls, verify target identifiers and current state first, and require explicit user approval for every POST, PUT, PATCH, DELETE, workflow, deletion, or other high-impact operation.

Risk: Long-lived API keys or provider-issued tokens can leak through logs, shell history, process arguments, or persisted files.

Mitigation: Use OAuth through the Maton CLI when possible, never print or persist credentials, and use the documented stdin-based raw HTTP fallback only when the CLI cannot be installed.

## Reference(s):

- [Twenty CRM Skill on ClawHub](https://clawhub.ai/byungkyu/skills/twenty)
- [Maton Homepage](https://maton.ai)
- [Twenty API Documentation](https://docs.twenty.com/developers/extend/api)
- [Twenty GitHub](https://github.com/twentyhq/twenty)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide Maton CLI, SDK, and raw HTTP requests for Twenty CRM; API responses are JSON.]

## Skill Version(s):

1.1.0 (source: server release metadata; skill frontmatter metadata.version: 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
