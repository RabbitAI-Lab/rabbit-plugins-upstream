## Description:

Query etix.com event-ticketing data from a shell with the fpx CLI, using a signed-in browser tab to search events, venues, and performers and retrieve event or venue detail without running the etix-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to query public Etix event-discovery data from shell workflows when the MCP server is not installed or not desired. It supports resolving IDs, fetching event and venue details, and parsing JSON or HTML response data through fpx.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Etix requests are routed through the Transporter browser extension and a paired fpx profile, which can expose browser session context to the workflow.

Mitigation: Use a dedicated browser profile or Etix tab, limit Chrome site access to etix.com, and install only if this routing model is acceptable.

Risk: Example commands write fetched Etix HTML or JSON to /tmp files.

Mitigation: Delete temporary files after use, especially on shared machines.

Risk: Etix HTML fetches can succeed at the transport layer while returning a DataDome interstitial instead of event or venue content.

Mitigation: Check for captcha-delivery or similar interstitial text before parsing saved HTML.

## Reference(s):

- [Etix consumer endpoints for fpx](references/etix-endpoints.md)
- [extract-datalayer.mjs](references/extract-datalayer.mjs)

## Skill Output:

**Output Type(s):** [markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with shell commands and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may produce fpx command output as JSON or parsed HTML-derived event and venue data.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
