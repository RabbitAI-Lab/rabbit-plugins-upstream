## Description: <br>
Proactive Tasks helps AI agents manage goals, break projects into tracked tasks, and make autonomous progress during heartbeat cycles while reporting meaningful updates or blockers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[imrkhn03](https://clawhub.ai/user/imrkhn03) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to create goals, decompose work into prioritized tasks, track progress, time, dependencies, and blockers, and let agents continue approved work during heartbeat cycles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recurring autonomous task work can continue without tight consent or project scope controls. <br>
Mitigation: Enable heartbeat or cron behavior only for named approved projects and require human approval before external, irreversible, or sensitive actions. <br>
Risk: Task notes and shared workspace state files may contain sensitive business details or secrets. <br>
Mitigation: Avoid putting secrets or sensitive details in task notes, SESSION-STATE.md, working-buffer, WAL, or memory files, and periodically review or clear those files. <br>
Risk: Persistent local state can make outdated goals or stale assumptions influence future autonomous work. <br>
Mitigation: Review active goals, blockers, SESSION-STATE.md, and memory files before enabling autonomous operation and after long pauses or context recovery. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/imrkhn03/skills/proactive-tasks) <br>
- [README](artifact/README.md) <br>
- [Heartbeat Configuration](artifact/HEARTBEAT-CONFIG.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON, markdown] <br>
**Output Format:** [Markdown guidance with bash commands and JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write local task data, session-state, working-buffer, WAL, and memory files when its CLI commands run.] <br>

## Skill Version(s): <br>
1.2.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
