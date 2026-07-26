## Description: <br>
Governed Veeam Backup & Replication operations for health overview, diagnostics, job control, restore workflows, repository capacity checks, infrastructure inventory, async session tracking, and undo-aware audited actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, backup operators, and infrastructure teams use this skill to inspect and operate Veeam Backup & Replication environments through CLI or MCP workflows with audit logging, dry-run previews, and undo records for reversible writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact backup and restore writes, including stopping jobs or sessions and starting irreversible VM restores. <br>
Mitigation: Use a dedicated least-privilege Veeam account, begin with read-only permissions where possible, and require an operational approval process before enabling write-capable credentials. <br>
Risk: Master passwords or Veeam credentials could be exposed if placed in committed MCP configuration, shell history, CI logs, or persistent plaintext environment files. <br>
Mitigation: Inject secrets through a secret manager or ephemeral environment, keep the encrypted store outside version control, and avoid committing MCP configs that contain `VEEAM_AIOPS_MASTER_PASSWORD`. <br>
Risk: The skill relies on account permissions and agent discipline rather than a built-in approval gate for MCP write tools. <br>
Mitigation: Configure the Veeam account with only the permissions each workflow needs and instruct the agent to avoid write tools unless an operator has explicitly approved the action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/veeam-aiops) <br>
- [Veeam-AIops homepage](https://github.com/AIops-tools/Veeam-AIops) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with inline shell commands and structured MCP tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI and MCP workflows may return Veeam environment data, audit status, dry-run previews, undo identifiers, and risk-tier labels.] <br>

## Skill Version(s): <br>
0.8.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
