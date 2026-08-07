## Description: <br>
Use this skill to manage VMware NSX networking, including segments, Tier-0 and Tier-1 gateways, NAT, routing, IP pools, and network health checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and network engineers use this skill to inspect and operate VMware NSX environments through CLI or MCP workflows. It supports segment, gateway, NAT, routing, IP pool, health, and troubleshooting tasks while directing firewall, VM lifecycle, storage, and load-balancing work to companion skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security verdict is suspicious because the skill is a high-impact NSX network management tool with security-relevant setup inconsistencies. <br>
Mitigation: Review the skill before production installation, confirm accessible Policy and Management API endpoints, and keep state-changing operations behind explicit human approval and audit review. <br>
Risk: Over-privileged NSX credentials could allow unintended changes to segments, gateways, NAT, routes, or IP pools. <br>
Mitigation: Use a least-privilege NSX account appropriate to the task, such as read-only access for monitoring and tightly scoped write access only where automation is required. <br>
Risk: Disabled or untrusted TLS verification can expose NSX Manager traffic and credentials. <br>
Mitigation: Set verify_ssl to true for production targets and configure a trusted CA bundle for NSX Manager connections. <br>
Risk: Network write operations can disrupt connectivity if applied to the wrong target or object. <br>
Mitigation: Use dry-run previews where available, confirm the target NSX Manager explicitly, check dependencies before destructive actions, and review the audit log after changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-nsx) <br>
- [VMware NSX homepage](https://github.com/vmware-skills/VMware-NSX) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown or text with inline shell commands, configuration snippets, and structured MCP results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include NSX inventory, health summaries, troubleshooting findings, and proposed or executed network operations.] <br>

## Skill Version(s): <br>
1.8.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
