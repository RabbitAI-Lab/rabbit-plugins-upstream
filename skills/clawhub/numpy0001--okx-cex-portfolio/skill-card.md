## Description: <br>
Helps agents inspect OKX account balances, positions, P&L, bills, fees, configuration, withdrawal limits, and confirmed internal account changes using the OKX CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[numpy0001](https://clawhub.ai/user/numpy0001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide an agent through OKX portfolio and account workflows, including balance snapshots, funding and trading account checks, position and P&L review, account bills, fees, limits, transfers, and position-mode changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive OKX balances, positions, bills, and related account data. <br>
Mitigation: Install only when this account access is intended, use demo mode first, and keep credentials out of chat. <br>
Risk: Live transfers or position-mode changes can affect real funds. <br>
Mitigation: Verify live versus demo mode before every action and review any transfer or position-mode change before approving it. <br>


## Reference(s): <br>
- [OKX homepage](https://www.okx.com) <br>
- [ClawHub skill page](https://clawhub.ai/numpy0001/okx-cex-portfolio) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline OKX CLI commands and command output interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should identify whether live or demo mode was used after each command result.] <br>

## Skill Version(s): <br>
1.3.8 (source: evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
