## Description:

Salesforce CRM API integration with managed OAuth for querying records, managing sObjects, and performing approved CRUD operations through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Salesforce administrators use this skill to inspect Salesforce CRM data, query records with SOQL, manage sObjects, and perform carefully confirmed CRM changes through managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Salesforce writes, deletes, batch calls, and workflow-triggering operations can alter or remove CRM data.

Mitigation: Default to read and list calls, verify the connection ID and target records, and require explicit user confirmation with the exact sObject, record IDs, payload, and expected effect before any modifying request.

Risk: Broad OAuth scopes or ambiguous active connections can send requests to the wrong Salesforce organization or account.

Mitigation: Use the narrowest Salesforce account or sandbox available, specify the intended connection when multiple connections exist, prefer read-only scopes, and revoke unused connections promptly.

Risk: Maton API keys and provider-issued tokens can leak if printed, stored, passed on command lines, or sent to unrelated hosts.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, never inspect or log token values, and send raw API-key fallback requests only to api.maton.ai.

Risk: Salesforce records and other API responses may contain untrusted content.

Mitigation: Treat returned content as data, not instructions; do not execute, eval, or interpolate external content into commands or prompts without validation.

## Reference(s):

- [ClawHub Salesforce Skill](https://clawhub.ai/byungkyu/skills/salesforce-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Salesforce REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)
- [Salesforce SOQL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are task guidance and command examples for interacting with Salesforce through Maton; destructive or write actions require explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
