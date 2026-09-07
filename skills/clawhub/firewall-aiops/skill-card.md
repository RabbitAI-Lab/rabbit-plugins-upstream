## Description:

Firewall AIops helps agents operate OPNsense and pfSense firewalls through CLI and MCP tools for status, rules, NAT, VPN, DHCP, diagnostics, RCA, and governed writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, network operators, and agents use this skill to inspect and administer OPNsense or pfSense firewalls, including health checks, firewall rules, NAT, aliases, VPN, DHCP, logs, state tables, RCA workflows, and controlled change operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform live disruptive firewall changes and does not provide a built-in read-only mode or approval gate.

Mitigation: Start with a read-only firewall API account, enable write permissions only during controlled maintenance, and rely on firewall-side permissions for enforcement.

Risk: Operations such as reboot, apply_changes, reconfigure, and kill_states can interrupt service or active sessions.

Mitigation: Use dry-run previews where available, schedule high-risk actions in a maintenance window, and treat audited irreversible actions as requiring operator review.

Risk: Incorrect TLS settings can weaken production firewall administration.

Mitigation: Confirm TLS configuration before production use and enable certificate verification outside lab or self-signed-certificate environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/firewall-aiops)
- [Project homepage](https://github.com/AIops-tools/Firewall-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration examples, and structured firewall-operation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live firewall observations, RCA findings, risk-tier labels, dry-run previews, and audit or undo guidance.]

## Skill Version(s):

0.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
