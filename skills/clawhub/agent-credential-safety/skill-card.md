## Description: <br>
Guides coding agents to handle local API keys, environment variables, passwords, SSH aliases, remote servers, and authentication without exposing secret values. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sirsws](https://clawhub.ai/user/sirsws) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI coding-agent users use this skill to set operating rules for credential access, SSH usage, and authentication-sensitive tasks. It is intended to reduce accidental secret exposure while allowing agents to complete approved work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credential bridging can create an additional persistent copy of a live API key in a project .env file. <br>
Mitigation: Treat bridging as manual-only unless the user explicitly approves the exact destination and confirms the file is protected from source control and broad local access. <br>


## Reference(s): <br>
- [Coding Agent Landscape](references/coding-agent-landscape.md) <br>
- [Agent Credential Safety on ClawHub](https://clawhub.ai/sirsws/skills/agent-credential-safety) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell, Python, environment, and SSH configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Directs agents to avoid printing, copying, logging, or committing secret values.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
