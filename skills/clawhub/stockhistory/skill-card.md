## Description:

Queries JisuAPI for historical daily stock prices, stock lists, and stock details by code and optional date range for K-line and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve JisuAPI stock history, list, and detail data for Chinese stock lookup, K-line preparation, and trend summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The JisuAPI app key and stock lookup parameters are sent to JisuAPI over HTTPS.

Mitigation: Use a scoped or rotatable API key where possible, store it in JISU_API_KEY, and avoid entering sensitive information beyond stock codes and date ranges.

Risk: Returned market data may be unavailable, delayed, or rejected by the upstream API for invalid stock codes or date ranges.

Mitigation: Check structured error responses before analysis and present failed lookups as unavailable data rather than investment conclusions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jisuapi/skills/stockhistory)
- [JisuAPI Stock Historical Data API](https://www.jisuapi.com/api/stockhistory/)
- [JisuAPI Website](https://www.jisuapi.com/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON API results and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and JISU_API_KEY; calls JisuAPI over HTTPS and returns stock data or structured error objects.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
