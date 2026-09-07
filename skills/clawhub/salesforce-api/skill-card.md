## Description:

Salesforce CRM API integration with managed OAuth for querying, administering, and carefully modifying Salesforce records through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CRM administrators use this skill to access Salesforce REST APIs, run SOQL and SOSL queries, inspect sObjects, and perform approved CRUD, batch, or composite operations with managed OAuth credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change Salesforce CRM data, including destructive or batch operations.

Mitigation: Use OAuth with least privilege, prefer sandbox or read-only scopes when possible, and require explicit approval after checking object type, record IDs, payload, and consequence before writes or deletes.

Risk: Multiple Salesforce or Maton connections can make the target account ambiguous.

Mitigation: Pin the intended connection ID and verify the account context before each request, especially before any operation that changes data.

Risk: Fallback API-key usage can expose a long-lived credential if printed, exported broadly, or persisted.

Mitigation: Prefer OAuth through the Maton CLI, avoid exposing MATON_API_KEY to unnecessary child processes, and rotate the key if it is printed, committed, or pasted.

## Reference(s):

- [ClawHub Salesforce Skill](https://clawhub.ai/byungkyu/skills/salesforce-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Salesforce REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)
- [Salesforce SOQL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)
- [Salesforce SOSL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl.htm)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Salesforce connection authorized with the narrowest practical permissions.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
