## Description:

Firewall AIops helps agents inspect and operate OPNsense and pfSense firewalls across health, rules, NAT, VPN, DHCP, logs, root-cause analyses, and audited governed writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Network operators, SREs, and security engineers use this skill to observe OPNsense or pfSense firewall state, diagnose WAN, rule, traffic, VPN, DHCP, and NAT issues, and perform governed firewall changes when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact firewall writes without an enforceable read-only or approval gate.

Mitigation: Start with a read-only OPNsense or pfSense API account, grant write permissions only during an intentional change window, and keep console recovery available for high-risk operations.

Risk: The skill needs access to firewall credentials and stores local firewall state under the user's firewall-aiops directory.

Mitigation: Protect the local firewall-aiops directory, use the encrypted secret store, avoid legacy plaintext secret environment variables, and keep the master password out of logs and shared shells.

Risk: TLS verification or plaintext transport choices can weaken protection for firewall API traffic.

Mitigation: Enable TLS verification in production and use plaintext HTTP only when TLS is terminated by a trusted proxy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/firewall-aiops)
- [Project homepage](https://github.com/AIops-tools/Firewall-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include firewall observations, RCA findings, dry-run previews, audit-oriented guidance, and rollback steps.]

## Skill Version(s):

0.12.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
