## Description: <br>
This skill helps agents operate a unified local Web dashboard for task queues, system metrics, network status, log filtering, and CLI status checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and individual users use this skill to launch a local dashboard, inspect CPU, memory, load, task queues, and network state, filter logs, and run quick CLI status checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can involve local command execution and dashboard service startup. <br>
Mitigation: Review commands before execution and use it only where starting local services and running CLI tools is acceptable. <br>
Risk: The skill can inspect logs, system state, and potentially sensitive local data. <br>
Mitigation: Avoid providing sensitive logs, credentials, or private configuration unless the data flow is understood. <br>
Risk: The skill describes queue-clearing operations and callback or API request behavior without clear confirmation steps. <br>
Mitigation: Ask for explicit user confirmation before clearing queues or sending callbacks and API requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/glitch-dashboard-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local dashboard commands, configuration snippets, and structured status or log output.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
