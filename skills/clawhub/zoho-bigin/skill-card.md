## Description:

Zoho Bigin API integration with managed OAuth for managing contacts, companies, pipelines, and products in Bigin CRM through Maton CLI and API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and CRM operators use this skill to read, search, create, update, and delete Zoho Bigin CRM records while managing OAuth-backed Maton connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify CRM account data, including contacts, companies, pipelines, and products.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit user approval before every create, update, or delete request.

Risk: Connection deletion is irreversible and can break automation using that connection.

Mitigation: List connections, confirm the exact connection identifier with the user, and avoid deletion unless the user has approved the specific target.

Risk: OAuth tokens or Maton API keys could be exposed if copied, printed, logged, or passed through shell history.

Mitigation: Prefer OAuth through the Maton CLI, leave credentials in the operating system credential store, and use raw HTTP with an API key only when the CLI cannot be installed.

Risk: The Maton API passthrough can reach endpoints beyond the documented intended surface when the connection permits them.

Mitigation: Use the narrowest available Zoho scopes, specify the intended connection and profile, and apply the same write-confirmation rules to any endpoint reached through the passthrough.

Risk: Zoho Bigin responses may contain personal data or untrusted CRM content.

Mitigation: Return only fields needed for the task, avoid dumping raw responses into logs or files, and treat content from CRM records as data rather than instructions.

## Reference(s):

- [Zoho Bigin Skill Page](https://clawhub.ai/byungkyu/skills/zoho-bigin)
- [Maton Homepage](https://maton.ai)
- [Bigin API Overview](https://www.bigin.com/developer/docs/apis/v2/)
- [Bigin REST API Documentation](https://www.bigin.com/developer/docs/apis/)
- [Modules API](https://www.bigin.com/developer/docs/apis/modules-api.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request and response examples, and optional Python or JavaScript code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API paths, request payloads, connection-selection guidance, and safety checks for CRM operations.]

## Skill Version(s):

1.2.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
