## Description:

Salesforce provides CRM API integration through Maton-managed OAuth, helping agents query records with SOQL, manage sObjects, and perform Salesforce CRUD operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CRM operators use this skill to let an agent inspect and administer Salesforce data through Maton CLI and SDK workflows. It is intended for read-first CRM administration with explicit confirmation before connection creation, record mutation, batch operations, or raw API writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can mutate Salesforce CRM data through injected credentials, including create, update, delete, batch, composite, workflow, messaging, sharing, and other write operations.

Mitigation: Use sandbox or least-privilege Salesforce accounts where possible, start with read/list calls, verify the exact sObject and record IDs, and require explicit record-level confirmation before writes.

Risk: `maton api` can reach broader Salesforce REST endpoints than the curated examples imply.

Mitigation: Prefer documented Salesforce endpoint paths, specify the intended connection, and require extra review before raw API, batch, composite, or workflow requests.

Risk: Maton API keys and provider-issued tokens can be exposed through logs, command arguments, files, or environment leakage.

Mitigation: Prefer OAuth with the operating system credential store, never print or persist credentials, and send API keys only to `api.maton.ai` when the CLI cannot be used.

## Reference(s):

- [ClawHub Salesforce Skill](https://clawhub.ai/byungkyu/skills/salesforce-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Salesforce REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)
- [SOQL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)
- [SOSL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl.htm)
- [Related ClawHub API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with CLI commands, JSON examples, and SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Salesforce connection.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
