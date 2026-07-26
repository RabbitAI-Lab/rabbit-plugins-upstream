## Description: <br>
Smart Memory helps agents maintain local long-term memory by recalling relevant cues before work, recording reusable knowledge afterward, and managing retention with deduplication, decay, signals, and garbage collection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bbpfish](https://clawhub.ai/user/bbpfish) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use Smart Memory to give coding or productivity agents persistent local recall across sessions, store reusable knowledge cards, and maintain the memory store with validation, migration, and cleanup commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist conversation-derived data and environment details in a local long-term memory store. <br>
Mitigation: Review stored memory data before use, avoid sensitive inputs unless retention is intended, and treat env-snapshot as optional diagnostic data. <br>
Risk: Scheduled or auto-confirm maintenance can mutate the memory store without step-by-step review. <br>
Mitigation: Start with dry runs or manual confirmation, and enable schedules only after privacy, retention, backup, and confirmation behavior are clear. <br>
Risk: Reproducibility can vary if runtime dependencies are not pinned. <br>
Mitigation: Pin dependencies when reproducible installs matter and review requirements before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/bbpfish/skills/smart-memory) <br>
- [README](README.md) <br>
- [Smart Memory v3 Reference](references/README.md) <br>
- [General Best Practices Review](references/review_gbp.md) <br>
- [AgentSkills Open Standard](https://github.com/anthropics/agent-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and text or JSON output from local Python scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally, stores memory data in SQLite or JSON files, and may persist conversation-derived memory and environment snapshots.] <br>

## Skill Version(s): <br>
2.2.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
