## Description:

Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to let an AI agent read and manage records, lists, notes, tasks, meetings, and related data in their connected Attio workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account can expose broad Attio workspace data and permit changes.

Mitigation: Protect the API key and limit the connected account's permissions.

Risk: Deletes, membership changes, and webhook destinations can have lasting or outbound effects.

Mitigation: Require explicit user approval before making these changes.

## Reference(s):

- [superagnt Attio integration documentation](https://superagnt.com/r/ch-attio-crm-docs)
- [Get a superagnt API key](https://superagnt.com/r/ch-attio-crm-key)
- [Connect an Attio account](https://app.superagnt.com/dashboard/connections)
- [MCP client installation guide](https://www.superagnt.com/install)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Attio API response data and concise task summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results and available actions depend on the connected Attio workspace and its permissions.]

## Skill Version(s):

2.0.10 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
