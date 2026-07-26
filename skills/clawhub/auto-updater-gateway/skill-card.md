## Description: <br>
Guides agents through scheduling daily or weekly Gateway cron jobs that report on or apply Clawdbot and installed skill updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xabo1986](https://clawhub.ai/user/xabo1986) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to configure recurring Clawdbot Gateway cron jobs that update installed skills, optionally update Clawdbot, and deliver change reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent unattended Gateway cron jobs can update all installed skills and optionally update or restart Clawdbot. <br>
Mitigation: Start with report-only checks, schedule runs during quiet periods, require manual approval before Clawdbot self-updates or restarts, and confirm how to list, pause, or delete the cron job. <br>
Risk: Example commands include local absolute paths and a Telegram recipient value that may not match the user's environment. <br>
Mitigation: Replace all paths and delivery recipients before use, then verify `clawdhub whoami` in the target workdir before enabling updates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xabo1986/skills/auto-updater-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes cron timing, timezone, delivery channel, update scope, and report contents; users replace example paths and recipient values.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and artifact frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
