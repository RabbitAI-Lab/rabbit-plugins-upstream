## Description:

Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to read and manage Attio CRM data, automate workspace workflows, and work with lists, notes, tasks, meetings, files, and identity records through the connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary notes account-credit access, SCIM identity administration, and external API calls that extend beyond basic CRM operations.

Mitigation: Use only the endpoints needed for the requested task; consider whether the broader credit and identity-management capabilities are needed, and verify that you trust the API destination before using an API key.

Risk: The documented API surface includes destructive changes and actions that can be performed as the connected user.

Mitigation: Follow the skill's instruction to get explicit confirmation before deleting, overwriting, or sending anything on the user's behalf.

## Reference(s):

- [Documentation](https://superagnt.com/r/ch-attio-crm-docs)
- [MCP installation instructions](https://www.superagnt.com/install)
- [Attio Integration on ClawHub](https://clawhub.ai/superagnt/skills/attio-crm)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with curl examples and JSON API data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SUPERAGNT_API_KEY and a connected Attio account. Actions and returned data depend on the user's account permissions.]

## Skill Version(s):

2.0.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
