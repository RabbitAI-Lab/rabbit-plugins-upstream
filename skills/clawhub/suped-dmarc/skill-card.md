## Description:

DMARC monitoring and report analysis with Suped. Inspect SPF/DKIM authentication issues, domains and raw report XML; add domains and onboard MSP clients through Suped's OAuth MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[suped](https://clawhub.ai/user/suped)

### License/Terms of Use:

MIT-0

## Use Case:

Operators use this skill to review Suped DMARC reports, investigate SPF/DKIM issues, and manage domains or MSP clients in an organization they select.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account can expose DMARC reports and permit domain or MSP client additions within the user's existing permissions.

Mitigation: Confirm the target organization before accessing its data or requesting additions.

Risk: A shared OAuth connection uses the operator's Suped account across requests.

Mitigation: Configure separate requester accounts when multiple users need independent access.

Risk: A successful MSP client creation creates another client, so retrying an uncertain creation can create a duplicate.

Mitigation: Inspect current organizations before retrying when a creation result is uncertain.

## Reference(s):

- [Suped MCP documentation](https://www.suped.com/docs/mcp)
- [OpenClaw MCP OAuth documentation](https://docs.openclaw.ai/cli/mcp/transports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries of DMARC reports, authentication results, and saved issue statuses; may include returned raw report XML when requested.]

## Skill Version(s):

1.0.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
