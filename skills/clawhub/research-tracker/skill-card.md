## Description: <br>
Manage autonomous AI research agents with SQLite-based state tracking for long-running investigations, handoffs, progress monitoring, and operator oversight. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[julian1645](https://clawhub.ai/user/julian1645) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to coordinate long-running autonomous research projects, record progress, pass instructions to active agents, and monitor heartbeats or stop signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on an external CLI distributed through a Homebrew tap or Go repository. <br>
Mitigation: Install only when the publisher and external source are trusted, and prefer reviewing or pinning a release before use in sensitive environments. <br>
Risk: Research activity is retained on disk in a local SQLite database. <br>
Mitigation: Avoid logging secrets or sensitive research content unless local retention is acceptable for the project. <br>
Risk: Long-running research agents can drift, stall, or continue after operator priorities change. <br>
Mitigation: Monitor heartbeats, attention flags, pending instructions, audits, and stop signals during active research. <br>


## Reference(s): <br>
- [Research Tracker on ClawHub](https://clawhub.ai/julian1645/skills/research-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and command reference tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides use of an external CLI that writes local SQLite state.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
