## Description: <br>
FinXData helps agents query FinXData financial data APIs for stock quotes, market themes, financial reports, news tracking, Dragon-Tiger lists, lockup calendars, macroeconomic data, FRED data, quota status, update cadence, API key setup, error handling, and service health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qiuqp](https://clawhub.ai/user/qiuqp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve and summarize FinXData financial datasets through a bundled HTTP wrapper, including authenticated account APIs and agent public endpoints. It is intended for data lookup and information organization, not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A FinXData API key could be exposed if copied into shared prompts, logs, or untrusted environments. <br>
Mitigation: Keep FINXDATA_API_KEY private, use environment variables for configuration, and avoid sharing command output that may contain credentials. <br>
Risk: Changing FINXDATA_BASE_URL can redirect requests to an untrusted service. <br>
Mitigation: Leave FINXDATA_BASE_URL unset for the default FinXData endpoint unless the replacement endpoint is trusted. <br>
Risk: Financial API results may be stale, incomplete, or misread as investment advice. <br>
Mitigation: Summarize returned dates, report periods, and data status, and present conclusions as information organization rather than buy or sell recommendations. <br>
Risk: Quota, rate limit, network, or service errors can interrupt data retrieval. <br>
Mitigation: Use the quota command for account limits, reduce batch size or call frequency when limited, and retry later for temporary service or network failures. <br>


## Reference(s): <br>
- [FinXData API reference](references/api.md) <br>
- [FinXData usage guide](references/usage.md) <br>
- [FinXData API service endpoint](https://api.finxdata.ai) <br>
- [ClawHub skill page](https://clawhub.ai/qiuqp/skills/finxdata) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; API responses are JSON and often contain Markdown data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Authenticated endpoints use FINXDATA_API_KEY; agent public endpoints require an agent type and may be rate limited.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
