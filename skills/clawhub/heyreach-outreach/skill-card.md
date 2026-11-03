## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow authors use this skill to manage HeyReach LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outbound messages, destructive changes, or account administration can affect the connected HeyReach workspace.

Mitigation: Use only the endpoints needed for the user's request, and get explicit confirmation before sending messages, deleting or changing records, or performing sensitive account administration.

Risk: The bundled curl examples have quote escaping that needs correction before execution.

Mitigation: Review and correct the shell quoting in each example before running it.

## Reference(s):

- [HeyReach Integration Documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [superagnt MCP Installation Guide](https://www.superagnt.com/install)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Guidance]

**Output Format:** [Markdown guidance with curl examples and API tool operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operations act on the user's connected HeyReach workspace using SUPERAGNT_API_KEY.]

## Skill Version(s):

2.0.12 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
