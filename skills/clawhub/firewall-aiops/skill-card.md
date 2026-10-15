## Description:

Helps agents inspect, troubleshoot, and administer OPNsense and pfSense firewalls through diagnostics and governed operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators and engineers use this skill to diagnose gateway health, firewall rules, blocked traffic, NAT, VPN, and DHCP on OPNsense or pfSense, and to make supervised firewall changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated write and reboot operations can change or interrupt firewall service without an enforced approval gate.

Mitigation: Begin with a read-only firewall API account; use write access only during supervised maintenance and require explicit human approval before MCP writes.

Risk: Insecure TLS settings could expose production firewall management traffic.

Mitigation: Confirm TLS certificate verification is enabled for production targets.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/firewall-aiops)
- [Project homepage (declared in ClawHub metadata)](https://github.com/AIops-tools/Firewall-AIops)
- [Capabilities and supported operations](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Setup and security guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance and command examples; structured firewall tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostics and change previews are available; writes can change live firewall behavior.]

## Skill Version(s):

0.14.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
