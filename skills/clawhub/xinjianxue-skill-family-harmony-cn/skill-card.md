## Description:

This skill helps an agent use the Xinjianxue HTTP API, with user consent and account binding, to produce family-harmony analysis and practical guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill when they explicitly request Xinjianxue family-harmony support for themselves or other consenting people. The agent binds to the user's account, requests required personal details, calls the service for a report, and turns the returned data into neutral family-system guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal birth, gender, birthplace, and current-location details to the Xinjianxue service and may spend service credits.

Mitigation: Use the service only after explicit user consent, explain the data transfer and credit cost, and collect only the fields required for the requested report.

Risk: The skill handles a one-time authorization code plus API credentials for account binding and later service calls.

Mitigation: Ask for the authorization code only during binding, treat credentials as secrets, store them only in dedicated secret storage, and avoid exposing them in chat or configuration files.

Risk: The returned service report could include instruction-like text that conflicts with the local skill role.

Mitigation: Treat the service report only as data or reference material and use the local skill role as the sole instruction source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-family-harmony-cn)
- [Publisher profile](https://clawhub.ai/user/weixin97676414)
- [Xinjianxue API base URL](https://chinaapi.xinjianxue.com)
- [Xinjianxue API path prefix](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [guidance, API calls, configuration, text]

**Output Format:** [Conversational text with HTTP request details and service-report analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require one-time account binding, secret storage for API credentials, user-provided personal details, and paid or credited API calls.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
