## Description:

Read Jobber Client Hub appointments, invoices, quotes, and work requests from a shell through the fpx CLI and a signed-in browser tab, instead of running the jobber-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch and parse their customer-side Jobber Client Hub data for scripts, shell workflows, and agent-assisted inspection when the MCP server is not installed. It is read-only and focuses on appointments, invoices, quotes, and work requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on fpx and the Transporter extension having browser-backed access to signed-in Jobber pages.

Mitigation: Install only if that access is acceptable, restrict browser extension site access to the narrow Jobber domain when possible, and revoke pairing or site access when finished.

Risk: The documented setup installs @fetchproxy/cli globally without pinning a version.

Mitigation: Prefer a pinned or local CLI install and review updates before use.

Risk: Jobber hub URLs and saved portal HTML can expose customer portal data.

Mitigation: Keep hub URLs out of shared shell history and committed files, avoid saving raw pages unless needed, and delete saved invoice or hub HTML after use.

Risk: Empty parser output can indicate a page mismatch or markup change rather than absence of records.

Mitigation: Check parser warnings and re-verify selectors against the live page before relying on empty results.

## Reference(s):

- [Recipes](references/recipes.md)
- [Why this skill does not use Jobber's documented API](references/why-not-the-api.md)
- [Client Hub parser](references/parse-clienthub.mjs)
- [Jobber Client Hub](https://clienthub.getjobber.com)
- [Jobber GraphQL API endpoint](https://api.getjobber.com/api/graphql)
- [Jobber OAuth token endpoint](https://api.getjobber.com/api/oauth/token)
- [Jobber OAuth authorization endpoint](https://api.getjobber.com/api/oauth/authorize)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON parser output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled parser reads HTML from stdin and writes structured JSON records for appointments, invoices, quotes, and work requests.]

## Skill Version(s):

0.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
