## Description:

Spin up, SSH into, run commands on, and tear down Linux servers from Claude, with payment by USDC over x402 or card.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luiscosio](https://clawhub.ai/user/luiscosio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let Claude provision, access, operate, renew, and destroy real Linux servers for deployments, command execution, hosting, or temporary agent-owned compute.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent payment credentials, root server control, and server destruction authority.

Mitigation: Use a dedicated low-balance wallet, set AGENTMETAL_MAX_USDC, keep the AgentMetal API key in secret storage, and require explicit approval before spending money, running root commands, opening firewall ports, renewing leases, or destroying servers.

Risk: Managed SSH keys and account keys can expose privileged infrastructure access.

Mitigation: Avoid exposing raw private keys where possible, limit access to managed-key servers, and review command proposals before execution.

## Reference(s):

- [AgentMetal API documentation for agents](https://api.agentmetal.dev/llms.txt)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, API calls, Code]

**Output Format:** [Markdown with JSON configuration and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool names, payment and wallet setup guidance, server lifecycle steps, command execution instructions, and firewall or destruction actions that require explicit review.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
