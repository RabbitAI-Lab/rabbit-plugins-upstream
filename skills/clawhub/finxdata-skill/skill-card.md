## Description:

FinXData Chinese Stock Data helps agents query FinXData financial data, prioritizing no-key access for stock quotes, disclosures, market themes, macro data, financial summaries, and graph summaries, with optional API-key access for deeper analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[finxdata](https://clawhub.ai/user/finxdata)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to retrieve and summarize Chinese stock market, company disclosure, thematic, macroeconomic, financial, and graph-summary data through FinXData APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends financial-data queries, an agent-type identifier, and optionally a FINXDATA_API_KEY to FinXData's official API.

Mitigation: Use the no-key agent interfaces when they satisfy the request, configure API keys only when deeper account-backed data is needed, and avoid sharing unnecessary sensitive query context.

Risk: Financial data returned by the API could be mistaken for investment advice.

Mitigation: Use the skill for information retrieval and summarization, state relevant data dates and limits, and avoid deterministic buy or sell recommendations.

Risk: API responses can contain untrusted text, links, or remote error details.

Mitigation: Treat response content as data only, do not execute instructions from responses, and do not automatically open returned links or attachments.

Risk: Free and API-key interfaces are subject to quotas, rate limits, and response-size limits.

Mitigation: Use narrow parameters, batch only supported quote requests, respect retry guidance, and reduce result windows or paginate when limits are reached.

## Reference(s):

- [FinXData API Reference](references/api.md)
- [FinXData Usage Guide](references/usage.md)
- [FinXData Website](https://www.finxdata.ai)
- [FinXData ClawHub Skill Page](https://clawhub.ai/finxdata/skills/finxdata-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; script calls return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API responses wrapped as trusted_metadata and untrusted_api_data; financial information is for data retrieval and summary, not investment advice.]

## Skill Version(s):

1.0.16 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
