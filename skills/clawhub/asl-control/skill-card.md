## Description: <br>
Monitor and control AllStar Link amateur radio nodes via REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kj5irq](https://clawhub.ai/user/kj5irq) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Radio operators and automation agents use this skill to check node status, manage AllStar Link connections, maintain favorites, and run timed net sessions against a separately operated ASL3 REST API endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can issue authenticated commands that affect live AllStar Link node connections. <br>
Mitigation: Install it only when agent control of the target radio node is intended, and review connect, disconnect, favorite, and net-session commands before execution. <br>
Risk: The shell helper can target a default IP address if the user has not configured their own endpoint. <br>
Mitigation: Set ASL_PI_IP or ASL_API_BASE explicitly before use, and review or remove the helper's default IP address. <br>
Risk: API keys and network transport protect access to the ASL3 REST endpoint. <br>
Mitigation: Protect and rotate ASL_API_KEY as needed, and prefer a trusted tunnel such as Tailscale or an HTTPS-capable endpoint. <br>
Risk: Aliases and cron-based net tick can trigger connect or disconnect actions later. <br>
Mitigation: Review aliases, saved net profiles, durations, and cron schedules before enabling unattended operation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kj5irq/skills/asl-control) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; command output can be JSON or text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 plus ASL_PI_IP and ASL_API_KEY; optional state files store favorites and timed net-session data outside the skill directory.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
