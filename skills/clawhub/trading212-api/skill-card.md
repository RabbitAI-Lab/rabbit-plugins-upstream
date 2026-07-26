## Description: <br>
Guides agents through Trading 212 API authentication, account and portfolio queries, instrument lookup, report export, and order placement or cancellation for Demo or Live accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tsvetelin-kulinski](https://clawhub.ai/user/tsvetelin-kulinski) <br>

### License/Terms of Use: <br>
MIT License <br>


## Use Case: <br>
Developers, operators, and Trading 212 account holders can use this skill to configure API access, inspect account state, search instruments, export reports, and prepare or execute Trading 212 orders through an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide live brokerage order placement or cancellation, which may move real money or create duplicate orders if requests are wrong or repeated. <br>
Mitigation: Use DEMO mode first, require explicit confirmation before every live order or cancellation, and manually verify environment, account, ticker, quantity, side, and price before execution. <br>
Risk: Trading 212 API credentials and account data are sensitive and could be exposed through chat transcripts, shell history, logs, or downloaded reports. <br>
Mitigation: Keep API keys out of chat and shell history where possible, use environment variables or private secret storage, store reports only in private locations, and delete exported files when no longer needed. <br>
Risk: Environment, account, or instrument mismatches can cause failed calls or unintended trades against the wrong account or security. <br>
Mitigation: Confirm LIVE versus DEMO and Invest versus Stocks ISA before API calls, look up the exact Trading 212 ticker before trading, and ask the user to choose when multiple instrument matches exist. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tsvetelin-kulinski/skills/trading212-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include curl commands, environment variable setup, API response examples, validation steps, and CSV report download guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
