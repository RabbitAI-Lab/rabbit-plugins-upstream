## Description: <br>
Security monitoring and infrastructure health checks for OpenClaw agents, including breach monitoring, SSL certificate expiry checks, GitHub security audits, credential rotation tracking, secret scanning, git hygiene, token watchdog checks, and permission audits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arc-claw-bot](https://clawhub.ai/user/arc-claw-bot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and security-minded operators use this skill to run local security and infrastructure health checks for OpenClaw agent environments, then review warnings or critical findings for follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill inspects sensitive local security configuration and credential metadata. <br>
Mitigation: Install and run it only in environments where that level of local read access is intended and authorized. <br>
Risk: Generated reports and credential tracker data can contain sensitive operational details. <br>
Mitigation: Treat report files and credential-tracker files as sensitive and avoid committing them to source control. <br>
Risk: HaveIBeenPwned monitoring queries account breach status. <br>
Mitigation: Enable HIBP checks only for accounts the operator is authorized to monitor. <br>
Risk: Recurring heartbeat or cron execution can repeatedly scan local configuration. <br>
Mitigation: Configure scheduled execution only when recurring scans are desired and review the destination for logs and reports. <br>


## Reference(s): <br>
- [Arc Sentinel ClawHub release page](https://clawhub.ai/arc-claw-bot/skills/arc-sentinel) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Terminal reports and JSON report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include security findings, credential rotation status, and paths to sensitive local configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
