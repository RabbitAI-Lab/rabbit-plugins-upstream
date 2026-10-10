## Description:

Helps agents provision and manage cloud compute, use decentralized inference, deploy hosted agents and paid endpoints, and back up agent state through x402 Compute services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to provision GPU and VPS instances, access inference and embeddings, deploy persistent agent pods or paid processors, and manage encrypted agent backups with wallet or credit payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud provisioning, payments, and instance deletion can incur charges or remove resources.

Mitigation: Confirm costs, payment amounts, target resources, and destructive actions with the user before execution.

Risk: Wallet keys and management credentials can authorize payments or control cloud resources.

Mitigation: Use dedicated low-balance wallets, protect credentials, and grant only the access needed for each task.

Risk: Remote installation and persistent hosted agents can extend access beyond the current session.

Mitigation: Review installation sources and hosted-agent permissions before deployment; monitor and revoke access when no longer needed.

## Reference(s):

- [x402 Compute documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [x402 Compute dashboard](https://cloud.x402compute.cc)
- [ClawHub skill release](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [Compute API reference](artifact/references/api-reference.md)
- [Agent Pods API reference](artifact/references/agent-pods-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with commands, configuration examples, and API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide paid cloud operations and persistent service management.]

## Skill Version(s):

1.32.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
