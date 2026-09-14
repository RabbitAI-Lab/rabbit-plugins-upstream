## Description:

Zoho Bigin API integration with managed OAuth for managing contacts, companies, pipelines, and products in Bigin CRM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, support, and operations users use this skill through an agent to read, create, update, or delete Zoho Bigin CRM records and to manage sales pipeline data. Developers and operators can also use it to configure approved Maton connections, functions, and triggers for Zoho Bigin workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify sensitive CRM records through an authorized Zoho Bigin connection.

Mitigation: Use OAuth where possible, start with read/list calls, approve each write or delete separately, and grant only the scopes needed for the task.

Risk: Hosted functions and triggers can automate CRM actions after deployment.

Mitigation: Approve each function, trigger, and destination separately, use DENY_ALL network policy unless a host is explicitly required, and remove unused automations when finished.

Risk: Full CRM responses and trigger payloads may contain personal or business-sensitive data.

Mitigation: Avoid forwarding full event payloads to third-party hosts and extract only the fields needed for the user-requested task.

## Reference(s):

- [Zoho Bigin Skill on ClawHub](https://clawhub.ai/byungkyu/skills/zoho-bigin)
- [Maton Homepage](https://maton.ai)
- [Bigin API Overview](https://www.bigin.com/developer/docs/apis/v2/)
- [Bigin REST API Documentation](https://www.bigin.com/developer/docs/apis/)
- [Modules API](https://www.bigin.com/developer/docs/apis/modules-api.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with inline shell, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved Zoho Bigin authorization before account data can be accessed or modified.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
