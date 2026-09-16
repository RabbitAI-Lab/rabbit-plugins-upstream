## Description:

Firewall AIops helps agents operate OPNsense and pfSense firewalls across health checks, rules, NAT, VPN, DHCP, diagnostics, root-cause analysis workflows, and governed write operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators, security engineers, and developers use this skill to inspect and operate OPNsense or pfSense firewalls, including troubleshooting WAN health, auditing rules, reviewing blocked traffic, inspecting NAT/VPN/DHCP state, and applying controlled firewall changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact firewall writes can change live network access or reboot devices.

Mitigation: Use a dedicated read-only firewall API account by default and grant write-capable credentials only when an external operator approval process is in place.

Risk: Write-capable operations rely on agent judgment or connected-account permissions rather than a built-in approval gate.

Mitigation: Require approval outside the tool, use dry-run previews where supported, set audit annotations for change windows, and review the local audit trail.

Risk: Secrets or management traffic can be exposed through unsafe handling or relaxed TLS settings.

Mitigation: Use the encrypted secret store, avoid passing secrets with --value, keep TLS verification enabled in production, and do not place secrets in prompts or logs.

Risk: Unpinned package installation can introduce behavior changes after review.

Mitigation: Pin or verify the firewall-aiops package version before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/firewall-aiops)
- [Project homepage](https://github.com/AIops-tools/Firewall-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or structured tool-result summaries with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live firewall readouts, risk labels, dry-run guidance, audit references, and truncation indicators from tool results.]

## Skill Version(s):

0.12.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
