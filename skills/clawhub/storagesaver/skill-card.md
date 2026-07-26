## Description: <br>
StorageSaver helps agents explain Mac disk usage, generate visual storage reports, and provide read-only cleanup guidance with scheduled storage alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nelsonscott](https://clawhub.ai/user/nelsonscott) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Mac users and their agents use StorageSaver to inspect disk pressure, identify large storage categories, and receive prioritized cleanup recommendations. The scheduled watcher supports recurring alerts while leaving any cleanup command execution to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Storage scans and exported reports may reveal private file paths and local storage details. <br>
Mitigation: Keep generated reports local unless intentionally sharing them, and review report contents before emailing or uploading them. <br>
Risk: The optional NOTIFY_CMD setting runs a user-provided shell command and can send reports to external channels. <br>
Mitigation: Set NOTIFY_CMD only to commands the user would run directly, and avoid notification commands that expose reports unintentionally. <br>
Risk: Cleanup recommendations can include destructive shell commands for the user to copy and run. <br>
Mitigation: Treat commands as proposals, review them with the user, and do not execute cleanup actions unless the user explicitly asks. <br>


## Reference(s): <br>
- [StorageSaver on ClawHub](https://clawhub.ai/nelsonscott/skills/storagesaver) <br>
- [nelsonscott publisher profile](https://clawhub.ai/user/nelsonscott) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; the watcher can emit text alerts plus HTML and JSON report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only by design; scheduled state, logs, JSON reports, and HTML reports are stored under ~/.config/storagesaver.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
