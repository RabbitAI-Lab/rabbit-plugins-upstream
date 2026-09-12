## Description:

Firewall AIops helps agents operate OPNsense and pfSense firewalls, including health checks, rules, NAT, VPN, DHCP, log and state-table diagnostics, RCA workflows, and governed writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and security administrators use this skill to inspect and manage OPNsense or pfSense firewalls, troubleshoot connectivity and blocked traffic, audit rules, and perform selected firewall changes with audit and dry-run support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact firewall writes and does not enforce a built-in approval gate or read-only mode.

Mitigation: Use a dedicated least-privilege firewall API account, prefer read-only access by default, and review every write or commit operation before allowing it.

Risk: Firewall API credentials and the local firewall-aiops state are sensitive.

Mitigation: Treat ~/.firewall-aiops as sensitive, avoid broad export of FIREWALL_AIOPS_MASTER_PASSWORD, and use the encrypted secret store rather than legacy plaintext secret variables.

Risk: Weak transport settings can expose firewall management traffic or credentials.

Mitigation: Use HTTPS with certificate verification in production, and avoid plain HTTP or verify_ssl:false except in isolated lab environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/firewall-aiops)
- [Firewall AIops homepage](https://github.com/AIops-tools/Firewall-AIops)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [setup-guide.md](references/setup-guide.md)
- [agent-guardrails.md](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured firewall-operation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed firewall tool calls, command snippets, RCA summaries, dry-run recommendations, and change-validation steps.]

## Skill Version(s):

0.12.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
