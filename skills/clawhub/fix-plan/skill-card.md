## Description: <br>
Manages fix_plan.md and checklist.md trackers by formatting schema, triaging blockers, syncing external issue state, moving completed work, and maintaining related planning topics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and project maintainers use this skill to keep Markdown work trackers consistent, prioritized, synchronized with external issue state, and trimmed as completed work moves into summaries or archives. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Qdrant lookup and ingest helpers can process plan or research Markdown through configured external tooling. <br>
Mitigation: Do not invoke artifact_pre_lookup.py or artifact_post_ingest.py unless you intend that behavior, trust the configured Qdrant setup, and trust the qdrant-import.py helper in the home skill directory. <br>
Risk: Tracker lifecycle actions can move completed entries, append extracted checklist items, or otherwise modify fix_plan.md or checklist.md. <br>
Mitigation: Use explicit /fix-plan commands, keep backups for completed-item moves, and review tracker diffs before relying on the updated plan. <br>
Risk: Optional RAG dispatch can store full plan or research bodies outside the tracker. <br>
Mitigation: Supply --rag only when the destination skill and storage location are known and acceptable for the content being indexed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix-plan) <br>
- [Format guide](format.md) <br>
- [Priority guide](priority.md) <br>
- [Sync guide](sync.md) <br>
- [Sync automation guide](sync-automation.md) <br>
- [Move guide](move.md) <br>
- [Completion criteria guide](completion-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional code, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May edit tracker files or emit commands when invoked by an agent with the required tools.] <br>

## Skill Version(s): <br>
0.5.0 (source: release evidence and changelog, released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
