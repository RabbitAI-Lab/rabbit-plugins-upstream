## Description:

Look up official MCP Registry declarations and recent changes alongside Lowdown's daily observations of server reachability and tools before choosing or troubleshooting an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[petshopbros](https://clawhub.ai/user/petshopbros)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to check recorded MCP Registry declarations, recent changes, and dated observations when choosing, connecting to, or troubleshooting a server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queried MCP server names are sent to a public API.

Mitigation: Query only public Registry server names and avoid including sensitive information in requests.

Risk: Daily observations from one location may be mistaken for continuous availability.

Mitigation: Report observation dates and missing days, and do not present samples as uptime or a rating.

## Reference(s):

- [Lowdown API schema](https://lowdown-proxy.vercel.app/openapi.json)
- [Lowdown daily data and report](https://github.com/PetShopBros/lowdown-data)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dated, factual summaries of Registry records and daily observations; no server rating or uptime guarantee.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
