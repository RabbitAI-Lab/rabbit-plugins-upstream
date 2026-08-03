## Description: <br>
fabric-aiops helps agents operate controller-managed network fabrics across Cisco Meraki, Cisco Catalyst Center, Arista CloudVision Portal, and UniFi Network with health analysis, inventory reads, guarded remediation commands, audit logging, and undo support where available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Network operations engineers and agent developers use this skill to inspect controller-managed network fabrics, diagnose WAN or fleet-health issues, and run guarded remediation workflows with audit records and dry-run support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make live network-controller changes without an in-tool approval gate. <br>
Mitigation: Use least-privilege or read-only controller credentials until remediation is intentionally needed, require an external human approval process, and run dry-run previews before write operations. <br>
Risk: Controller credentials can grant broad access to production network infrastructure. <br>
Mitigation: Store credentials through the documented encrypted secret store, avoid exporting the master password except in controlled automation, and rotate or scope controller accounts appropriately. <br>
Risk: Artifact documentation says controller API behavior is mock-tested and not yet exercised against live controllers. <br>
Mitigation: Validate workflows in a lab or limited-scope environment before relying on the skill for production remediation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/fabric-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/Fabric-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, analysis] <br>
**Output Format:** [Markdown, inline shell commands, and structured tool/API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May issue live controller reads or writes when configured with credentials; write operations should be previewed with dry-run and reviewed by the operator.] <br>

## Skill Version(s): <br>
0.9.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
