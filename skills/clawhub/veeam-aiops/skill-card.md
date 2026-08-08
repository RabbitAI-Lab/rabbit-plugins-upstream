## Description: <br>
veeam-aiops helps agents operate Veeam Backup & Replication for health overview, diagnostics, backup job control, restore workflows, repository and infrastructure inventory, and async session monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators, backup administrators, and developers use this skill to inspect Veeam Backup & Replication environments, triage failed jobs or low repository capacity, run or stop backup jobs, start restore workflows, and follow async sessions through CLI or MCP workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact Veeam write tools can change backup operations immediately without an internal MCP approval gate. <br>
Mitigation: Install with a dedicated least-privilege Veeam account, preferably read-only at first, and require explicit human confirmation before job stops, job disables, session stops, undo_apply, or VM restore actions. <br>
Risk: VM restore and session stop actions may be irreversible or have no undo token. <br>
Mitigation: Use dry-run previews, verify the resolved VM name and target outside the opaque identifier, and approve restores only after confirming the intended machine and maintenance context. <br>
Risk: Async jobs and restores can be reissued accidentally if an agent confuses job, session, backup, or restore-point identifiers. <br>
Mitigation: Start the operation once, then poll session tools for progress; chain list and detail tools to obtain fresh identifiers before write operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/veeam-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/Veeam-AIops) <br>
- [Capabilities](references/capabilities.md) <br>
- [Setup guide](references/setup-guide.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls] <br>
**Output Format:** [Markdown with inline shell commands and structured JSON tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include audited CLI or MCP operations against configured Veeam Backup & Replication targets.] <br>

## Skill Version(s): <br>
0.10.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
