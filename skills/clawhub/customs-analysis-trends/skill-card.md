## Description:

Query monthly import and export trade trends for a specified HS code, returning breakdowns with trade counts, quantities, weights, amounts, buyer counts, and seller counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Trade analysts, supply chain managers, and market researchers use this skill to analyze recent import and export trends for specific HS codes, compare import versus export activity, and monitor seasonal or market dynamics across customs data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to an UpKuaJing API key.

Mitigation: Provide the key through a secure environment secret when possible, avoid displaying ~/.upkuajing/.env, and restrict access to environments that need the API.

Risk: Trend queries use paid UpKuaJing API calls.

Mitigation: Confirm current pricing and obtain explicit user approval before running fee-incurring queries.

Risk: Optional error reports can include prompts, business-sensitive queries, API responses, or credentials if the report context is not reviewed.

Mitigation: Review and redact the error report payload before sending it, and send reports only after user confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-trends)
- [Publisher profile](https://clawhub.ai/user/upkuajing)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html)
- [Trends API reference](references/customs-analysis-trends-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Natural language guidance with shell commands and JSON API output summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; trend queries return monthly export and import data plus fee and request identifiers.]

## Skill Version(s):

1.0.1 (source: server release evidence and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
