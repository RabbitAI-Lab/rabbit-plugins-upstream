## Description: <br>
Connects a Feishu or Lark bot to Clawdbot through a local WebSocket bridge for setup, troubleshooting, service management, and group chat behavior tuning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexanys](https://clawhub.ai/user/alexanys) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to connect Feishu or Lark chat to a local Clawdbot agent, configure bot credentials, run the bridge, manage the macOS launchd service, and tune group chat response behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Feishu chat messages are routed through the local bridge to the configured Clawdbot agent. <br>
Mitigation: Install only for intended Feishu bots and chats, and review group-response rules before enabling the bridge. <br>
Risk: The bridge depends on Feishu App Secret and Clawdbot gateway token handling. <br>
Mitigation: Store the Feishu secret in the configured secret file with restrictive permissions and protect the Clawdbot configuration token. <br>
Risk: The service can continue running under macOS launchd after setup. <br>
Mitigation: Unload the LaunchAgent when the bridge should not receive or forward chat messages. <br>
Risk: The WebSocket dependency is declared with a semver range. <br>
Mitigation: Update and lock the ws dependency to a fixed reviewed version before production deployment. <br>


## Reference(s): <br>
- [Feishu Open Platform](https://open.feishu.cn/app) <br>
- [ClawHub skill page](https://clawhub.ai/alexanys/skills/feishu-bridge) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Covers Feishu bot setup, local bridge startup, macOS launchd service management, diagnostics, and group-response tuning.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
