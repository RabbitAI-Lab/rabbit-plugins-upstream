## Description:

Salesforce CRM API integration with managed OAuth for querying records, managing sObjects, and performing approved CRUD operations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, administrators, and agents use this skill to work with Salesforce CRM data through a managed OAuth connection. It supports read-first administration workflows, controlled record changes, and optional Maton-hosted automation when the user approves the exact connection, operation, and destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Salesforce CRM records can be changed or deleted through approved write and batch operations.

Mitigation: Use the narrowest Salesforce account and scopes available, prefer sandbox orgs for destructive or batch work, and require explicit confirmation of the sObject, record IDs, and consequence before writes.

Risk: OAuth connections, API keys, functions, triggers, and destinations can expose business data if scoped or routed too broadly.

Mitigation: Default to read/list calls, verify the intended connection ID, avoid embedding credentials in destinations, approve each destination host and payload, and revoke unused connections promptly.

Risk: The skill does not document cryptographic verification for Maton CLI or SDK releases.

Mitigation: Verify Maton CLI and SDK releases independently before deployment in sensitive environments.

## Reference(s):

- [ClawHub Salesforce Skill](https://clawhub.ai/byungkyu/skills/salesforce-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Salesforce REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)
- [Salesforce SOQL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)
- [Salesforce SOSL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl.htm)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated Salesforce API calls, Maton CLI commands, and configuration steps for user-approved CRM operations.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
