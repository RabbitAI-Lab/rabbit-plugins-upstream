## Description: <br>
Guides agents to handle Kimi Desktop OpenClaw gateway lifecycle issues by avoiding direct CLI or process control and advising a full desktop app restart. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support agents, and desktop automation agents use this skill when a user reports Kimi/OpenClaw gateway restart, startup, shutdown, hang, or health-check problems. It steers the agent toward user-facing restart guidance instead of terminal commands that may conflict with Kimi Desktop's supervisor. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may avoid terminal-based gateway repair commands when handling Kimi/OpenClaw gateway issues. <br>
Mitigation: Explain that Kimi Desktop owns gateway lifecycle management and guide the user to fully quit and reopen the desktop app. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands] <br>
**Output Format:** [Markdown guidance with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Lists disallowed gateway lifecycle commands and provides macOS and Windows full-quit recovery instructions; does not require code execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
