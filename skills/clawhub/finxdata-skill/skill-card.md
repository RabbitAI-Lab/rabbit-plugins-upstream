## Description: <br>
Helps agents query FinXData financial-data APIs for market prices, stock data, financial reports, news, macroeconomic data, quota status, and service health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[finxdata](https://clawhub.ai/user/finxdata) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and end users use this skill to retrieve and summarize FinXData financial data, including stock quotes, market sectors, company reports, macroeconomic indicators, FRED series, tracking feeds, quota status, and API health. It is best suited for information retrieval and structured summaries, not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated commands send FINXDATA_API_KEY to the configured FinXData endpoint. <br>
Mitigation: Configure FINXDATA_API_KEY deliberately and keep FINXDATA_BASE_URL on the trusted FinXData service unless a trusted alternative endpoint is required. <br>
Risk: Financial queries may be transmitted to FinXData and returned data may be time-sensitive. <br>
Mitigation: Use the narrowest query needed, summarize the returned dates and data freshness, and avoid presenting the output as investment advice. <br>
Risk: Repeated API calls can consume quota or trigger rate limits. <br>
Mitigation: Batch supported quote and price requests, reuse results within a task, respect 429 responses, and consult quota status only when needed. <br>


## Reference(s): <br>
- [FinXData API reference](references/api.md) <br>
- [FinXData usage guide](references/usage.md) <br>
- [ClawHub skill page](https://clawhub.ai/finxdata/skills/finxdata-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries, JSON API responses, shell commands, and environment-variable configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include concise explanations of API errors, quota status, retry posture, and data freshness.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
