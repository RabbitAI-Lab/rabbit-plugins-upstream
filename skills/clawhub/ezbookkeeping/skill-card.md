## Description: <br>
Use ezBookkeeping API Tools script to record new transactions, query transactions, retrieve account information, retrieve categories, retrieve tags, and retrieve exchange rate data in the self hosted personal finance application ezBookkeeping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayswind](https://clawhub.ai/user/mayswind) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and personal finance automation users use this skill to call ezBookkeeping APIs from shell or PowerShell scripts for account, category, tag, transaction, exchange-rate, server-version, and session-token workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify financial data in ezBookkeeping. <br>
Mitigation: Install only when the agent is expected to query or change ezBookkeeping data, and review proposed write operations before execution. <br>
Risk: The skill can list and revoke login tokens. <br>
Mitigation: Treat token administration commands as sensitive actions that require explicit user intent. <br>
Risk: The skill requires an API token and may read token values from environment variables or .env files. <br>
Mitigation: Use a dedicated least-privilege token, avoid broad home-directory .env secrets when possible, and restrict token file permissions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mayswind/skills/ezbookkeeping) <br>
- [ezBookkeeping](https://ezbookkeeping.mayswind.net) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Markdown, Configuration] <br>
**Output Format:** [Shell or PowerShell command output, with JSON responses or markdown tables when pretty formatting is available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EBKTOOL_SERVER_BASEURL and EBKTOOL_TOKEN for authenticated ezBookkeeping API access.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
