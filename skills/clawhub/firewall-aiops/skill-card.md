## Description:

Firewall AIops helps agents operate OPNsense and pfSense firewalls, covering health checks, rules, NAT, aliases, VPN, DHCP, logs, RCA workflows, and governed write operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network administrators, SREs, and security engineers use this skill to inspect and troubleshoot OPNsense or pfSense firewalls, then plan or execute governed changes such as rule toggles, alias updates, state kills, service restarts, commits, and reboots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact firewall write actions can change live rules, aliases, states, services, or appliance availability without a built-in approval gate.

Mitigation: Use a read-only OPNsense or pfSense API account by default, grant write permissions only for planned change windows, and require explicit operator approval before MCP write calls.

Risk: A trusted agent or over-permissioned account could apply disruptive firewall changes.

Mitigation: Install the skill only for trusted agents and accounts, review dry-run output first, and keep local audit annotations for change accountability.

Risk: Firewall credentials and backups under ~/.firewall-aiops could expose operational access if mishandled.

Mitigation: Protect ~/.firewall-aiops and backups, avoid broadly visible master-password environment variables, and migrate away from legacy plaintext secret fallbacks.

Risk: TLS configuration guidance is mixed across artifacts and weak verification can hide man-in-the-middle risk.

Mitigation: Verify TLS settings during setup and use certificate verification for production firewall connections.

## Reference(s):

- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Project homepage](https://github.com/AIops-tools/Firewall-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/firewall-aiops)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured firewall-operation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include firewall status summaries, RCA findings, dry-run recommendations, audit guidance, and governed write proposals.]

## Skill Version(s):

0.12.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
