## Description: <br>
This skill helps an agent fetch stock quotes, earnings information, financial data, trending symbols, and other Yahoo Finance market data through a command-line interface. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stuhorsman](https://clawhub.ai/user/stuhorsman) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and analysts use this skill when an agent needs to look up Yahoo Finance market data such as quotes, company profiles, earnings dates, analyst recommendations, historical OHLCV data, search results, and trending symbols. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install flow adds `jq`, installs the `yahoo-finance2` npm CLI, and may create or overwrite a local `yf` command symlink. <br>
Mitigation: Review install commands before execution and install in an environment where adding packages and managing the `yf` symlink is acceptable. <br>
Risk: The CLI makes network requests to Yahoo Finance and may store cookies locally. <br>
Mitigation: Use the skill only where external market-data access and the documented cookie-file behavior are acceptable; delete the cookie file if troubleshooting requires it. <br>
Risk: The reviewed behavior is market-data lookup, not trading authority. <br>
Mitigation: Treat outputs as informational market data and verify important values before making financial or operational decisions. <br>


## Reference(s): <br>
- [Yahoo Finance CLI Skill Page](https://clawhub.ai/stuhorsman/skills/yahoo-finance-cli) <br>
- [Publisher Profile: stuhorsman](https://clawhub.ai/user/stuhorsman) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance centers on the `yf` Yahoo Finance CLI and `jq`; command output from the external CLI is JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
