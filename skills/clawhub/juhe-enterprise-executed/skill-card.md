## Description:

Queries Juhe's enterprise executed-person records API for current and historical enforcement records using a company name, unified social credit code, registration number, or keyword.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an approved Juhe enterprise account use this skill to look up whether a company has current or historical court execution records and to summarize case numbers, courts, execution amounts, filing dates, and status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends company names, case filters, and the Juhe API key to a paid third-party legal-record service.

Mitigation: Use only with an approved Juhe enterprise account, confirm the exact company before lookup, and treat each query as a billable disclosure to Juhe.

Risk: API keys may be exposed through command-line arguments, local .env files, logs, or copied URLs.

Mitigation: Prefer platform-managed secrets or the JUHE_ENTERPRISE_EXECUTED_KEY environment variable; avoid scripts/.env and --key usage, and never place the key in a URL.

Risk: Returned party identifiers can include sensitive identity numbers.

Mitigation: Keep identity numbers masked in user-facing output and review any downstream sharing of legal-record results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-executed)
- [Juhe enterprise executed-person API documentation](https://www.juhe.cn/docs/api/id/842)
- [Juhe API endpoint](https://apis.juhe.cn/api_credit/query842)
- [Juhe website](https://www.juhe.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, API Calls, Guidance]

**Output Format:** [Plain text or Markdown summary with optional JSON response emitted by the bundled Python script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and JUHE_ENTERPRISE_EXECUTED_KEY; results may include paginated court execution records and masked identity numbers.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
