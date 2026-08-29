## Description:

Query company customs trade statistics by HS code dimension to analyze HS code distribution, trade volume breakdown, and monthly trade trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trade analysts use this skill to query UpKuaJing customs data for a company's HS code distribution, monthly trade trends, and product-category trade concentration. It is intended for paid API-backed customs trade analysis using a company ID and buyer or supplier role.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid UpKuaJing API queries can incur account fees.

Mitigation: Confirm current pricing and obtain explicit user approval before running fee-bearing query or top-up commands.

Risk: The skill stores and reads UPKUAJING_API_KEY from ~/.upkuajing/.env.

Mitigation: Use a dedicated API key with limited exposure, protect the local env file, and rotate the key if it is shared or exposed.

Risk: Error reports can transmit request context to the platform.

Mitigation: Send error reports only after user confirmation and exclude sensitive business details unless they are required for troubleshooting.

Risk: The scripts perform automatic version-check traffic and write a local version cache.

Mitigation: Review this behavior before deployment in environments with strict network egress or local persistence policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-hscode-stats)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html)
- [Company HS Code Trade Statistics API](artifact/references/customs-company-hscode-stats-api.md)
- [Skill Error Report API](artifact/references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; query responses include customs statistics, fee information, and request identifiers.]

## Skill Version(s):

1.0.1 (source: evidence.release.version and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
