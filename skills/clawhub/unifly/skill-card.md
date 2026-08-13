## Description:

unifly helps agents manage Ubiquiti UniFi network infrastructure through the unifly CLI, covering devices, clients, networks, WiFi, firewall policies, NAT, DNS, VPN, monitoring, backups, and raw API workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hyperb1iss](https://clawhub.ai/user/hyperb1iss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, network engineers, and authorized administrators use this skill to inspect and operate UniFi environments through structured CLI workflows. It is intended for live network administration tasks such as provisioning VLANs and WiFi, managing firewall and NAT policy, monitoring events and health, administering VPNs, and producing repeatable configuration payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad live UniFi network administration, including changes to devices, clients, networks, firewall policy, NAT, VPN, DNS, backups, and raw API calls.

Mitigation: Install it only for users authorized to administer the target UniFi environment and require review of the resolved profile, auth mode, target site, and planned mutations before execution.

Risk: Commands such as delete, reboot, poweroff, voucher purge, backup deletion, VPN changes, and bulk device operations can disrupt connectivity or remove operational state.

Mitigation: Require an explicit human-readable summary before destructive operations, avoid unattended use of --yes unless already approved, and verify state after each mutation.

Risk: The raw API passthrough can reach endpoints not covered by higher-level command safeguards.

Mitigation: Prefer wrapped unifly commands when available and require explicit review of raw API path, method, payload, and target controller before running passthrough calls.

Risk: Event streams, JSON outputs, vouchers, VPN payloads, controller profiles, and operational exports may contain sensitive network or credential-related data.

Mitigation: Treat generated outputs as sensitive, redact secrets before sharing, use demo or sanitized output when appropriate, and avoid embedding credentials directly in configuration files.

Risk: Automation examples can scale changes across many devices or policies without a true dry-run mode.

Mitigation: Use read-before-write checks, payload files that can be reviewed, firewall or ACL reorder snapshots, TUI handoff for visual confirmation, and staggered execution for device restarts, upgrades, or port cycles.

## Reference(s):

- [unifly Command Reference](artifact/references/commands.md)
- [UniFi Networking Concepts](artifact/references/concepts.md)
- [Automation Workflows](artifact/references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON/TOML configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers structured CLI output such as JSON for agent processing and configuration payloads for create/update workflows.]

## Skill Version(s):

0.8.4 (source: server release metadata; artifact frontmatter and changelog mention 0.10.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
