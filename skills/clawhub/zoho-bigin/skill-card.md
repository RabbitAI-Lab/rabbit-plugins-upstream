## Description:

Zoho Bigin API integration with managed OAuth for managing contacts, companies, pipelines, and products in Bigin CRM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to inspect and manage Zoho Bigin CRM records, authorize Maton-managed Bigin connections, and prepare approved automations for CRM workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write, delete, connection, hosted function, and trigger actions can affect Zoho Bigin data or account access.

Mitigation: Default to read/list operations and require explicit user approval before writes, deletes, new connections, hosted functions, or trigger destinations.

Risk: Maton API keys or OAuth-backed credentials can expose access if copied into broad environments or logs.

Mitigation: Prefer OAuth through the Maton CLI and operating-system credential storage; use raw HTTP or environment variables only when the CLI cannot be installed.

Risk: Hosted functions and triggers can relay CRM or connected-app data beyond the intended workflow.

Mitigation: Use least-privilege connections, review the handler and destination before approval, prefer DENY_ALL network policy for hosted functions, and avoid unrelated event-source references unless the user asks for that automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/zoho-bigin)
- [Maton homepage](https://maton.ai)
- [Bigin API overview](https://www.bigin.com/developer/docs/apis/v2/)
- [Bigin REST API documentation](https://www.bigin.com/developer/docs/apis/)
- [Modules API](https://www.bigin.com/developer/docs/apis/modules-api.html)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs commonly include Maton CLI commands, API request examples, least-privilege approval guidance, and configuration steps for OAuth connections, functions, and triggers.]

## Skill Version(s):

1.2.4 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
