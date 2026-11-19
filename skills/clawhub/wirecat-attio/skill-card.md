## Description:

Use attio to read an Attio workspace's CRM - deals with their stage, owner, amount, company and people, the deal pipeline and its stages, people, companies, workspace members and the workspace's own attributes - with the owner's profile and JSON answers; deals are synced into the local WireCat store. Use when a question could be answered from the owner's Attio sales data (how a deal stands, what is open, who a client is, what changed), or to call an Attio API operation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and sales or operations teams use the skill to answer questions from an Attio workspace's CRM, check synced deal and pipeline data, and perform a requested operation through Attio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attio API operations can change or delete real workspace data.

Mitigation: Review the selected profile, target, and permissions before a write or delete; use --dry-run to inspect writes where supported.

Risk: The security evidence says the scan was partial and one local reference could not be resolved.

Mitigation: Review the relevant API reference and check sync completeness and issues before relying on CRM results.

## Reference(s):

- [Attio API operation reference](references/api.md)
- [Attio Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-attio)
- [Publisher profile: wirecat](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [JSON CRM results with concise natural-language answers; shell commands for Attio CLI operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Synced CRM data may be partial or out of date; the skill directs users to check sync status and issues.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
