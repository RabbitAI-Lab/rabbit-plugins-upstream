## Description: <br>
Firewall Aiops helps agents inspect and operate OPNsense and pfSense firewalls, including health checks, rules, NAT, aliases, VPN, DHCP, firewall logs, RCA workflows, and governed write operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to query OPNsense or pfSense firewall state, investigate gateway, rule, and blocked-traffic issues, and perform audited firewall changes during planned operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact firewall writes, apply operations, reconfiguration, and reboot can run when the connected API account has permission, and the skill does not provide an in-tool approval or read-only gate. <br>
Mitigation: Use a read-only OPNsense or pfSense API account by default, grant write scope only during planned change windows, and require explicit operator confirmation before write, apply, reconfigure, or reboot actions. <br>
Risk: Firewall credentials and local configuration can expose administrative access if stored or handled incorrectly. <br>
Mitigation: Keep ~/.firewall-aiops protected, use the encrypted secrets store, avoid the legacy plaintext secret environment variable, and rotate or migrate secrets when needed. <br>
Risk: Production firewall access can be weakened by insecure transport settings or unverified API behavior. <br>
Mitigation: Enable SSL verification for production targets and validate connectivity and platform behavior with firewall-aiops doctor before relying on operational results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/firewall-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/Firewall-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured tool guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include firewall observations, RCA findings, dry-run previews, audit-oriented change guidance, and rollback guidance.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
