## Description:

Fabric AIops lets agents inspect, diagnose, and perform governed remediation on controller-managed network fabrics across Cisco Meraki, Cisco Catalyst Center, Arista CloudVision Portal, and UniFi Network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators, SREs, and infrastructure engineers use this skill to query controller-managed fabrics, diagnose WAN and network health issues, inspect inventory and clients, and perform guarded remediation such as device restart, VLAN update, device claim or removal, and template binding. It is intended for controller API workflows, not OT equipment, hypervisors, storage, cluster orchestration, or direct device CLI automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make production network changes through controller APIs and has no built-in approval or read-only gate.

Mitigation: Use read-only or narrowly scoped controller credentials for normal sessions and require human approval outside the tool before restarts, removals, VLAN changes, or template binding.

Risk: The external fabric-aiops package is installed and invoked as a runtime dependency.

Mitigation: Install only from a pinned and verified release after reviewing package provenance and release integrity.

Risk: Controller secrets and the FABRIC_AIOPS_MASTER_PASSWORD can grant access to live infrastructure.

Mitigation: Keep write-capable credentials out of routine agent sessions, avoid exposing FABRIC_AIOPS_MASTER_PASSWORD except in controlled environments, and rotate credentials if exposure is suspected.

Risk: The artifact states the test suite is mock-based and no supported platform has yet been exercised against a live controller.

Mitigation: Run fabric-aiops doctor and validate workflows in a non-production or read-only environment before relying on live-controller results.

## Reference(s):

- [Fabric-AIops GitHub repository](https://github.com/AIops-tools/Fabric-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/fabric-aiops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Analysis]

**Output Format:** [Markdown with inline shell commands and structured controller-operation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk-tiered remediation guidance, dry-run suggestions, audit and undo considerations, and controller output summaries.]

## Skill Version(s):

0.11.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
