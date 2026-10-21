## Description:

Helps agents inspect and troubleshoot OLVM and oVirt 4.5 engines using read-only inventory, health checks, and ranked diagnoses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to investigate OLVM or oVirt engine health, hosts, storage, virtual machines, events, and jobs without making engine changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Engine credentials or the master password could be exposed.

Mitigation: Use a read-only engine account, protect the local credential store, and safeguard OLVM_AIOPS_MASTER_PASSWORD.

Risk: Disabling TLS checks could expose the engine connection.

Mitigation: Keep TLS verification enabled and configure the engine CA.

Risk: Installing an unintended package release could change reviewed behavior.

Mitigation: Confirm that the uv or uvx package version matches the intended reviewed release.

## Reference(s):

- [OLVM AIops project homepage](https://github.com/AIops-tools/OLVM-AIops)
- [ClawHub skill listing](https://clawhub.ai/zw008/skills/olvm-aiops)
- [Setup and security guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown guidance with optional commands and structured diagnostic results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results may be partial when listing or scan limits are reached.]

## Skill Version(s):

0.6.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
