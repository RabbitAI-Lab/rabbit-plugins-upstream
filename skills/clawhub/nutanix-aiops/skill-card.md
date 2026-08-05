## Description: <br>
Nutanix AIops enables agents to inspect and operate Nutanix Prism Central v4 estates across clusters, VMs, storage, networking, data protection, alerts, LCM, capacity, diagnostics, and RCA with governed CLI and MCP workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Infrastructure operators, SREs, and developers use this skill to diagnose Nutanix estates, triage alerts, forecast capacity, and perform governed VM, storage, network, DR, and lifecycle operations through Prism Central v4. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose destructive Nutanix Prism Central operations without a built-in approval or read-only control. <br>
Mitigation: Start with a dedicated read-only Prism Central account and enable write-capable credentials only for controlled maintenance workflows with clear human approval outside the skill. <br>
Risk: The skill stores sensitive local state under ~/.nutanix-aiops/. <br>
Mitigation: Protect ~/.nutanix-aiops/, prefer the encrypted credential store, and avoid long-lived environment-variable secrets where possible. <br>
Risk: High-impact infrastructure changes can affect VMs, storage, networking, data protection, and lifecycle management. <br>
Mitigation: Use dry-run previews where supported, confirm the exact target resource, and keep write permissions scoped to the operator's intended maintenance window. <br>


## Reference(s): <br>
- [Nutanix AIops GitHub repository](https://github.com/AIops-tools/Nutanix-AIops) <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/nutanix-aiops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and structured MCP tool output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May operate Nutanix Prism Central through local CLI or MCP tools; destructive workflows should be previewed with dry-run and separately authorized by the operator.] <br>

## Skill Version(s): <br>
0.9.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
