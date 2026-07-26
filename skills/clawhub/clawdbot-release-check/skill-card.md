## Description: <br>
Check for new clawdbot releases and notify once per new version. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pors](https://clawhub.ai/user/pors) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Clawdbot users and operators use this skill to check for newer Clawdbot releases, review current and latest version status, and optionally enable a daily notification job. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional setup script creates a persistent daily notification job. <br>
Mitigation: Run setup.sh only when a scheduled check is desired, confirm the notification channel and recipient before enabling it, and remove the job with setup.sh --uninstall when it is no longer needed. <br>
Risk: The checker contacts GitHub release endpoints and stores local state and cache files. <br>
Mitigation: Use the skill only when release checks are expected, and review or clear ~/.clawdbot state and cache files if notification behavior needs to be reset. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/pors/skills/clawdbot-release-check) <br>
- [Clawdbot GitHub Homepage](https://github.com/clawdbot/clawdbot) <br>
- [Clawdbot GitHub Releases API](https://api.github.com/repos/clawdbot/clawdbot/releases) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown-style notification text, status text, and shell setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; may read and write local state and cache files under ~/.clawdbot.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
