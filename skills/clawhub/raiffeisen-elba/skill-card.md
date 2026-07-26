## Description: <br>
Automate Raiffeisen ELBA online banking: login/logout, list accounts, and fetch transactions via Playwright. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and automation developers use this skill to retrieve Raiffeisen ELBA account balances, depot positions, transactions, and documents through local browser automation after two-factor approval. <br>

### Deployment Geography for Use: <br>
Austria <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores ELBA credentials and browser session material locally, including a short-lived bearer token. <br>
Mitigation: Keep the workspace private, use restrictive file permissions, avoid shared or backed-up machines, and run logout after each session to clear cached session state. <br>
Risk: The skill extracts an authenticated bearer token from the local browser session to call Raiffeisen ELBA APIs. <br>
Mitigation: Audit the code before using real credentials, approve two-factor prompts only when expected, and stop use if the browser automation or requested bank domain is unexpected. <br>
Risk: Account, transaction, depot, and document exports may write sensitive financial data to disk. <br>
Mitigation: Write outputs only to private workspace or temporary locations, secure or delete exported files promptly, and avoid storing them in synced or shared folders. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/odrobnik/skills/raiffeisen-elba) <br>
- [Security policy](SECURITY.md) <br>
- [Setup instructions](SETUP.md) <br>
- [Accounts output schema](references/accounts.schema.json) <br>
- [Transactions output schema](references/transactions.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, JSON, CSV, files, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; runtime outputs are JSON, CSV, and downloaded files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local Python, requests, Playwright, a private workspace, and user-approved Raiffeisen two-factor authentication.] <br>

## Skill Version(s): <br>
1.4.5 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
