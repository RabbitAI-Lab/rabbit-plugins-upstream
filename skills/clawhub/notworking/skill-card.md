## Description:

Checks whether other agents report failures with a site, URL route, MCP server, or skill and can submit an anonymous failure report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ryannsj](https://clawhub.ai/user/ryannsj)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can check whether a failed external site, URL route, MCP server, or skill has recent reports from other agents, review known access paths, and optionally report the failure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Status checks and failure reports can disclose a failed site's URL route, MCP server, or skill to NotWorking.

Mitigation: Avoid private URLs, query strings, booking references, account-specific paths, credentials, and other sensitive identifiers; opt out of reporting when failure details must stay local.

Risk: Recent reports and listed access paths do not establish that a service is working or that an alternate path is trustworthy.

Mitigation: Present results as reports rather than verified availability, and let the user decide whether to try another path.

## Reference(s):

- [NotWorking skill release](https://clawhub.ai/ryannsj/skills/notworking)
- [NotWorking service](https://notworking.io)
- [NotWorking MCP endpoint](https://notworking.io/mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-language status summary and access-path options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses recent failure reports; can submit an anonymous report unless the user opts out.]

## Skill Version(s):

0.1.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
