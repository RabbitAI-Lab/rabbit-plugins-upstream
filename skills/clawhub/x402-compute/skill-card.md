## Description:

Helps agents provision and manage compute resources, hosted agent pods, inference services, paid processors, training jobs, and agent backups through the x402 Compute platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and engineers use this skill to deploy and manage GPU/VPS compute, hosted agents, inference endpoints, and related paid services. It also guides workflows for training, grid participation, and encrypted agent backup or migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional node setup runs a remote installer without first pinning or verifying it.

Mitigation: Skip the node installer for cloud-only use. If running a node, obtain and verify a pinned release and use an isolated environment.

Risk: Payment signing and compute management can expose funds or credentials to unintended spending.

Mitigation: Use a dedicated low-balance wallet, explicit spending limits, and scoped API keys.

Risk: Backup, renewal, or deletion actions can affect sensitive data or active resources.

Mitigation: Review backup contents, renewal settings, and deletion targets before proceeding.

## Reference(s):

- [x402 Compute Documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [ClawHub Release](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402 Compute Cloud](https://cloud.x402compute.cc)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance, shell commands, configuration values, and structured service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate paid provisioning, lifecycle, or payment operations when authorized.]

## Skill Version(s):

1.34.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
