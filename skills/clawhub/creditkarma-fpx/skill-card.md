## Description: <br>
Query Credit Karma transactions from a shell with the fpx CLI by capturing signed-in session cookies once, then using curl against Credit Karma transaction and refresh endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to retrieve Credit Karma transaction data from a shell or script without running the creditkarma-mcp server. It provides setup, cookie capture, pagination, token refresh, and response-checking guidance for the Credit Karma transaction workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credit Karma cookies and access or refresh tokens can expose the user's account and transaction history. <br>
Mitigation: Use only in a trusted local environment, keep credentials in shell variables when possible, avoid shell history and logs, and store any necessary credential files with restrictive permissions. <br>
Risk: Request and response files written under /tmp may contain sensitive financial data or reusable session material. <br>
Mitigation: Delete temporary request and response files after use and avoid sharing logs or terminal transcripts that include cookie, token, or transaction values. <br>
Risk: The workflow depends on unpublished Credit Karma endpoints and short-lived browser session credentials. <br>
Mitigation: Check each GraphQL response for in-body authentication errors before trusting the data, refresh tokens only as documented, and re-capture cookies from a signed-in browser session when refresh fails. <br>


## Reference(s): <br>
- [Credit Karma fpx request examples](references/requests.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance includes commands for cookie capture, GraphQL transaction requests, pagination, token refresh, and error checks.] <br>

## Skill Version(s): <br>
2.3.3 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
