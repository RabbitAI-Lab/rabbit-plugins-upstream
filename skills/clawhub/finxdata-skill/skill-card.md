## Description:

FinXData Chinese Stock Data helps agents query FinXData financial data APIs for A-share and H-share stock quotes, financial reports, stock graph summaries, market news, dragon-tiger lists, lockup releases, macroeconomic data, anomaly tracking, quota status, update cadence, and service health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[finxdata](https://clawhub.ai/user/finxdata)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and summarize Chinese equity, market, macroeconomic, FRED, quota, and service-status data from FinXData. The skill is intended for financial data lookup and information organization, not deterministic investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial query terms, stock codes, and an optional FinXData API key are sent to the configured FinXData service.

Mitigation: Install only when this data sharing is acceptable, keep FINXDATA_BASE_URL pointed at a trusted endpoint, and avoid exposing API keys in shared logs or prompts.

Risk: Changing FINXDATA_BASE_URL can redirect API-key-bearing requests to another compatible server.

Mitigation: Use the default FinXData endpoint or a vetted endpoint, and review environment configuration before running queries.

Risk: Financial data summaries can be stale or mistaken for investment advice.

Mitigation: Treat results as information retrieval, include returned dates or report periods where relevant, and avoid deterministic buy or sell recommendations.

## Reference(s):

- [FinXData API Reference](references/api.md)
- [FinXData Usage Guide](references/usage.md)
- [ClawHub Skill Page](https://clawhub.ai/finxdata/skills/finxdata-skill)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON from the FinXData wrapper, with concise natural-language summaries for users.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include FinXData response confidence, data dates or report periods, quota details, retry status, and rate-limit guidance.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
