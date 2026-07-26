## Description: <br>
Guides OKX CLI authentication, including site selection, OAuth device-flow login, API-key detection, session status checks, logout, and auth binary management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[numpy0001](https://clawhub.ai/user/numpy0001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to connect Codex or OpenClaw workflows to an OKX account, recover from authentication failures, and prepare authenticated OKX trading, portfolio, earn, or bot workflows. It is not intended for unauthenticated market-data queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can request OAuth authorization or API-key setup for an OKX account, creating sensitive account-access exposure. <br>
Mitigation: Install and use it only when the user intends to connect OKX, and grant only account permissions the user understands and accepts. <br>
Risk: The skill depends on OKX CLI commands and may store login state under OKX tooling. <br>
Mitigation: Use trusted OKX CLI packages, review authentication status before trading workflows, and avoid sharing credentials in chat unless the user explicitly chooses the API-key path. <br>
Risk: Choosing the wrong OKX site can route authentication to the wrong regional endpoint. <br>
Mitigation: Require explicit site selection before OAuth login and pass the selected site to the CLI login command. <br>


## Reference(s): <br>
- [OKX](https://www.okx.com) <br>
- [ClawHub skill page](https://clawhub.ai/numpy0001/okx-cex-auth) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON parsing instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May surface OAuth verification URLs, user codes, selected OKX site identifiers, login status, scopes, and CLI troubleshooting steps.] <br>

## Skill Version(s): <br>
1.3.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
