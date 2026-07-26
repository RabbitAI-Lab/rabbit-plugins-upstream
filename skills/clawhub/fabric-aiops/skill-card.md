## Description: <br>
Fabric Aiops helps agents inspect and operate controller-managed network fabrics across Cisco Meraki, Cisco Catalyst Center, Arista CloudVision Portal, and UniFi Network, including health analysis, inventory reads, guarded remediation commands, audit logs, and undo support where available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Network operators, SREs, and infrastructure engineers use this skill to query controller-managed fabrics, triage WAN and fleet health, inspect inventory and clients, and run explicitly governed remediation actions when they have appropriate controller permissions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make live production network changes through controller APIs using persisted credentials. <br>
Mitigation: Use read-only or tightly scoped controller accounts by default, require external approval for write-capable use, and test against non-production controllers before enabling live remediation. <br>
Risk: There is no built-in read-only mode or approval gate inside the skill itself. <br>
Mitigation: Enforce authorization through the connected controller account and the supervising agent workflow; use dry-run previews and double confirmation for state-changing CLI commands. <br>
Risk: Non-interactive use can expose the master password through environment handling if configured carelessly. <br>
Mitigation: Avoid non-interactive master-password exposure unless necessary, keep runtime environments tightly scoped, and rely on the encrypted secret store rather than plaintext fallback credentials. <br>
Risk: The artifact states that controller API paths are mock-tested and have not yet been exercised against live controllers. <br>
Mitigation: Run fabric-aiops doctor and validate workflows in a lab or non-production controller before relying on the skill for production operations. <br>


## Reference(s): <br>
- [Fabric-AIops GitHub repository](https://github.com/AIops-tools/Fabric-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, controller query results, JSON-like tool outputs, and remediation previews] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include live controller observations, ranked health analyses, dry-run remediation previews, audit references, and undo guidance.] <br>

## Skill Version(s): <br>
0.7.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
