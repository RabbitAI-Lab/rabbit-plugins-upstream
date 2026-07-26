## Description: <br>
WHOOP morning check-in (recovery/sleep/strain) with suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[borahm](https://clawhub.ai/user/borahm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent operators use this skill to authorize WHOOP access, run a morning check-in, and return recent recovery, sleep, strain, and daily suggestion text to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests long-lived access to a WHOOP health account through a refresh token. <br>
Mitigation: Treat the refresh token like a password, keep the environment file and token cache private, and revoke the WHOOP app authorization when access is no longer needed. <br>
Risk: The security review notes missing, unreviewed command scripts for authorization and daily check-ins. <br>
Mitigation: Inspect the missing whoop-auth and whoop-morning code before installing the skill, running the commands, or enabling a daily cron schedule. <br>
Risk: Command output may expose health details or credentials if copied into logs or shared messages. <br>
Mitigation: Avoid sharing command output that contains tokens or sensitive WHOOP recovery, sleep, or strain details. <br>


## Reference(s): <br>
- [ClawHub WHOOP skill page](https://clawhub.ai/borahm/skills/whoop) <br>
- [WHOOP OAuth authorization endpoint](https://api.prod.whoop.com/oauth/oauth2/auth) <br>
- [WHOOP OAuth token endpoint](https://api.prod.whoop.com/oauth/oauth2/token) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and plain-text morning check-in guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WHOOP OAuth credentials and a refresh token before the check-in command can run.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
