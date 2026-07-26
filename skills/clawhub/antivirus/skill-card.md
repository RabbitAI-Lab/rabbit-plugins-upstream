## Description: <br>
MoltGuard helps protect agents and users from prompt injection, data exfiltration, and malicious commands hidden in files or web content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaslwang](https://clawhub.ai/user/thomaslwang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to install and operate MoltGuard security checks for prompt injection, data leakage, risky commands, and account or enterprise Core configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives a third-party Core service visibility into sensitive agent activity during security checks. <br>
Mitigation: Install only after reviewing the service trust boundary and data handling expectations; use an approved enterprise Core deployment when required. <br>
Risk: The skill creates and exposes local API credentials through account-claiming and status workflows. <br>
Mitigation: Do not share claim or status output in logged or collaborative chats, and confirm how to revoke credentials and remove the plugin before deployment. <br>
Risk: Runtime plugin installation, local dashboard startup, and configuration scripts can change the local agent environment. <br>
Mitigation: Review the installation and uninstall steps in a controlled environment before broader use. <br>


## Reference(s): <br>
- [ClawHub Antivirus skill page](https://clawhub.ai/thomaslwang/skills/antivirus) <br>
- [OpenGuardrails MoltGuard homepage](https://github.com/openguardrails/openguardrails/tree/main/moltguard) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and slash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve local plugin installation, external Core service checks, dashboard access, and API credential handling.] <br>

## Skill Version(s): <br>
6.8.20 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
