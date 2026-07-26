## Description: <br>
Task management based on Eisenhower Matrix + P0-P2 priority with Customer Project Management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yayayahei](https://clawhub.ai/user/yayayahei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users use this skill to manage personal and customer project work in markdown task files. It supports Eisenhower quadrants, P0-P2 prioritization, customer project tracking, delegation, maybe-list triage, archiving, and an optional local dashboard. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dashboard includes a browser-accessible shell that can execute host commands if exposed to an untrusted user or network. <br>
Mitigation: Run the dashboard only on trusted local machines and keep it bound to localhost; remove the terminal or add strong authentication before any shared or remote deployment. <br>
Risk: Dashboard actions can edit local markdown task files. <br>
Mitigation: Keep task files in version control or backups and review changes after dashboard-based moves, completions, deletions, or copies. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yayayahei/skills/eisenhower-task-manager) <br>
- [README](README.md) <br>
- [Dashboard README](dashboard/README.md) <br>
- [Task Addition Flow](references/task-add.md) <br>
- [Task Completion Flow](references/task-complete.md) <br>
- [Task Numbering Rules](references/numbering-rules.md) <br>
- [Maybe List Operations](references/maybe-list-workflow.md) <br>
- [Dashboard Offer Workflow](references/dashboard-offer.md) <br>
- [Output Format Examples](references/output-examples.md) <br>
- [Statistics Templates](references/templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and local markdown task-file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The optional dashboard can update local task markdown files and expose task state through a browser interface.] <br>

## Skill Version(s): <br>
8.3.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
