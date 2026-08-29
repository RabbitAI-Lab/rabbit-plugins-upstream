## Description:

FinXData helps agents query FinXData financial data APIs for A-share and H-share stocks, market prices, financial reports, market news, dragon-tiger lists, lockup calendars, macroeconomic and FRED data, quota status, update cadence, and error handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qiuqp](https://clawhub.ai/user/qiuqp)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to retrieve and summarize FinXData financial datasets, including stock quotes, company and market summaries, financial reports, macroeconomic indicators, API quota status, and service error explanations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial, market, macroeconomic, quota, and diagnostic queries may be sent to FinXData along with an API key or agent-type header.

Mitigation: Use a trusted FINXDATA_BASE_URL, scope the API key to this service, avoid sending unnecessary sensitive context, and rely on the skill's narrow commands for the minimum needed request.

Risk: Returned financial data can be incomplete, stale, rate-limited, or mistaken for investment advice.

Mitigation: Treat outputs as informational, include the returned date or reporting period when summarizing, avoid deterministic buy or sell recommendations, and follow quota or Retry-After guidance before retrying.

## Reference(s):

- [FinXData Skill Page](https://clawhub.ai/qiuqp/skills/finxdata)
- [FinXData API Reference](references/api.md)
- [FinXData Usage Guide](references/usage.md)
- [FinXData API Service](https://api.finxdata.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON from FinXData API calls, with agent-facing summaries commonly rendered as Markdown or concise text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include returned financial data, confidence labels, dates, quota fields, retry guidance, and API error explanations; results are informational and not investment advice.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
