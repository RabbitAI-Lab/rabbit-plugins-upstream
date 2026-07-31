## Description: <br>
Uses Eastmoney MX condition-based stock screening and universe lookup to help find stocks, listed companies, sector constituents, index constituents, or candidates matching market, valuation, financial, industry, board, or concept constraints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoeluli7459-dev](https://clawhub.ai/user/zoeluli7459-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to turn natural-language A-share, sector, concept, or index screening requests into Eastmoney MX stock-screening queries, CSV outputs, and concise result summaries. It is intended for data-screening candidates and constituent lookup, not single-security quotes, news research, watchlist actions, simulated trading, or personalized buy/sell advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stock-screening queries and the MX_APIKEY are sent to the Eastmoney MX endpoint. <br>
Mitigation: Confirm the endpoint and data-sharing posture are acceptable before installation, and scope the MX_APIKEY according to the user's operational requirements. <br>
Risk: The skill writes CSV, description, and raw JSON response files to the configured local output directory. <br>
Mitigation: Use MX_OUTPUT_DIR to choose an appropriate storage location and review generated files before sharing them outside the local environment. <br>
Risk: Screening results may be mistaken for investment advice. <br>
Mitigation: Present results as data-screening candidates, include match counts and key filters, and avoid buy/sell recommendations unless a separate analysis workflow is explicitly requested. <br>


## Reference(s): <br>
- [mx-xuangu Result Fields](references/result-fields.md) <br>
- [Eastmoney MX stock-screen endpoint](https://mkapi2.dfcfs.com/finskillshub/api/claw/stock-screen) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Code] <br>
**Output Format:** [Markdown summary with shell command guidance and generated CSV, description, and raw JSON file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include parsed screening conditions, match counts, representative rows, and local result file paths; API failures or ambiguous constraints are reported for user action.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
