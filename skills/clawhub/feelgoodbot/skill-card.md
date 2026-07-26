## Description: <br>
Set up feelgoodbot file integrity monitoring and TOTP step-up authentication for macOS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kris-hansen](https://clawhub.ai/user/kris-hansen) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to install and configure local macOS file integrity monitoring, Clawdbot alerting, and TOTP checks before sensitive agent actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup installs github.com/kris-hansen/feelgoodbot/cmd/feelgoodbot@latest, so the installed upstream binary is not pinned by version in the artifact. <br>
Mitigation: Review and trust the upstream feelgoodbot Go project before setup, or pin and audit the upstream version before deployment. <br>
Risk: The setup enables Clawdbot webhooks, stores a local webhook secret, restarts the gateway, and starts a persistent daemon. <br>
Mitigation: Review the generated local configuration and confirm webhook and daemon behavior are appropriate for the host before leaving it running. <br>
Risk: TOTP protection depends on separate initialization and agent integration before sensitive actions are protected. <br>
Mitigation: Run and verify the documented TOTP initialization and require agents to check protected actions before performing sensitive operations. <br>


## Reference(s): <br>
- [Feelgoodbot GitHub Repository](https://github.com/kris-hansen/feelgoodbot) <br>
- [Feelgoodbot ClawHub Skill Page](https://clawhub.ai/kris-hansen/skills/feelgoodbot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a setup shell script that installs an upstream Go binary, writes local configuration, enables webhook alerting, and starts a daemon.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
