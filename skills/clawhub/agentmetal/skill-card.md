## Description:

Helps agents rent and operate Linux servers through AgentMetal, with USDC or card payment options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luiscosio](https://clawhub.ai/user/luiscosio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to select, rent, configure, and manage paid Linux servers for deployments or remote commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment workflows can spend real USDC or incur card charges for prepaid server leases and add-ons.

Mitigation: Keep wallet keys private, set a low AGENTMETAL_MAX_USDC limit, and require approval after showing the plan, duration, and total cost before each payment.

Risk: Remote exec can run commands as root on a paid server.

Mitigation: Scope API keys tightly and require approval after showing the server ID, exact command, and consequences before execution.

Risk: Rebooting or destroying servers can interrupt services or delete workloads.

Mitigation: Require approval after showing the server ID and destructive consequences before reboot or destroy actions; confirm lease extensions and add-ons separately.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/luiscosio/skills/agentmetal)
- [AgentMetal homepage](https://agentmetal.dev)
- [AgentMetal agent manual](https://api.agentmetal.dev/llms.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples and CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes server identifiers, addresses, lease expiry, and command results when operations succeed.]

## Skill Version(s):

0.3.3 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
