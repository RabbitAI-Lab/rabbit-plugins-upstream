## Description:

Rent a confidential VM (Intel TDX) by the hour with USDC over x402 and run a Docker workload on it. No signup; the paying wallet owns the machine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentgates](https://clawhub.ai/user/agentgates)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to price and deploy Docker workloads on hourly confidential VMs, paying in USDC through x402. It helps an agent retrieve deployment status, an endpoint, and attestation details after the VM is running.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A deployment payment can incur hourly USDC charges.

Mitigation: Read the current 402 offer and verify its network, recipient, and amount before signing. Obtain human approval or stay within an explicitly authorized budget.

Risk: The confidential-enclave claims have not been independently verified, and workloads or secrets are sent to the service.

Mitigation: Send only workloads and secrets intended for Agentgates; keep secrets re-settable and do not rely on unverified confidentiality claims.

Risk: A VM can run and bill without being reachable if its workload publishes no port.

Mitigation: Check that the compose configuration publishes the required port before deploying.

## Reference(s):

- [Agentgates Compute API documentation](https://api.agentgates.ai/api/compute/docs)
- [Agentgates Compute MCP service](https://mcp.agentgates.ai/compute)

## Skill Output:

**Output Type(s):** [API Calls, Configuration, Guidance]

**Output Format:** [Structured API requests and deployment status details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment incurs hourly USDC charges; confirm the current price and authorization before paying.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
