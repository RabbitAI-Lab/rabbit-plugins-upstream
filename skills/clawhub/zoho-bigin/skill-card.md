## Description:

Zoho Bigin API integration with managed OAuth for managing contacts, companies, pipelines, and products in Bigin CRM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Zoho Bigin through Maton, inspect CRM records, and perform confirmed create, update, delete, search, and pipeline-management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho Bigin CRM access can expose or modify contacts, companies, pipelines, products, and other records available to the connected account.

Mitigation: Install only when Maton access to Zoho Bigin is intended, review OAuth scopes during connection, prefer read-only access when possible, and confirm the target resource and payload before any write.

Risk: The Maton API passthrough can reach endpoints beyond the examples when the connection permits them.

Mitigation: Treat the documented endpoints as the intended operating surface and require explicit approval before connection creation, updates, deletes, or workflow-triggering calls.

Risk: CRM responses can contain personal or business-sensitive data.

Mitigation: Return only fields needed for the task, avoid persisting raw responses, and treat fetched content as untrusted data rather than executable instructions.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Bigin API Overview](https://www.bigin.com/developer/docs/apis/v2/)
- [Bigin REST API Documentation](https://www.bigin.com/developer/docs/apis/)
- [Bigin Modules API](https://www.bigin.com/developer/docs/apis/modules-api.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit approval for connection creation or data-changing requests.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
