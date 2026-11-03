## Description:

Manage cold email campaigns, leads, and outreach analytics via Instantly AI through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and AI workflow authors use this integration to manage Instantly campaigns, leads, outreach analytics, and connected account settings through superagnt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected account actions can send emails, change or delete records, and reach administration, billing, API key, purchase, and webhook settings.

Mitigation: Use only the endpoints needed for the user's request; get explicit confirmation before sending, deleting, overwriting, changing administration or billing, creating keys, or making purchases. Review webhook destinations before use.

Risk: The integration uses an API key and a connected Instantly account.

Mitigation: Protect the API key and mail credentials, and limit the connected account's permissions where possible.

## Reference(s):

- [superagnt Instantly integration documentation](https://superagnt.com/r/ch-instantly-outreach-docs)
- [superagnt MCP server](https://mcp.superagnt.com/mcp)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON API responses and Markdown guidance with curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endpoint results vary; requests can read or modify the connected Instantly account.]

## Skill Version(s):

2.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
