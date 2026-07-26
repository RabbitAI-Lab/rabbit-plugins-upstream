## Description: <br>
Fetch real-time stock quotes from Yahoo Finance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noypearl](https://clawhub.ai/user/noypearl) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users can fetch current Yahoo Finance quote data for one or more stock ticker symbols and receive normalized JSON for agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ticker symbols requested through the skill are sent to Yahoo Finance. <br>
Mitigation: Only request ticker symbols that are acceptable to share with Yahoo Finance, and review this network behavior before deployment. <br>
Risk: Quote data depends on Yahoo Finance availability and may return null fields for missing symbols. <br>
Mitigation: Handle null fields in downstream workflows and verify market data before using it for decisions. <br>
Risk: The skill requires Node to run. <br>
Mitigation: Confirm Node is available in the agent runtime environment before installation or execution. <br>


## Reference(s): <br>
- [Yahoo Finance quote endpoint](https://query1.finance.yahoo.com/v7/finance/quote) <br>
- [ClawHub skill page](https://clawhub.ai/noypearl/skills/yahoo-data-fetcher) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON] <br>
**Output Format:** [JSON array of stock quote objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns null quote fields for symbols Yahoo Finance does not return.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
