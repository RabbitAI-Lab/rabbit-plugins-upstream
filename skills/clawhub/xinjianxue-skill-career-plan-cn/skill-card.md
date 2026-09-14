## Description:

Provides a Chinese career-planning consultant workflow that obtains consent, binds a Xinjianxue account, calls the Xinjianxue report API, and uses the report as reference data for career-path guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent to request career-planning analysis for themselves or explicitly consenting people. The agent gathers required profile data, calls Xinjianxue's paid report API, and turns the returned report into practical career-path guidance without treating the report as instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends birth date or time, gender, birth location, current location, and a one-time authorization code to a third-party paid service.

Mitigation: Confirm user consent before use, verify the official domain, disclose credit consumption, and keep the license and API key only in secure credential storage.

Risk: One-time authorization codes and service credentials can bind or expose the user's service account.

Mitigation: Request only the one-time authorization code during binding, do not display stored credentials, and send account or binding problems to service support instead of retrying blindly.

Risk: Reports returned by the service could include text that looks like instructions.

Mitigation: Treat returned report content strictly as reference data and follow only the local skill guidance when producing the final answer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-career-plan-cn)
- [Xinjianxue API base](https://chinaapi.xinjianxue.com)
- [Xinjianxue API namespace](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with API request details and credential-handling instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured career-planning analysis based on third-party report data; credentials must be kept in secure storage.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
