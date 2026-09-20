## Description:

OLVM AIops helps agents inspect and troubleshoot Oracle Linux Virtualization Manager and oVirt 4.5 engines through read-only inventory, event, health, capacity, and diagnosis workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to investigate OLVM or oVirt engine health, host and VM status, storage capacity, jobs, and recent events. It is suited for read-only diagnostics and guided troubleshooting where the agent should report ranked findings and measured signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or invoking an unreviewed package could run code from a source the operator has not approved.

Mitigation: Confirm trust in the olvm-aiops package source and prefer a pinned, reviewed version before installing or using the skill.

Risk: Local configuration, audit data, and encrypted credentials are stored under ~/.olvm-aiops by default.

Mitigation: Keep ~/.olvm-aiops private, protect the master password, and avoid legacy plaintext password environment variables.

Risk: An overly privileged engine account or disabled TLS verification can expand operational impact even though this release is read-only.

Mitigation: Connect with a read-only OLVM/oVirt account, keep TLS verification enabled, and use the engine CA and FQDN except on disposable lab engines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/olvm-aiops)
- [Project homepage](https://github.com/AIops-tools/OLVM-AIops)
- [Setup and security guide](artifact/references/setup-guide.md)
- [Capabilities reference](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured diagnostic guidance with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostic recommendations, ranked findings, quoted measured signals, setup guidance, and CLI or MCP usage instructions.]

## Skill Version(s):

0.4.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
