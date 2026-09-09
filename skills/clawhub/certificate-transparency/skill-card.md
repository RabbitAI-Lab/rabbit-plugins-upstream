## Description:

CTlogs MCP connects an assistant to CTlogs.io so it can perform read-only Certificate Transparency lookups for subdomains, certificates, hostnames, index status, and account quota.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abtdomain](https://clawhub.ai/user/abtdomain)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security teams, and brand protection teams use this skill to connect MCP-capable assistants to CTlogs.io and ask targeted questions about public Certificate Transparency data. It supports infrastructure review, certificate history lookup, hostname search, index freshness checks, and quota checks through a read-only hosted connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Assistant queries can consume the user's CTlogs.io account allowance.

Mitigation: Review plan limits before installation and use the account quota tool or CTlogs account pages to monitor remaining allowance.

Risk: Certificate Transparency records can be mistaken for proof that a host is currently live or actively serving content.

Mitigation: Confirm important findings with DNS, HTTP, certificate, or internal asset inventory checks before taking operational action.

Risk: The connector sends lookup requests to the hosted CTlogs.io MCP service.

Mitigation: Install only for MCP clients that should use CTlogs.io and review the service terms, privacy policy, and plan limits before connecting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/abtdomain/skills/certificate-transparency)
- [CTlogs.io](https://ctlogs.io)
- [CTlogs.io API documentation](https://ctlogs.io/docs)
- [CTlogs.io pricing](https://ctlogs.io/pricing)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [What Certificate Transparency actually tells you](https://ctlogs.io/blog/what-certificate-transparency-actually-tells-you)
- [ABTdomain GitHub organization](https://github.com/ABTdomain)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only MCP connector guidance; live query results depend on the user's CTlogs.io account plan and allowance.]

## Skill Version(s):

0.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
