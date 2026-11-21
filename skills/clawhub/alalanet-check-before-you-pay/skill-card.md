## Description:

Before installing a package, repository, skill or MCP server, check it (known malicious, typosquats, names that do not exist); before paying an x402 endpoint or connecting to a remote MCP server, check that it is alive and that its price and payment address match its listing. Free, no sign-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alalaalex](https://clawhub.ai/user/alalaalex)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use alalanet to check packages, repositories, skills, and MCP servers before installing or connecting, and to review service status and payment terms before paying an x402 endpoint. It returns signed check results and guidance for deciding whether to proceed, pause, or avoid an action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security scanners rate the skill suspicious, reporting a mismatch between its advertised checks and reported receipt-signing and external publishing behavior. Scan coverage is partial.

Mitigation: Consider avoiding installation until the publisher clarifies the reported behavior and how private repository content is handled. If proceeding, do not submit private files or use the signing-key workflow unless you understand and accept those actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/alalaalex/skills/alalanet-check-before-you-pay)
- [alalanet MCP server](https://alalanet.com/mcp)
- [alalanet service check API](https://alalanet.com/v1/check?url=<endpoint-url>)

## Skill Output:

**Output Type(s):** [Guidance, Structured data]

**Output Format:** [Signed structured check results with human-readable guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts and reasons for installation, connection, service, and payment checks; scan coverage for this release is partial.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
