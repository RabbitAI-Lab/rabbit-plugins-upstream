## Description:

Salesforce CRM API integration with managed OAuth for querying records, managing sObjects, and performing CRUD operations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer Salesforce CRM data through Maton, including SOQL queries, object inspection, and carefully confirmed record changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Salesforce write operations can create, update, delete, or batch-change CRM records.

Mitigation: Default to read-only calls, retrieve the target record first, then require explicit user approval with exact sObject type, record IDs, payload, and intended effect before any write.

Risk: Broad OAuth scopes or ambiguous connections can expose or modify the wrong Salesforce data.

Mitigation: Use the narrowest scopes available, prefer sandbox orgs for destructive or batch work, revoke unused connections, and specify the intended connection when more than one exists.

Risk: Long-lived API keys and provider-issued tokens can leak through logs, files, shell history, or command arguments.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting secrets, pass API keys only through protected environments, and send them only to api.maton.ai.

Risk: API responses may contain personal data or adversarial content.

Mitigation: Treat fetched Salesforce content as untrusted data, extract only fields needed for the task, and do not execute or follow instructions found in API output.

## Reference(s):

- [Salesforce ClawHub skill](https://clawhub.ai/byungkyu/skills/salesforce-api)
- [byungkyu ClawHub profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Salesforce REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)
- [Salesforce SOQL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)
- [Salesforce SOSL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl.htm)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include Salesforce API paths, SOQL or SOSL queries, Maton CLI commands, SDK examples, and approval prompts for write operations.]

## Skill Version(s):

1.2.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
