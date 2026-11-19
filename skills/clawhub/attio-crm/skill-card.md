## Description:

Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CRM operators use the skill to connect AI agents and workflows to an Attio workspace, manage CRM records and activity, and automate related tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags workspace user and group administration beyond the described CRM purpose, along with account-credit access.

Mitigation: Before use, confirm those capabilities and the external destinations are necessary and intended, as the scan guidance recommends.

Risk: The documented API includes updates and deletions, including SCIM user and group administration.

Mitigation: Use only the endpoints needed for the user's request and obtain explicit confirmation before destructive or outbound actions, as the skill instructs.

## Reference(s):

- [Attio Integration documentation](https://superagnt.com/r/ch-attio-crm-docs)
- [MCP client setup](https://www.superagnt.com/install)
- [ClawHub skill listing](https://clawhub.ai/superagnt/skills/attio-crm)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with curl examples and JSON API payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and a connected Attio account; requests use the connected account's Attio access.]

## Skill Version(s):

2.0.17 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
