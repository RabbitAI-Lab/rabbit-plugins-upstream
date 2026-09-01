## Description:

vmware-monitor helps agents perform safe, read-only VMware vCenter and ESXi monitoring, inventory lookup, health triage, event review, and object investigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators, developers, and support engineers use this skill to inspect VMware environments, summarize cluster and cross-vCenter health, investigate VMs, hosts, and datastores, and route any needed remediation to companion write-capable skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs read access to VMware vCenter or ESXi inventory and health data.

Mitigation: Use a least-privilege read-only vCenter or ESXi account and install only when that access level is acceptable.

Risk: Credentials may be stored in ~/.vmware-monitor/.env, and base64 values are obfuscation rather than encryption.

Mitigation: Protect the file with mode 600 and prefer a secret manager or injected environment variables for production credentials.

Risk: Disabling TLS verification can expose monitoring sessions outside isolated lab environments.

Mitigation: Keep TLS verification enabled in production and use CA-signed certificates.

Risk: Optional daemon and webhook features can send aggregated alert metadata to configured endpoints.

Mitigation: Enable the daemon or webhooks only intentionally and use endpoints approved for infrastructure alert metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-monitor)
- [VMware Monitor homepage](https://github.com/vmware-skills/VMware-Monitor)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Health Summary Template](references/health-summary-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, structured MCP results, terminal tables, and optional self-contained HTML snapshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only VMware monitoring outputs; list-style MCP tools report returned, limit, total, truncated, and hint fields when available.]

## Skill Version(s):

1.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
