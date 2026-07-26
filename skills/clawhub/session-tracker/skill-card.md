## Description: <br>
session-tracker helps agents checkpoint, resume, and recover multi-step work by recording local session state, TodoWrite updates, declared file paths, and optional monitoring data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[darkd](https://clawhub.ai/user/darkd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to preserve progress across session drops, recover interrupted multi-step tasks, and inspect local recovery state before continuing work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent recovery state can retain task names, step descriptions, declared file paths, and worklog entries until removed. <br>
Mitigation: Use --auto-cleanup for tasks that should leave no state after success, run cleanup when recovery data is no longer needed, and use prune to remove older sessions. <br>
Risk: scan, status, and monitor can expose filesystem metadata about download, upload, .session, and skills directories. <br>
Mitigation: Keep filesystem scanning off for sensitive projects unless that metadata is acceptable, and use the default minimal init workflow when crash recovery alone is sufficient. <br>
Risk: The optional background monitor creates a local process and monitor log while it is running. <br>
Mitigation: Start the monitor only when stuck detection is needed, prefer foreground mode when a detached process is undesirable, and stop or clean up the monitor after use. <br>
Risk: cleanup irreversibly removes local recovery state. <br>
Mitigation: Review whether recovery data is still needed before cleanup; the command requires --force or interactive confirmation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/darkd/skills/session-tracker) <br>
- [Security audit](https://clawhub.ai/darkd/skills/session-tracker/security-audit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; runtime commands emit plain text and JSON-backed local session files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local recovery state under .session/ and can remove it with cleanup, auto-cleanup, or prune.] <br>

## Skill Version(s): <br>
2.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
