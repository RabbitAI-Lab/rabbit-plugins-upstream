## Description:

Helps agents query and manage Salesforce CRM records through a Maton connection with managed OAuth authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CRM administrators use this skill to query Salesforce records, manage sObjects, and carry out approved record changes or automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Salesforce access or changes to the wrong account can expose or alter CRM data.

Mitigation: Use the narrowest available scopes and sandbox orgs where possible, verify the connection ID, and approve the exact records and consequences before writes.

Risk: Deletes, batch changes, functions, triggers, and destinations can make irreversible or automated changes.

Mitigation: Require explicit per-record approval for destructive and batch work and separate approval before enabling automation or destinations.

Risk: Raw API keys and unused connections can leave credentials exposed or access active unnecessarily.

Mitigation: Prefer the CLI's managed authentication; avoid raw keys unless the CLI is unavailable, and revoke connections or automation when finished.

## Reference(s):

- [ClawHub Salesforce skill release](https://clawhub.ai/byungkyu/skills/salesforce-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Salesforce REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with shell, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Salesforce responses may contain sensitive CRM records; limit results to task-relevant fields.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
