## Description:

Zoho Projects API V3 integration with managed OAuth for managing projects, tasks, milestones, tasklists, and team collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to Zoho Projects through Maton-managed OAuth, inspect project resources, and perform project, task, milestone, tasklist, and collaboration actions with confirmation for writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived Maton API keys can be exposed through environment variables, command history, logs, or pasted output.

Mitigation: Prefer Maton OAuth, use expected Maton package sources, do not print or persist credentials, and only use the raw HTTP API-key fallback when the CLI cannot be installed.

Risk: Write operations can create, update, or delete Zoho Projects resources in the wrong account or with the wrong payload.

Mitigation: Review the Zoho account and scopes, specify the intended connection when needed, list resources first, and confirm the exact resource and payload before any create, update, or delete action.

Risk: Fetched project content can include untrusted text that attempts to steer subsequent agent actions.

Mitigation: Treat API response content as data, not instructions, and use it only after validating endpoint choices, resource identifiers, and intended effects.

## Reference(s):

- [Zoho Projects API V3 Documentation](https://projects.zoho.com/api-docs)
- [Zoho Projects Developer Portal](https://www.zoho.com/projects/help/rest-api/zohoprojectsapi.html)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-projects)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON request examples, SDK snippets, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-authorized Zoho Projects connection; write operations require explicit confirmation.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
