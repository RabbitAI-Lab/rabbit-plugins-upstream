## Description:

Operates OPNsense and pfSense firewalls by reporting status, analyzing rules and traffic, and carrying out approved configuration changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network administrators and engineers use it to inspect OPNsense or pfSense health, rules, NAT, VPN, DHCP, and traffic, investigate common firewall issues, and perform approved changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Firewall changes can disrupt access, and safety checks may proceed when they cannot establish that a change is safe.

Mitigation: Start with a read-only account; require approval for the exact target and change, preview writes, and retain console access.

Risk: Unverified HTTPS certificates can weaken protection for firewall API credentials.

Mitigation: Explicitly enable HTTPS certificate verification for firewall connections.

## Reference(s):

- [Firewall AIops capabilities](artifact/references/capabilities.md)
- [Setup and security guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/firewall-aiops)
- [Project homepage](https://github.com/AIops-tools/Firewall-AIops)

## Skill Output:

**Output Type(s):** [Analysis, Text, API Calls, Shell commands, Configuration guidance]

**Output Format:** [Structured firewall status and diagnostic results with concise natural-language summaries; Markdown guidance and shell commands when relevant.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report findings and proposed or completed firewall operations; write actions should receive explicit approval for the exact target and change.]

## Skill Version(s):

0.16.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
