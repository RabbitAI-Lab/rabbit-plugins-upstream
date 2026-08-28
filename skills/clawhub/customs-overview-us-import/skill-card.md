## Description:

Queries UpKuaJing US import transaction statistics grouped by state or city, including import records, container counts, recent 90-day activity, and cursor-based pagination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Export teams, logistics analysts, and trade professionals use this skill to monitor US import activity, compare state-level or city-level container flow, and support market-entry analysis from customs import data.

### Deployment Geography for Use:

Global; the queried trade data is specific to US import activity.

## Known Risks and Mitigations:

Risk: The skill handles an UpKuaJing API key that may be stored in ~/.upkuajing/.env.

Mitigation: Treat the API key as a secret, avoid printing or sharing the env file, and restrict access to the account credentials.

Risk: US import-statistics queries can incur fees, and top-up flows can generate payment URLs.

Mitigation: Confirm fee-bearing actions with the user before execution and use the documented pricing lookup instead of estimating costs.

Risk: Error reporting can send diagnostic context to the platform.

Mitigation: Submit error reports only after user confirmation and avoid including sensitive query or account details in diagnostic context.

Risk: Normal API calls perform an update check that writes a version cache under the user's home directory.

Mitigation: Review this network and local-cache behavior before installing or running the skill in controlled environments.

## Reference(s):

- [US Import API Reference](references/customs-overview-us-import-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses with concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paginated responses may include a cursor, fee information, and a requestId.]

## Skill Version(s):

1.0.1 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
