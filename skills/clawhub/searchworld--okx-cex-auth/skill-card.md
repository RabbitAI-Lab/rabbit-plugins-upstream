## Description: <br>
Guides agents through OKX CLI authentication, including site selection, OAuth device login, API-key handling, session checks, logout, and auth binary management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[searchworld](https://clawhub.ai/user/searchworld) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to connect an OKX account to the OKX CLI, recover expired sessions, inspect login status, and manage the required okx-auth binary before using OKX trading, portfolio, earn, or bot skills. <br>

### Deployment Geography for Use: <br>
Global, with OKX site selection for Global, EEA, US, and TR. <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill requires trusting the OKX CLI package, and successful authorization may allow account read or trading actions. <br>
Mitigation: Install it only when connecting an OKX account, review package provenance when stronger supply-chain assurance is needed, and confirm the scopes shown by OKX during authorization. <br>
Risk: A silent or incorrect site choice can connect the user to the wrong OKX regional site. <br>
Mitigation: Ask the user to choose Global, EEA, US, or TR before login and pass that exact site to the OKX auth command. <br>


## Reference(s): <br>
- [OKX homepage](https://www.okx.com) <br>
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-auth) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May surface an OAuth verification URL, user code, selected OKX site, and scope/status summaries when authentication is required.] <br>

## Skill Version(s): <br>
1.3.9 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
