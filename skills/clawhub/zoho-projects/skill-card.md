## Description:

Zoho Projects API V3 integration with managed OAuth for managing projects, tasks, milestones, tasklists, and team collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations teams, and project contributors use this skill to inspect and manage Zoho Projects resources through Maton-mediated OAuth access. It supports project, task, milestone, tasklist, user, and comment workflows while emphasizing read-first behavior and explicit confirmation for account connections or data-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mediate access to a user's Zoho Projects account after authorization.

Mitigation: Prefer OAuth, review requested Zoho scopes during authorization, and install only when Maton-mediated Zoho Projects access is intended.

Risk: Project, task, milestone, tasklist, comment, or connection changes can modify or delete user data.

Mitigation: Default to read/list calls, verify the exact account and resource identifiers, and require explicit user confirmation before creating connections or running POST, PUT, PATCH, or DELETE requests.

Risk: Long-lived Maton API keys can be exposed through environment variables, command lines, logs, or copied output.

Mitigation: Use OAuth and the Maton CLI credential store when possible; use the raw API-key curl fallback only when the CLI cannot be used, feed secrets via stdin, and rotate any exposed key.

Risk: Ambiguous Maton profiles or multiple Zoho Projects connections can send requests to the wrong account.

Mitigation: Use explicit profile and connection selection when more than one account or connection exists, especially before any write or delete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-projects)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Projects API V3 Documentation](https://projects.zoho.com/api-docs)
- [Zoho Projects Developer Portal](https://www.zoho.com/projects/help/rest-api/zohoprojectsapi.html)
- [ClawHub API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and API request patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and a user-authorized Zoho Projects connection.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
