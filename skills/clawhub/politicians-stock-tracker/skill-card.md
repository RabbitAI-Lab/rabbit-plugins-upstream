## Description: <br>
Track congress stock trades and politician stock trades: Pelosi tracker, senate stock trades, House trades, congress trades by ticker, and STOCK Act disclosures sourced from House Clerk and Senate eFD filings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and financial researchers use this skill to retrieve and summarize public U.S. congressional stock-trade disclosures by recent activity, ticker, member, and disclosure timing. Outputs are informational and should not be treated as personalized investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SentiSense API key and sends congressional-trade lookup requests to SentiSense. <br>
Mitigation: Keep SENTISENSE_API_KEY in the environment, do not paste it into chat output or URLs, and install only if this external API use is acceptable. <br>
Risk: Congressional disclosure data can be misread as trading advice. <br>
Mitigation: Present results as informational context only and avoid personalized buy, sell, portfolio, or order-entry recommendations. <br>
Risk: STOCK Act filings report amount ranges and may be disclosed after the transaction date. <br>
Mitigation: Quote amountRange bands, distinguish transactionDate from disclosureDate, and include disclosureDelayDays when summarizing trades. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/politicians-stock-tracker) <br>
- [SentiSense](https://sentisense.ai) <br>
- [SentiSense API Key](https://app.sentisense.ai/get-api-key) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, API Calls, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries with JSON-derived disclosure data and inline bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only GET requests require SENTISENSE_API_KEY; returned financial data is informational and not trading advice.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
