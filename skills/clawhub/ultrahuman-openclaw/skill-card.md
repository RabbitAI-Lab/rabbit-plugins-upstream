## Description: <br>
Fetch and summarize Ultrahuman Ring and CGM metrics inside OpenClaw using the Ultrahuman MCP server via mcporter. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devpranoy](https://clawhub.ai/user/devpranoy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
OpenClaw users use this skill to fetch personal Ultrahuman health metrics and generate concise daily or weekly summaries covering sleep, recovery, movement, steps, VO2 max, HRV, and resting heart rate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on local mcporter and Ultrahuman MCP tooling that can access sensitive Ultrahuman credentials and personal health metrics. <br>
Mitigation: Review or pin the external Ultrahuman MCP repository before use, keep tokens out of shared configs and logs, and rotate the token if exposure is suspected. <br>


## Reference(s): <br>
- [Ultrahuman Developer Portal](https://vision.ultrahuman.com/developer) <br>
- [Ultrahuman MCP repository](https://github.com/Monasterolo21/Ultrahuman-MCP) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and plain-text health summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local mcporter and Ultrahuman MCP configuration with Ultrahuman credentials.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
