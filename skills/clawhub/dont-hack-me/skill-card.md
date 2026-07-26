## Description: <br>
Security self-check for Clawdbot/Moltbot that audits clawdbot.json for exposed gateway settings, missing authentication, open messaging policies, weak tokens, loose file permissions, and plaintext secrets, with user-approved auto-fixes for fixable findings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[peterokase42](https://clawhub.ai/user/peterokase42) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to review local Clawdbot/Moltbot configuration for common security misconfigurations and to apply explicit, user-approved fixes. It is intended for local configuration auditing before sharing reports or changing gateway, token, channel, or file-permission settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read sensitive local Clawdbot/Moltbot configuration while performing the audit. <br>
Mitigation: Invoke it explicitly for that configuration and review the report before sharing it because it may expose gateway, token, channel, and file-permission details. <br>
Risk: Auto-fixes can change gateway access, authentication tokens, channel policies, and file permissions. <br>
Mitigation: Approve fixes only after reviewing the proposed changes; the skill backs up the original file and asks for confirmation before applying fixable changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/peterokase42/skills/dont-hack-me) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown report with PASS, WARN, FAIL, and SKIP statuses, plus optional configuration-change guidance and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May inspect sensitive local configuration and propose edits only after user approval.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
