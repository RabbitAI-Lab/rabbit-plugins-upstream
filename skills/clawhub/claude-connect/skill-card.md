## Description: <br>
Connect Claude to Clawdbot instantly and keep it connected 24/7. Run after setup to link your subscription, then auto-refreshes tokens forever. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tunaissacoding](https://clawhub.ai/user/tunaissacoding) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Clawdbot users with an existing Claude CLI subscription use this legacy skill to copy OAuth credentials into Clawdbot and keep those credentials refreshed with a macOS launchd job. Clawdbot's native Claude OAuth setup should be preferred when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles live Claude OAuth tokens and copies refresh credentials between Keychain and Clawdbot auth files. <br>
Mitigation: Install only when this legacy refresher is specifically needed, prefer Clawdbot native OAuth when available, and protect auth-profiles.json and related credential files. <br>
Risk: The installer can create a persistent macOS launchd job that refreshes tokens in the background. <br>
Mitigation: Review the launchd service before installation and unload or remove it when the refresher is no longer needed. <br>
Risk: The skill can auto-detect notification targets and send refresh status messages through configured channels. <br>
Mitigation: Disable notifications or configure the notification target manually before running the installer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tunaissacoding/skills/claude-connect) <br>
- [Clawdbot documentation](https://docs.clawd.bot) <br>
- [Quickstart guide](QUICKSTART.md) <br>
- [Upgrade guide](UPGRADE.md) <br>
- [README deprecation notice](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, and script-backed setup steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write OAuth profile configuration, Keychain entries, logs, launchd service files, and notification settings when scripts are run.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and CHANGELOG.md, released 2026-01-26) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
