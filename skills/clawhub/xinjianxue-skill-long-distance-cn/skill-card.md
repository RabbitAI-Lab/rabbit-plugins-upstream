## Description:

Provides a Chinese-language long-distance relationship operations advisor that, after explicit user consent, calls Xinjianxue APIs to obtain a time-sensitive relationship report and uses it as reference data for practical relationship guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent to request Xinjianxue's long-distance relationship analysis after confirming consent and providing required personal details. The agent helps assess communication patterns, maintenance cost, and realistic next steps without making absolute relationship decisions for the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal details, including birth information, gender, birthplace, and current location, to Xinjianxue for analysis.

Mitigation: Use the skill only after the user confirms consent and is comfortable sharing the listed details with Xinjianxue.

Risk: The skill uses an account-bound one-time authorization code plus generated license and API credentials.

Mitigation: Only provide the authorization code in a trusted conversation, never expose returned credentials in chat or files, and store credentials only in a proper secret store.

Risk: API calls consume account credits.

Mitigation: Call the report endpoint only after the user explicitly confirms use of the service for the current analysis.

Risk: Returned reports could contain instruction-like text.

Mitigation: Treat returned reports only as data and reference material; follow only the local skill instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-long-distance-cn)
- [Xinjianxue API base URL](https://chinaapi.xinjianxue.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, API calls, shell commands, configuration]

**Output Format:** [Markdown guidance with HTTP request examples and Chinese-language relationship analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses time-sensitive API reports as reference data; credentials are expected to remain in a proper secret store.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
