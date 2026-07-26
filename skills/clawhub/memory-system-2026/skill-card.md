## Description: <br>
Maintains a four-layer memory and knowledge-distillation workflow from WAL entries to MEMORY.md, daily logs, and Obsidian synchronization, including Insight Miner analysis and backlink discovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adchina2025](https://clawhub.ai/user/adchina2025) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and personal knowledge-management users use this skill to maintain persistent agent memory, daily logs, task context, financial summaries, and Obsidian archives across a workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Long-lived memory may persist personal, financial, preference, decision, task, and system-change data across local files and an Obsidian vault. <br>
Mitigation: Use only with intended workspaces and vaults, and define explicit recording, review, redaction, deletion, and sync rules before installation. <br>
Risk: Financial summaries and broad workspace memory can expose sensitive context if reviewed or synced outside the intended location. <br>
Mitigation: Limit configured paths and review generated memory, task, and financial summaries before syncing or archiving them. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file paths, schedules, and shell command references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses workspace-specific placeholders for memory, accounting, vault, sync, and script paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
