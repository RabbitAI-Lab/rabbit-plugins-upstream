## Description:

fabric-aiops helps agents operate and analyze controller-managed network fabrics across Cisco Meraki, Catalyst Center, Arista CloudVision, UniFi Network, and Cisco ACI, including health triage, read-only inventory, ACI tracing, and governed write workflows where supported.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network engineers and operations teams use this skill to inspect controller-managed network fabrics, rank fabric health issues, trace Cisco ACI endpoint paths, and run governed remediation commands when their controller account permits writes. It is intended for controller API workflows, not OT equipment, device-level CLI automation, hypervisors, storage appliances, or cluster orchestrators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact network changes and does not provide a built-in read-only mode or approval gate for agent-driven MCP use.

Mitigation: Prefer a read-only controller account first and treat MCP access as write-capable unless controller permissions block writes.

Risk: Controller credentials grant access to production network APIs.

Mitigation: Avoid broad admin API keys, keep FABRIC_AIOPS_MASTER_PASSWORD out of shell history and logs, and rotate or scope credentials according to the controller's own access controls.

Risk: Write operations can affect live network devices and configuration.

Mitigation: Use dry-run previews and CLI confirmation for writes, verify target identifiers before execution, and rely on controller permissions for final authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/fabric-aiops)
- [Fabric AIops repository](https://github.com/AIops-tools/Fabric-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Text or Markdown with shell commands, configuration snippets, and structured controller results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live or injected controller analysis results, risk-tiered remediation previews, audit guidance, and undo-related instructions.]

## Skill Version(s):

0.12.0 (source: server release metadata, released 2026-09-21T03:56:26Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
