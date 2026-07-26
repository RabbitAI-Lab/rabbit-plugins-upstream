## Description: <br>
Deploy a lightweight status API that exposes an OpenClaw bot's runtime health, service connectivity, cron jobs, skills, system metrics, and related operational status as JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[suspect80](https://clawhub.ai/user/suspect80) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to set up a local JSON status endpoint for an OpenClaw agent, including health, service, cron, skill, and system signals for dashboards or status pages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The status API can expose sensitive operational details about an OpenClaw bot, services, skills, and host system metrics. <br>
Mitigation: Run it only in a trusted local or admin environment, bind it to localhost or protect it with strong authentication and TLS, and avoid exposing returned status data publicly. <br>
Risk: Config-driven command checks can execute host shell commands if enabled. <br>
Mitigation: Disable command checks unless every configuration source is trusted, review configured commands before use, and run the service under a low-privilege account. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/suspect80/skills/bot-status-api-test) <br>
- [Publisher profile](https://clawhub.ai/user/suspect80) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON, shell, and systemd configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup guidance for a Node.js status API and JSON status output shape.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
