## Description: <br>
13F institutional ownership tracker: quarterly hedge fund and mutual fund holdings from SEC 13F filings, by ticker or by manager, with top institutional holders per stock, quarter-over-quarter buying and selling deltas, and activist investor positions across thousands of managers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and financial research users use this skill to retrieve read-only 13F institutional ownership context by ticker, manager, quarter-over-quarter change, aggregate flow, or activist position. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake delayed 13F context for real-time positions or personalized investment advice. <br>
Mitigation: State the reportDate and quarterly filing lag, and avoid presenting outputs as trading recommendations. <br>
Risk: The SENTISENSE_API_KEY grants access to SentiSense financial-data lookups. <br>
Mitigation: Keep the key in an environment variable or request header, and do not expose it in query strings or user-facing output. <br>
Risk: Cross-source convergence language may overstate confidence in an investment signal. <br>
Mitigation: Frame convergence as contextual comparison only and avoid suggesting trades solely from that language. <br>


## Reference(s): <br>
- [SentiSense](https://sentisense.ai) <br>
- [SentiSense API Key](https://app.sentisense.ai/get-api-key) <br>
- [ClawHub Skill Listing](https://clawhub.ai/thesentitrader/skills/institutional-13f-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with financial-data summaries and optional curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and read-only network access to app.sentisense.ai.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
