## Description: <br>
Manages VMware NSX security workflows for distributed firewall policies and rules, security groups, VM tagging, Traceflow diagnostics, and IDS/IPS status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Network security engineers and infrastructure operators use this skill to inspect and manage NSX Distributed Firewall policies, security groups, VM tags, traceflows, and IDS/IPS posture during microsegmentation work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DFW, group, tag, and Traceflow actions can affect production NSX security posture. <br>
Mitigation: Install only where the operator is allowed to administer NSX security, use least-privilege or read-only NSX service accounts when possible, and require explicit human approval for production changes. <br>
Risk: Credentials may be exposed through local configuration or environment files. <br>
Mitigation: Prefer a secret manager over storing passwords in .env files and restrict permissions on local NSX configuration files. <br>
Risk: Incorrect firewall or security group changes can disrupt connectivity or leave assets unprotected. <br>
Mitigation: Review proposed actions before execution, use dry-run paths where available, verify group membership, and validate behavior with Traceflow before enabling deny rules. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-nsx-security) <br>
- [Project Homepage](https://github.com/vmware-skills/VMware-NSX-Security) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Capabilities Reference](references/capabilities.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured MCP tool arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include NSX object identifiers, status summaries, audit-aware action plans, and dry-run instructions.] <br>

## Skill Version(s): <br>
1.8.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
