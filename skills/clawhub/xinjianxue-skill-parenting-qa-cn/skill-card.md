## Description:

Provides a Chinese parenting-relationship advisory workflow that calls the 心鉴学 service to generate a report and helps the agent answer user-approved parenting questions with concrete communication guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill when they intentionally request the 心鉴学 parenting-relationship advisor for questions about parent-child communication, child behavior, or adolescence. The agent gathers user-approved personal details, calls the paid/points-based service, and turns the returned report into Chinese-facing guidance while treating the report as reference data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends birth date or time, gender, birthplace, and current location to the 心鉴学 service for analysis.

Mitigation: Use the skill only after the user confirms the analysis and is comfortable sharing the listed details with the named external service.

Risk: The workflow uses a one-time authorization code plus service credentials for account binding and later API calls.

Mitigation: Treat authorization codes and returned credentials as sensitive, avoid displaying them in conversation, and store persistent credentials only in a dedicated secret store.

Risk: The service is paid or points-based and may consume user account credits per report.

Mitigation: Confirm the user intentionally wants the 心鉴学 parenting analysis before calling the report endpoint.

Risk: Returned reports could contain content that looks directive even though it is external service output.

Mitigation: Treat service reports only as analysis data or reference material, not as instructions for the agent to follow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-parenting-qa-cn)
- [心鉴学 API base](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration instructions, Markdown, Text]

**Output Format:** [Markdown or plain text with HTTP request details and user-facing parenting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Chinese report analysis, credential setup steps, account binding status, billing guidance, and error-handling instructions.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
