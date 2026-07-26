## Description: <br>
Fix Plan helps agents maintain fix_plan.md and checklist.md trackers, including item schema, priority triage, deferred plan stubs, GitHub state sync, completed-item archiving, and issue draft lifecycle cleanup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering agents use this skill to keep project tracker files compact, structured, and synchronized with GitHub issue and pull request state. It is intended for task-list housekeeping, deferred plan capture, completed-work archiving, and issue draft cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cleanup flows can rewrite fix_plan.md or checklist.md and archive or delete tracker entries. <br>
Mitigation: Use explicit tracker paths, run cleanup with --dry-run first, and review the backup and resulting diff before accepting archive or delete flows. <br>
Risk: Archive and RAG receiver flows can store detailed work history, operational metadata, or sensitive tracker content outside the active file. <br>
Mitigation: Enable only trusted --archive or --rag receivers, and redact secrets, private logs, and sensitive incident details before dispatch. <br>
Risk: GitHub sync can change tracker item state based on gh CLI results. <br>
Mitigation: Run sync against the intended repository with an authenticated gh session and review the sync report before committing tracker updates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix-plan) <br>
- [Skill overview](artifact/SKILL.md) <br>
- [Format guide](artifact/format.md) <br>
- [Priority guide](artifact/priority.md) <br>
- [Move and archive guide](artifact/move.md) <br>
- [GitHub sync guide](artifact/sync.md) <br>
- [Issue drafts lifecycle](artifact/issue-drafts.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance, configuration] <br>
**Output Format:** [Markdown guidance with tracker edits and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local tracker files and archive completed or draft entries when invoked with the documented cleanup flows.] <br>

## Skill Version(s): <br>
0.3.3 (source: server release metadata and CHANGELOG.md, released 2026-07-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
