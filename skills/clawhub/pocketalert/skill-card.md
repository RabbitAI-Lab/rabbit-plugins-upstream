## Description: <br>
The Pocket Alert (pocketalert.app) skill for OpenClaw enables OpenClaw agents and workflows to send push notifications to iOS and Android devices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akellacom](https://clawhub.ai/user/akellacom) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation operators use this skill to send Pocket Alert push notifications from OpenClaw workflows, CI/CD jobs, monitoring checks, and background tasks. The skill also documents Pocket Alert CLI commands for listing and managing messages, applications, devices, webhooks, and configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The integration can give agents account-management and configuration powers beyond simple notification sending. <br>
Mitigation: Install it only when those capabilities are intended, and require explicit human approval before delete, API-key, or base-URL configuration commands are run. <br>
Risk: Notification messages can expose secrets or sensitive operational data to external devices or services. <br>
Mitigation: Use least-privilege API credentials when available and avoid sending secrets or sensitive operational data in alert titles, messages, or webhook templates. <br>
Risk: The Pocket Alert CLI must be downloaded and authenticated outside the skill. <br>
Mitigation: Verify the CLI download source before installation and store API credentials according to local secret-management policy. <br>


## Reference(s): <br>
- [Pocket Alert](https://pocketalert.app) <br>
- [Pocket Alert CLI Installation](https://info.pocketalert.app/cli.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/akellacom/skills/pocketalert) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the pocketalert CLI to be installed and authenticated before command execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
