## Description: <br>
Manages VMware NSX networking resources, including segments, Tier-0 and Tier-1 gateways, NAT rules, routing, IP pools, health checks, and connectivity troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to inspect, configure, and troubleshoot VMware NSX networking across segments, gateways, NAT, static routes, IP pools, fabric inventory, and health endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can directly change live VMware NSX network infrastructure, and MCP write tools execute without the CLI double-confirmation safeguards. <br>
Mitigation: Use least-privilege NSX service accounts, approve the exact operation and target before MCP writes, and prefer CLI dry-run plus confirmation for changes. <br>
Risk: Local NSX credentials and generated MCP configuration can expose access to network infrastructure if mishandled. <br>
Mitigation: Review MCP configuration before applying it, keep ~/.vmware-nsx/.env locked down, and use a secret manager for production credentials where possible. <br>


## Reference(s): <br>
- [VMware NSX GitHub repository](https://github.com/zw008/VMware-NSX) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Setup Guide](references/setup-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline shell commands and structured tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run recommendations, target selection, and MCP tool-use guidance for NSX operations.] <br>

## Skill Version(s): <br>
1.8.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
