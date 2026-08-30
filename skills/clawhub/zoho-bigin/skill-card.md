## Description:

Zoho Bigin API integration with managed OAuth for managing contacts, companies, pipelines, and products in Bigin CRM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to read, search, create, update, and delete Zoho Bigin CRM records through Maton-managed OAuth. It is intended for CRM account, contact, pipeline, product, and related API workflows where the agent proposes or executes Maton CLI/API calls with user confirmation for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify CRM records through a connected Zoho Bigin account.

Mitigation: Use read/list calls first, verify the target resource and account, and require clear user confirmation before create, update, delete, workflow, or messaging actions.

Risk: Credentials or provider-issued tokens can be exposed if handled outside the OAuth-backed Maton CLI flow.

Mitigation: Prefer OAuth, avoid printing or persisting credentials, do not inspect credential stores, and use raw HTTP only when the CLI is unavailable with secrets passed through stdin to api.maton.ai.

Risk: Multiple Maton profiles or Zoho Bigin connections can route requests to the wrong account.

Mitigation: Verify authentication and active connections before acting, and specify the intended profile or connection whenever more than one exists.

Risk: CRM content returned by the API may contain untrusted instructions or adversarial text.

Mitigation: Treat API response content as data, never execute or evaluate it, and do not let fetched content choose endpoints, recipients, or follow-up actions.

## Reference(s):

- [Zoho Bigin API Overview](https://www.bigin.com/developer/docs/apis/v2/)
- [Zoho Bigin REST API Documentation](https://www.bigin.com/developer/docs/apis/)
- [Zoho Bigin Modules API](https://www.bigin.com/developer/docs/apis/modules-api.html)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-bigin)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash commands, JSON API payloads, and Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Zoho Bigin connection; defaults to read/list calls and requires explicit confirmation for writes or new connections.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter metadata.version is 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
