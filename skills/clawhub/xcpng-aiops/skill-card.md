## Description: <br>
Xcpng Aiops helps agents operate XCP-ng virtualization fleets through Xen Orchestra with fleet health summaries, infrastructure inventory, RCA workflows, and governed VM, storage, and snapshot actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and infrastructure teams use this skill to inspect and troubleshoot XCP-ng fleets managed by Xen Orchestra, including VM health, pool posture, storage pressure, snapshots, backups, and XO tasks. It can also propose and execute governed operational writes such as VM start, stop, reboot, migration, snapshot operations, and SR rescans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact writes against XCP-ng infrastructure through the connected Xen Orchestra account. <br>
Mitigation: Use a dedicated least-privileged or read-only Xen Orchestra user for triage, require dry-run previews, and obtain explicit human approval before destructive or disruptive actions. <br>
Risk: Snapshot delete and revert operations are irreversible, and VM stop, reboot, or migration can disrupt running workloads. <br>
Mitigation: Review the target UUIDs and current state before write tools run, prefer dry-run first, and confirm rollback options where the operation supports undo. <br>
Risk: Stored Xen Orchestra credentials and master passwords can expose infrastructure control if shared or committed. <br>
Mitigation: Keep the master password out of shared MCP configuration and source control, use the encrypted secret store, and rotate or revoke XO tokens when access changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/xcpng-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/XCPng-AIops) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured JSON tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include triage findings, RCA explanations, dry-run previews, audit context, and configuration steps for the xcpng-aiops CLI or MCP server.] <br>

## Skill Version(s): <br>
0.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
