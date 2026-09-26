## Description:

Salesforce CRM API integration with managed OAuth for querying records, managing sObjects, and performing approved CRUD operations on Salesforce data through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, administrators, and operations teams use this skill to access Salesforce CRM data through managed OAuth, run SOQL queries, inspect object metadata, and perform approved record changes. It is intended for Salesforce administration workflows where account selection, narrow permissions, and record-level confirmation matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, delete, and batch-change Salesforce CRM records.

Mitigation: Default to read and list operations; require exact sObject, record IDs, intended effect, and explicit user approval before any write or destructive action.

Risk: A wrong Salesforce connection or broad OAuth scope can expose or mutate unintended business data.

Mitigation: Use the narrowest Salesforce scopes, prefer sandbox orgs for destructive or batch work, and verify the intended connection ID before each request.

Risk: Hosted functions and persistent trigger destinations can run or forward data repeatedly after setup.

Mitigation: Require separate approval for function deployment, invocation, trigger setup, and persistent destinations; keep destinations on approved Maton hosts unless the user names and approves an external host.

Risk: Long-lived API keys or destination headers can expose credentials.

Mitigation: Prefer OAuth, avoid exporting MATON_API_KEY, store credentials only through the managed credential store, and never place Maton or provider tokens in trigger destination headers.

## Reference(s):

- [ClawHub Salesforce Skill](https://clawhub.ai/byungkyu/skills/salesforce-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Salesforce REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)
- [Salesforce SOQL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should emphasize read/list calls by default and require explicit user approval for writes, connection creation, destructive actions, hosted functions, and persistent trigger destinations.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
