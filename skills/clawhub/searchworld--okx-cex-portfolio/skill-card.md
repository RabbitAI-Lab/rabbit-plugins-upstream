## Description: <br>
Provides OKX account balance, positions, P&L, bills, fees, account configuration, withdrawal limit, position-mode, and internal transfer guidance through the OKX CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[searchworld](https://clawhub.ai/user/searchworld) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect OKX portfolio state, review account activity, check fees and limits, and prepare or confirm internal fund transfers. It is suited for account operations, not market data, order placement, or trading bot workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive OKX account data and may expose credential details if configuration output is shared. <br>
Mitigation: Use a dedicated OKX sub-account with limited permissions and avoid displaying or summarizing `okx config show --json` output. <br>
Risk: Some supported actions can perform internal fund transfers or change position mode. <br>
Mitigation: Confirm live versus demo mode and the exact transfer or position-mode parameters before executing write commands, then verify account state afterward. <br>
Risk: The npm install may download and retain an additional OKX executable under the user's home directory. <br>
Mitigation: Review the package and installed executable before enabling the skill in an agent environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-portfolio) <br>
- [OKX homepage](https://www.okx.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI output interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should state whether live or demo mode was used and avoid exposing credential configuration output.] <br>

## Skill Version(s): <br>
1.4.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
