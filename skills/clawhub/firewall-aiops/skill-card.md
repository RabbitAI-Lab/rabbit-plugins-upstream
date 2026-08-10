## Description:

Governed OPNsense and pfSense firewall operations for health checks, rules, NAT, VPN, DHCP, root-cause analysis, and audited changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and managed service teams use this skill to inspect and operate OPNsense or pfSense firewalls, including health checks, rules, NAT, aliases, VPN, DHCP, logs, state tables, and common RCA workflows. It can also guide governed firewall changes such as toggling rules, editing alias entries, applying staged changes, restarting services, killing states, and rebooting when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make high-impact firewall changes without an in-tool approval gate or read-only mode.

Mitigation: Start with a dedicated read-only OPNsense/pfSense API account, grant write permissions only when needed, and require external human approval for apply_changes, reconfigure, reboot, service restarts, and state kills.

Risk: Firewall credentials, encrypted stores, and master-password environment variables are sensitive operational secrets.

Mitigation: Protect ~/.firewall-aiops, FIREWALL_AIOPS_MASTER_PASSWORD, and any legacy secret environment variables, and restrict filesystem access to the operator account.

Risk: TLS misconfiguration can expose firewall API traffic in production.

Mitigation: Verify TLS in production and reserve relaxed certificate settings for controlled lab environments.

Risk: Some operations are irreversible or audit-only, including reboot and committed firewall changes.

Mitigation: Use dry-run previews where available, confirm change windows externally, keep console or out-of-band access for high-risk operations, and validate the firewall state after each change.

## Reference(s):

- [Capabilities reference](artifact/references/capabilities.md)
- [Setup and security guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/firewall-aiops)
- [Project homepage](https://github.com/AIops-tools/Firewall-AIops)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured firewall-operation summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include firewall state summaries, RCA findings, dry-run previews, audit-aware change guidance, and configuration steps.]

## Skill Version(s):

0.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
