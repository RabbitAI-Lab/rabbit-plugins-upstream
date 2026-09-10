## Description:

FinXData Chinese Stock Data helps agents query FinXData HTTP APIs for standardized disclosures, stock and market quotes, financial reports, market news, macroeconomic data, FRED series, quota status, and service health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[finxdata](https://clawhub.ai/user/finxdata)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and summarize Chinese market and macroeconomic data from FinXData, including A-share and Hong Kong disclosures, quotes, financials, sector activity, and quota or error status. It is suited for information retrieval and data summarization, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The wrapper can expose FINXDATA_API_KEY in local process arguments when making API-key requests.

Mitigation: Use real keys only on trusted machines, avoid shared or monitored systems where process command lines are visible, and rotate keys after suspected exposure.

Risk: Returned financial data can be incomplete, delayed, empty, or marked with unknown coverage status.

Mitigation: Include returned dates, filters, and coverage status in user-facing summaries, and avoid presenting results as investment advice.

Risk: Account-based and public agent endpoints can be quota-limited or rate-limited.

Mitigation: Use the narrowest necessary query, batch supported codes, avoid repeated refreshes, and respect Retry-After or quota guidance before retrying.

## Reference(s):

- [FinXData Skill Page](https://clawhub.ai/finxdata/skills/finxdata-skill)
- [FinXData API Reference](references/api.md)
- [FinXData Usage Guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require FINXDATA_API_KEY for account-based endpoints or an agent type for public agent endpoints; some calls consume quota or are rate-limited.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
