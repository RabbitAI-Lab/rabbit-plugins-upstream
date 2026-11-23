## Description:

Charter Compute lets agents run Python jobs, fetch web pages, and rent a persistent Linux home, with usage billed in USDC on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drew-dot-com](https://clawhub.ai/user/drew-dot-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Charter Compute to run bounded Python work, retrieve pages through a browser, or rent a persistent Linux home when they need compute or network access outside their current environment. Paid operations use USDC on Base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unpinned `npx -y charter-mcp` command may run a changed package release with local permissions.

Mitigation: Use an audited exact package version or a reviewed, locked installation before running it.

Risk: The operator of a rented home can read its disk.

Mitigation: Avoid storing sensitive data or credentials on a rented home.

## Reference(s):

- [Charter Compute on ClawHub](https://clawhub.ai/drew-dot-com/skills/charter-compute)
- [Charter agent documentation](https://charter.mainnet.toonprotocol.dev/agents)
- [Charter machine-readable documentation](https://charter.mainnet.toonprotocol.dev/llms.txt)
- [Charter grant fund](https://charter.mainnet.toonprotocol.dev/grants)
- [Charter MCP source linked by the skill](https://github.com/drew-dot-com/charter/tree/main/mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions]

**Output Format:** [Shell commands plus JSON results containing execution output, fetched page text, wallet or grant status, and lease details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid calls are billed by the hour; Python jobs are limited to the documented runtime environment and script size.]

## Skill Version(s):

0.3.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
