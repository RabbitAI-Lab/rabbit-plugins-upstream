## Description: <br>
Guides an agent through setting up a complete OpenClaw personal AI assistant on AWS, including server provisioning, OpenClaw installation, Telegram setup, API configuration, optional Google Workspace integration, security hardening, and personalization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[j540](https://clawhub.ai/user/j540) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and technically comfortable users use this skill to have an agent deploy and configure a persistent OpenClaw assistant on their own AWS infrastructure. The workflow covers infrastructure setup, messaging integration, model credentials, optional productivity integrations, and operational checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to administer a cloud server and configure a persistent assistant with broad access. <br>
Mitigation: Review privileged commands before execution, use least-privilege cloud credentials, and verify how to stop the service and revoke access. <br>
Risk: The workflow involves live API keys, bot tokens, OAuth credentials, and possibly Google Workspace data. <br>
Mitigation: Use fresh credentials, avoid sharing long-lived secrets in chat, limit OAuth scopes, and revoke tokens after testing or when no longer needed. <br>
Risk: The security scan summary says the guide has weak guardrails around credential handling. <br>
Mitigation: Confirm where secrets are stored, restrict file permissions, and avoid embedding reusable secrets directly in persistent configuration when a safer secret store is available. <br>


## Reference(s): <br>
- [OpenClaw installation human guide](references/openclaw-installation-human-guide.md) <br>
- [OpenClaw documentation](https://docs.clawd.bot) <br>
- [gog CLI repository](https://github.com/steipete/gogcli.git) <br>
- [Skill page](https://clawhub.ai/j540/skills/openclaw-setup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline JSON and bash command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes privileged setup steps, credential collection prompts, and operational verification checklists.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
