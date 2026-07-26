## Description: <br>
Plaid helps agents use plaid-cli to link financial institutions, fetch account balances, and query transactions by date range through Plaid. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jverdi](https://clawhub.ai/user/jverdi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users can use this skill to guide an agent through Plaid account linking, balance lookup, transaction search, and transaction monitoring workflows with plaid-cli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help access Plaid-linked financial account, balance, transaction, and token data. <br>
Mitigation: Install only when the external plaid-cli dependency is trusted, protect ~/.plaid-cli, avoid shared machines, and use sandbox credentials for testing. <br>
Risk: The plaid-cli tokens command can display access tokens. <br>
Mitigation: Avoid running token-display commands unless the user explicitly requests them and understands the exposure. <br>
Risk: Secrets such as client IDs, secrets, and access tokens can be exposed through logs or command output. <br>
Mitigation: Do not print or log secrets, and keep Plaid credentials in protected environment variables or local configuration. <br>


## Reference(s): <br>
- [Plaid skill page](https://clawhub.ai/jverdi/skills/plaid) <br>
- [plaid-cli Go module](https://github.com/jverdi/plaid-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON or CSV command output handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may involve Plaid-linked financial data, local token storage under ~/.plaid-cli, and plaid-cli commands that can display access tokens when explicitly requested.] <br>

## Skill Version(s): <br>
0.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
