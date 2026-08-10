## Description: <br>
Monitors OpenClaw model API status and helps an agent ask for confirmation before switching models when quota or error signals appear. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2233admin](https://clawhub.ai/user/2233admin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to check model API status, review quota warnings, and switch the configured model only after an explicit decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed model switches can interrupt service because the OpenClaw gateway is restarted. <br>
Mitigation: Run switching commands only after an explicit decision and schedule changes outside peak usage when possible. <br>
Risk: The skill can read local OpenClaw status files and edit the OpenClaw configuration. <br>
Mitigation: Use trusted config and log paths, avoid elevated execution, and review the target model before running --confirm or --model. <br>
Risk: Optional scheduled checks can create recurring local execution. <br>
Mitigation: Add the cron job only when ongoing scheduled monitoring is intended and keep its log path under operational review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/2233admin/api-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and command output text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read OpenClaw status files; confirmed switches can edit openclaw.json and restart the OpenClaw gateway.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
