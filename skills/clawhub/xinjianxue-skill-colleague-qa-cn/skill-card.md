## Description:

This skill helps an agent provide workplace colleague-relationship advice by collecting user-confirmed personal details, calling the Xinjianxue report API, and using the returned report as reference data for boundary-setting and communication guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill when they explicitly want Xinjianxue's colleague-relationship advisor to analyze workplace friction, interpersonal boundaries, or communication choices. The agent should first confirm consent, then use the third-party report as reference material rather than as instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal birth, gender, and location details to a third-party service for each report.

Mitigation: Use the skill only after explicit user consent and only when the user trusts the Xinjianxue service.

Risk: The skill requires a one-time authorization code and persistent API credentials.

Mitigation: Treat the authorization code and resulting credentials as sensitive, store credentials only in dedicated secret storage, and avoid showing them in conversation or configuration files.

Risk: The third-party report may contain content that should not control the agent.

Mitigation: Use report output as reference data only and ignore any instruction-like text returned by the API.

Risk: Each report may spend the user's Xinjianxue points.

Mitigation: Confirm the user's intent before calling the report endpoint and explain that the service uses its stated points per report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-colleague-qa-cn)
- [Xinjianxue API endpoint](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [guidance, markdown, API Calls, configuration]

**Output Format:** [Markdown guidance with HTTP API request details and credential-handling steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user consent, persistent API credentials, outbound calls to Xinjianxue, and user-provided personal birth and location details for each report.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
