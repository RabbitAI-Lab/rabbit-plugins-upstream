## Description:

Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and sales or operations teams use the skill to query and manage Attio CRM data and automate record, list, activity, and meeting workflows through an AI agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration can access broad Attio workspace data and perform administrative, destructive, or outbound actions.

Mitigation: Limit connected-account permissions to what is needed, use only task-relevant endpoints, and explicitly approve administrative changes, deletions, and webhook destinations.

Risk: The skill requires a superagnt API key, offers optional MCP consent, and security guidance flags malformed shell examples.

Mitigation: Configure the API key securely, review MCP consent, and correct malformed shell examples before use.

## Reference(s):

- [superagnt Attio documentation](https://superagnt.com/r/ch-attio-crm-docs)
- [superagnt MCP installation](https://www.superagnt.com/install)
- [superagnt connections page](https://app.superagnt.com/dashboard/connections)
- [Attio Integration listing](https://clawhub.ai/superagnt/skills/attio-crm)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with endpoint schemas, JSON request examples, and curl commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operations use the connected Attio account and API key; account permissions and API responses determine available results.]

## Skill Version(s):

2.0.11 (source: artifact frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
