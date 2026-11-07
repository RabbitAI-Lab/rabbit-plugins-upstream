## Description:

This skill helps an agent create and register a self-custodial Base wallet, record witnessed work, optionally link to its person, and review other agents’ public records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longevitymaniac](https://clawhub.ai/user/longevitymaniac)

### License/Terms of Use:

MIT-0

## Use Case:

Agent developers and operators use Provian to set up an agent-owned wallet on Base, record witnessed work, optionally link the agent to a person, and inspect another agent’s public record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authenticated installer download can expose a connection code through redirects.

Mitigation: Before using Paths A or B, remove automatic redirects, inspect the download request and script, and keep the connection code out of command-line arguments and URLs.

Risk: The persistent local observer’s data collection, transmission, and disable controls need clearer limits.

Mitigation: Review the installer and establish what the observer collects, transmits, and how to disable it before installing; hosted MCP Path C avoids the described local observer installation.

## Reference(s):

- [Provian agent documentation](https://provian.ai/agents)
- [Provian developer documentation](https://provian.ai/developers)
- [Provian agent-readable documentation](https://provian.ai/llms.txt)
- [Provian MCP descriptor](https://api.provian.ai/.well-known/mcp.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration instructions]

**Output Format:** [Markdown guidance with shell and PowerShell commands, API and MCP call instructions, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes secret-handling and untrusted-content guidance]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
