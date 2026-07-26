## Description: <br>
Query Copilot Money personal finance data (accounts, transactions, net worth, holdings, asset allocation) and refresh bank connections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jayhickey](https://clawhub.ai/user/jayhickey) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to answer questions about Copilot Money account balances, transactions, net worth, holdings, and asset allocation, and to refresh bank connections when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a CLI that reads a local browser session token and retrieves sensitive Copilot Money financial data. <br>
Mitigation: Install only when the publisher and package are trusted, use explicit prompts, and treat access as equivalent to access to the user's Copilot Money account. <br>
Risk: Refresh or sync actions may affect connected financial account data. <br>
Mitigation: Require confirmation before refresh or sync actions and revoke the browser session when access is no longer wanted. <br>


## Reference(s): <br>
- [Copilot Money](https://copilot.money) <br>
- [ClawHub Skill Page](https://clawhub.ai/jayhickey/skills/copilot-money) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve sensitive personal finance data and local browser session token access through the referenced CLI.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
