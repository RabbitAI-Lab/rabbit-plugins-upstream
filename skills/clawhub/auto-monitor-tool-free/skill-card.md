## Description: <br>
A lightweight system monitoring skill for personal developers that helps agents inspect CPU, memory, disk, network, process, and basic alert status for single-machine environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use this skill to check local server health, review recent resource usage, configure simple threshold alerts, and collect lightweight history for personal or development environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to run local monitoring commands and long-running watch operations on the machine. <br>
Mitigation: Review commands before execution and install the skill only where local system monitoring by an agent is intended. <br>
Risk: Optional email alerts may require SMTP credentials. <br>
Mitigation: Store credentials in environment variables or a secret manager and prefer app-specific or least-privilege email credentials. <br>
Risk: Local monitoring history can accumulate on disk over time. <br>
Mitigation: Set retention limits and periodically clean local history data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/auto-monitor-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local status summaries, alert configuration guidance, and command examples for Python-based monitoring workflows.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
