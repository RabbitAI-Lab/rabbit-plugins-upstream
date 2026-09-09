## Description:

FinXData helps agents query standardized financial announcements, market prices, company data, macroeconomic datasets, FRED series, quotas, and service status through the FinXData API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qiuqp](https://clawhub.ai/user/qiuqp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve and summarize FinXData financial API results, including A/H-share announcements, quotes, financial statements, market tracking, macroeconomic data, FRED series, and quota or error status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A modified FINXDATA_BASE_URL can route credentialed requests away from the default FinXData API service.

Mitigation: Keep FINXDATA_BASE_URL unset or set only to https://api.finxdata.ai, and avoid inherited compatibility aliases from untrusted shell profiles or CI settings.

Risk: API-key backed requests are credentialed network calls with quota and privacy impact.

Mitigation: Use the narrowest required query, avoid exposing the key in prompts or logs, and check quota only when quota status or rate-limit handling is needed.

Risk: Financial API results may be incomplete, delayed, rate-limited, or unsuitable as standalone investment advice.

Mitigation: Report returned dates, confidence, coverage status, and errors clearly; summarize information without issuing deterministic buy or sell recommendations.

## Reference(s):

- [FinXData API reference](references/api.md)
- [FinXData usage guide](references/usage.md)
- [FinXData API service](https://api.finxdata.ai)
- [FinXData ClawHub skill page](https://clawhub.ai/qiuqp/skills/finxdata)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and JSON API responses from shell command execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require FINXDATA_API_KEY for account-backed endpoints or FINXDATA_AGENT_TYPE for public agent endpoints.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
