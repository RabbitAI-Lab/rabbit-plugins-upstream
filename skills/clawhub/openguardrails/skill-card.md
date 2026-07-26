## Description: <br>
MoltGuard helps agents protect users from prompt injection, data exfiltration, and malicious commands hidden in files and web content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaslwang](https://clawhub.ai/user/thomaslwang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to install, test, configure, update, and remove MoltGuard protections for prompt-injection, data-exfiltration, and risky-command detection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad agent security access and may inspect sensitive prompts, files, web content, commands, secrets, or PII through a remote service. <br>
Mitigation: Install only after explicit approval from the environment owner and review whether the remote scanning model is appropriate for the data handled by the agent. <br>
Risk: /og_status or /og_claim output can expose API keys or claim credentials. <br>
Mitigation: Treat that output as secret, avoid sharing it in logs or chats, and rotate or revoke credentials if exposed. <br>
Risk: Automatic credential creation and enterprise enrollment can change how the agent routes security checks. <br>
Mitigation: Verify the Core URL before enterprise enrollment and review credential revocation or removal steps before enabling the skill. <br>


## Reference(s): <br>
- [OpenGuardrails MoltGuard homepage](https://github.com/openguardrails/openguardrails/tree/main/moltguard) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and slash-command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operational commands for installing, testing, configuring, updating, and uninstalling MoltGuard.] <br>

## Skill Version(s): <br>
6.8.20 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
