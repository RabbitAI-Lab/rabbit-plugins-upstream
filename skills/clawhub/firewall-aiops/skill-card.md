## Description:

Firewall AIops helps agents operate OPNsense and pfSense firewalls for health checks, rules, NAT, aliases, VPN, DHCP, diagnostics, RCA workflows, and governed firewall changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and firewall operators use this skill to inspect and troubleshoot OPNsense or pfSense firewall estates, including gateway health, rules, NAT, aliases, VPNs, DHCP, logs, and state tables. It can also propose and execute governed firewall changes when connected to an account with write permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make live firewall changes, including high-risk apply, reconfigure, reboot, service restart, and state-kill operations.

Mitigation: Use a least-privilege or read-only firewall API account unless write authority is intentionally required, and require operator approval outside the tool before high-risk actions.

Risk: The skill does not provide an in-tool approval gate or read-only switch, so authorization depends on the connected account and agent workflow.

Mitigation: Control permissions at the firewall API account and keep console or out-of-band access available during write operations.

Risk: Some operations are irreversible or audit-only, including reboot and committed changes.

Mitigation: Prefer dry runs and reversible staged edits where available, review pending changes before applying them, and use recorded undo entries for reversible writes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/firewall-aiops)
- [Project Homepage](https://github.com/AIops-tools/Firewall-AIops)
- [capabilities.md](references/capabilities.md)
- [agent-guardrails.md](references/agent-guardrails.md)
- [setup-guide.md](references/setup-guide.md)
- [cli-reference.md](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and structured tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include firewall observations, RCA findings, dry-run previews, audit-oriented change steps, and rollback guidance.]

## Skill Version(s):

0.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
