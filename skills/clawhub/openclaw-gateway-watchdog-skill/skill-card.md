## Description: <br>
Monitor the OpenClaw Gateway plus configured Spark, Local API Hub, and Dashboard loopback health endpoints with a read-only watchdog state machine, local state files, cooldown dedupe, and optional Discord alerts on macOS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathanjing](https://clawhub.ai/user/jonathanjing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to monitor OpenClaw Gateway, Spark, Local API Hub, and Dashboard health from macOS, with foreground checks, optional cron or LaunchAgent execution, local audit state, and Discord incident notifications. It is intended for explicitly configured monitoring and recovery notification, not service restart or OpenClaw configuration changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A configured Spark API token can be repeatedly sent to the configured Spark status endpoint. <br>
Mitigation: Keep SPARK_API_URL on loopback or a trusted internal host, avoid relying on ~/.openclaw/.env for this watchdog unless URL validation is added, and review configuration before installation. <br>
Risk: Discord delivery sends operational incident details to a third-party destination. <br>
Mitigation: Use a private allowlisted Discord channel or webhook and grant only the permissions needed to post alerts. <br>
Risk: Cron or LaunchAgent setup can run the watchdog unattended on a schedule. <br>
Mitigation: Review the cron or LaunchAgent entry, interval, command path, and environment before loading it. <br>


## Reference(s): <br>
- [Cron Agent Turn Template](references/cron-agent-turn.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/jonathanjing/skills/openclaw-gateway-watchdog-skill) <br>
- [ClawHub Skill Homepage](https://clawhub.ai/jonathanjing/openclaw-gateway-watchdog-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can guide foreground checks, cron setup, LaunchAgent setup, and concise Discord incident reporting; the runtime script writes local state files and event logs when executed.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release, skill.json, SKILL.md metadata, CHANGELOG released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
