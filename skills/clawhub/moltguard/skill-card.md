## Description: <br>
MoltGuard is an OpenClaw security guard that helps protect agents and users from prompt injection, data exfiltration, and malicious commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaslwang](https://clawhub.ai/user/thomaslwang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users and teams use this skill to install and manage MoltGuard, a cloud-backed guardrail plugin that monitors prompt, behavioral, and data-risk surfaces for agent activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: MoltGuard is cloud-backed and may send agent activity or sensitive data to Core for security detection. <br>
Mitigation: Review the external provider terms and data handling before enabling it, and use an approved enterprise Core deployment when organizational policy requires it. <br>
Risk: MoltGuard API keys and Agent IDs are secrets that may appear during status, claim, or configuration flows. <br>
Mitigation: Treat these values as credentials, avoid sharing them in terminals or chats, and rotate them if they are exposed. <br>
Risk: Automatic credential setup can activate protection and store credentials locally after installation. <br>
Mitigation: Install only after explicit user intent, then inspect the generated OpenClaw configuration and credential storage path before broader rollout. <br>


## Reference(s): <br>
- [OpenGuardrails MoltGuard homepage](https://github.com/openguardrails/openguardrails/tree/main/moltguard) <br>
- [ClawHub MoltGuard listing](https://clawhub.ai/thomaslwang/skills/moltguard) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides installation, status, account-claiming, enterprise enrollment, update, and uninstall guidance for OpenClaw.] <br>

## Skill Version(s): <br>
6.8.16 (source: SKILL.md frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
