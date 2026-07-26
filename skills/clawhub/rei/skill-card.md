## Description: <br>
Set up Rei Qwen3 Coder as a model provider. Use when configuring coder.reilabs.org, adding Rei to Clawdbot, or troubleshooting 403 errors from Rei endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xreisearch](https://clawhub.ai/user/0xreisearch) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to configure Rei Qwen3 Coder as a Clawdbot model provider, switch between Rei and Opus models, and troubleshoot Rei endpoint access issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow requires a Rei API key and writes it into the local Clawdbot configuration. <br>
Mitigation: Use a dedicated revocable API key, avoid exposing it in shared chat or shell history, and check permissions on ~/.clawdbot/clawdbot.json. <br>
Risk: Routing model traffic through Rei changes where Clawdbot requests are sent. <br>
Mitigation: Install only when intending to use Rei as a provider and keep the backup/revert script available. <br>


## Reference(s): <br>
- [ClawHub Rei Skill](https://clawhub.ai/0xreisearch/skills/rei) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes setup, model switching, revert, and troubleshooting guidance for Clawdbot.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
