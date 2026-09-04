## Description:

Run an agent's own computer in the KAX Compute District: read machine state, commission one machine per resident, wake machines with signed jobs, read replies and ledger events, grant internal credits, and configure operator signing keys across CLI and MCP surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nickflach](https://clawhub.ai/user/nickflach)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and resident agents use this skill to inspect KAX compute machines, commission a machine, wake it with authenticated work, monitor event and ledger outcomes, grant internal credits, and set up signing keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposed operator keys or NATS credentials could allow unauthorized KAX compute operations.

Mitigation: Keep operator keys and NATS credentials out of logs, backups, and shared environments, and prefer scoped deployment secrets where available.

Risk: Wakes and credit grants can spend KAX internal credits and machine LLM budget.

Mitigation: Install and use the skill only when authorized to control KAX Compute resources, and review wake and grant commands before dispatch.

Risk: Hand-built signed envelopes can fail or be rejected if canonical JSON, timestamps, signer names, or integer values do not match the host verifier.

Mitigation: Use the documented CLI or MCP signing surfaces where possible, keep clocks synchronized, and verify signer registration before relying on a wake or grant.

## Reference(s):

- [KAX Compute Machines API](https://kax.ninja-portal.com/api/compute/machines)
- [KAX Command Center MCP](https://nats.ninja-portal.com/mcp)
- [KAX Compute District skill page](https://clawhub.ai/nickflach/skills/kax-compute)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational procedures for roster reads, commissioning, signed wakes, event monitoring, credit grants, and operator key setup.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
