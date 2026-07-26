## Description: <br>
Complete MacBook optimization suite: monitoring, troubleshooting, cleanup, and performance tuning. Works on all Macs (Intel & Apple Silicon). No extra tools required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drg3nz0](https://clawhub.ai/user/drg3nz0) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Mac users and support-oriented agents use this skill to inspect MacBook health, diagnose performance, storage, battery, thermal, memory, and network issues, and produce guided optimization or cleanup recommendations. The skill can also propose macOS shell commands and GUI-first workflows for Activity Monitor, System Settings, Finder, and local visual reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad cleanup and settings changes could delete files, alter startup behavior, stop processes, or change power settings in ways the user did not intend. <br>
Mitigation: Start with read-only checks, require a preview before any deletion or setting change, and approve cleanup, login item, service, cron, process, and power-setting changes one at a time. <br>
Risk: Granting broad macOS permissions can expand what an agent is able to inspect or change on the device. <br>
Mitigation: Avoid Full Disk Access or Accessibility permissions unless a specific approved task requires them. <br>
Risk: Optional persistent monitoring can create continuing background behavior on the Mac. <br>
Mitigation: Enable monitoring only when needed and review any proposed cron or background-service configuration before installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drg3nz0/skills/macbook-optimizer) <br>
- [Publisher profile](https://clawhub.ai/user/drg3nz0) <br>
- [Homepage declared in skill metadata](https://github.com/T4btc/macbook-optimizer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, GUI navigation steps, recommendations, and optional local report descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include proposed cleanup, login item, service, cron, process, and power-setting changes that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
