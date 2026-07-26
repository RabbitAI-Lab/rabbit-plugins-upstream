## Description: <br>
Track time, manage projects and tasks using timesheet.io CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[florianrauscha](https://clawhub.ai/user/florianrauscha) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to control Timesheet time tracking from an agent, including authentication checks, timers, projects, tasks, tags, reports, exports, profile settings, and CLI configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to create, update, delete, export, or configure Timesheet account data through the CLI. <br>
Mitigation: Require explicit user confirmation before destructive or account-changing commands and review command targets before execution. <br>
Risk: Timesheet API keys or account data could be exposed in chat, logs, or command output. <br>
Mitigation: Avoid sharing API keys in chat or logs and verify that the timesheet command on PATH is the official CLI before use. <br>


## Reference(s): <br>
- [Timesheet Homepage](https://timesheet.io) <br>
- [ClawHub Skill Page](https://clawhub.ai/florianrauscha/skills/timesheet) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON-oriented CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the timesheet CLI and recommends --json output for structured command results.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
