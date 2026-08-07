## Description: <br>
XCP-ng AIops helps agents operate an XCP-ng virtualization fleet through Xen Orchestra, including fleet health, VM, host, pool, storage, snapshot, backup, task, RCA, and governed write workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to triage and administer XCP-ng environments managed by Xen Orchestra, including health checks, RCA, snapshots, backups, storage reviews, and VM lifecycle operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform disruptive infrastructure actions through Xen Orchestra, including VM power operations and snapshot changes. <br>
Mitigation: Use a dedicated least-privilege or read-only Xen Orchestra account first, and require explicit human approval outside the tool before snapshot delete/revert or VM power operations. <br>
Risk: A shared or synced MCP configuration can expose the master password used to unlock the encrypted credential store. <br>
Mitigation: Do not place the real master password in shared or synced MCP config files; provide it only through an appropriate local secret mechanism. <br>
Risk: Local XCP-ng AIops state under ~/.xcpng-aiops can contain sensitive configuration, encrypted secrets, audit logs, and undo metadata. <br>
Mitigation: Protect ~/.xcpng-aiops with local filesystem permissions and restrict access to the operator account. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/xcpng-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/XCPng-AIops) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>
- [CLI reference](references/cli-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide MCP and CLI workflows that return structured JSON from XCP-ng and Xen Orchestra operations.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
