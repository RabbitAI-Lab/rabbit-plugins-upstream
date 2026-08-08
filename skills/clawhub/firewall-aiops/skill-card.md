## Description: <br>
Firewall AIops helps agents inspect, troubleshoot, and operate OPNsense and pfSense firewalls, including health, rules, NAT, VPN, DHCP, logs, RCA workflows, and governed change operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, firewall administrators, and operations teams use this skill to inspect OPNsense or pfSense state, diagnose connectivity and rule behavior, and perform audited firewall changes during controlled operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-accessible firewall write tools can disrupt connectivity or change security posture. <br>
Mitigation: Use a read-only OPNsense or pfSense API account by default and grant write permissions only during controlled change windows. <br>
Risk: High-impact operations such as apply_changes, reconfigure, reboot, service restart, state killing, and alias or rule edits can affect live traffic. <br>
Mitigation: Treat these tools as change-window actions, review dry-run output where available, and verify rollback or recovery access before committing changes. <br>
Risk: Firewall credentials and the master password protect privileged access to network infrastructure. <br>
Mitigation: Protect ~/.firewall-aiops, FIREWALL_AIOPS_MASTER_PASSWORD, and the encrypted secrets file according to administrator credential-handling practices. <br>


## Reference(s): <br>
- [Capabilities Reference](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Setup and Security Guide](references/setup-guide.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>
- [Project Homepage](https://github.com/AIops-tools/Firewall-AIops) <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/firewall-aiops) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline commands and structured tool-result guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include firewall observations, RCA findings, dry-run previews, audit-oriented change guidance, and rollback instructions.] <br>

## Skill Version(s): <br>
0.8.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
