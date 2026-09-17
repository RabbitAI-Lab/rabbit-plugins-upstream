## Description:

Read Jobber Client Hub appointments, quotes, invoices, and work requests from a shell with the fpx CLI instead of running the jobber-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve customer-side Jobber Client Hub data for appointments, invoices, quotes, and work requests from an authenticated browser-backed shell workflow. It is intended for read-only local extraction and scripting when the Jobber MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a persistent browser-backed fetch capability that can use a signed-in Jobber Client Hub session.

Mitigation: Keep the hub URL private, avoid storing it in committed files or shared shell history, and revoke the fpx/Transporter pairing when finished.

Risk: The security evidence flags an unpinned globally installed third-party CLI dependency.

Mitigation: Review the CLI before installation and prefer a pinned or local install if available.

Risk: The browser access profile may be broader than the exact portal host.

Mitigation: Use fetch-only capability and scope the profile or browser extension site access to clienthub.getjobber.com when supported.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Parser script](references/parse-clienthub.mjs)
- [Recipes](references/recipes.md)
- [Why this skill does not use Jobber's documented API](references/why-not-the-api.md)
- [Jobber Client Hub](https://clienthub.getjobber.com)
- [Jobber GraphQL API endpoint](https://api.getjobber.com/api/graphql)
- [Jobber OAuth token endpoint](https://api.getjobber.com/api/oauth/token)
- [Jobber OAuth authorization endpoint](https://api.getjobber.com/api/oauth/authorize)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and a Node.js parser that emits JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Jobber Client Hub extraction for appointments, invoices, quotes, and work requests; no writes, payments, or file downloads.]

## Skill Version(s):

0.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
