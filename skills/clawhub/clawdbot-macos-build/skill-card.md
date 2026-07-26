## Description: <br>
Build the Clawdbot macOS menu bar app from source. Use when you need to install the Clawdbot.app companion (for menu bar status, permissions, and Mac hardware access like camera/screen recording). Handles dependency installation, UI build, Swift compilation, code signing, and app packaging automatically. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manish-basargekar](https://clawhub.ai/user/manish-basargekar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to build, sign, package, install, and launch the Clawdbot macOS companion app from source for menu bar status, macOS permissions, notifications, and hardware access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The quick build flow runs unpinned remote build code and package scripts. <br>
Mitigation: Review or pin the source before running the build, then inspect package scripts and scripts/package-mac-app.sh. <br>
Risk: The built app may request high-privilege macOS permissions and enable local or remote access features. <br>
Mitigation: Approve only needed permissions after confirming how to stop launchd services, disable remote access and deep links, and uninstall the app. <br>


## Reference(s): <br>
- [Clawhub skill page](https://clawhub.ai/manish-basargekar/skills/clawdbot-macos-build) <br>
- [Clawdbot macOS documentation](https://docs.clawd.bot/platforms/macos) <br>
- [Clawdbot macOS release documentation](https://docs.clawd.bot/platforms/mac/release) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Build guidance includes macOS prerequisites, signing options, installation steps, and troubleshooting.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
