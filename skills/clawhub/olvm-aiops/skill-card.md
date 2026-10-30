## Description:

Inspects OLVM and oVirt 4.5 engines and returns inventory, health, capacity, event, and ranked diagnostic findings through read-only CLI and MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Virtualization administrators and engineers use the skill to inspect OLVM or oVirt 4.5 environments, review inventory and recent activity, and diagnose engine, host, storage, and VM health issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Engine credentials and local configuration or audit files could expose access or operational information if mishandled.

Mitigation: Use a dedicated read-only engine account, protect the master password and local files, and follow the encrypted secret-store setup.

Risk: Disabling TLS verification can expose engine credentials or session traffic to interception.

Mitigation: Keep TLS verification enabled and configure the engine CA certificate.

Risk: Audit storage warnings can mean the local log is incomplete.

Mitigation: Check audit warnings and health before relying on the log as a complete record.

Risk: An unreviewed standalone MCP package version may introduce unexpected behavior.

Mitigation: Pin the package to a reviewed version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/olvm-aiops)
- [Project homepage](https://github.com/AIops-tools/OLVM-AIops)
- [Capabilities](artifact/references/capabilities.md)
- [Setup and security guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Structured JSON findings and concise diagnostic text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are ranked and include measured signals, causes, and suggested actions; results indicate when scans are truncated.]

## Skill Version(s):

0.7.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
