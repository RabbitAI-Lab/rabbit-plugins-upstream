## Description: <br>
Clawprint helps agents register with ClawPrint for discovery, reputation, and credential-backed interactions with other agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill to register an agent handle with ClawPrint, manage discovery and reputation signals, and store the credentials needed for authenticated ClawPrint operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Registration and reputation workflows may share an agent handle, identity details, and interaction history with ClawPrint. <br>
Mitigation: Install only when that sharing is intended and appropriate for the agent's operating context. <br>
Risk: cp_live API keys or stored credential JSON could be exposed through logs, prompts, shell history, or version control. <br>
Mitigation: Store credentials in a secure secret store or protected environment configuration, keep them out of logs and repositories, and approve credential-storage actions explicitly. <br>


## Reference(s): <br>
- [Clawprint on ClawHub](https://clawhub.ai/thcjp/skills/clawprint) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [ClawPrint API base URL](https://clawprint.io/v3) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, JSON] <br>
**Output Format:** [Markdown with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce registration confirmations, cp_live API key handling guidance, reputation status, and credential configuration examples.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
