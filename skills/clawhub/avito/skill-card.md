## Description: <br>
Manage Avito.ru account, items, and messenger via API. Use for listing items, checking balance, reading chats, and getting account info. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruslanlanket](https://clawhub.ai/user/ruslanlanket) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to run Avito API helper scripts for authentication, account lookup, balance checks, listing advertisements, and viewing messenger chats. <br>

### Deployment Geography for Use: <br>
Global, where Avito.ru API access is available. <br>

## Known Risks and Mitigations: <br>
Risk: Avito API credentials, bearer tokens, and account data may be exposed if commands are run in shared shells, logs, or CI jobs. <br>
Mitigation: Use short-lived or least-privileged tokens, avoid logging token-bearing commands, and prefer environment variables, stdin, or a secrets manager for sensitive values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruslanlanket/skills/avito) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, API Calls] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Avito client credentials, bearer tokens, user IDs, and network access to api.avito.ru.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
