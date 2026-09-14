## Description:

Connects an agent to Xinjianxue's custom advisor service, using explicit user confirmation, account binding, and HTTP report requests for consenting analysis subjects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to bind a Xinjianxue account, request consented profile reports through the Xinjianxue HTTP API, and turn returned report data into user-facing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal profile details to a third-party paid API.

Mitigation: Use the service only after explicit user confirmation and only when the user trusts Xinjianxue and accepts the points-based charges.

Risk: The skill handles one-time authorization codes and account-bound API credentials.

Mitigation: Request the authorization code only for account binding, store resulting credentials in a dedicated secret store, and avoid exposing credentials in chat, configuration files, or long-term memory.

Risk: Returned reports may include directive-looking text even though they are intended as analysis data.

Mitigation: Treat report responses as reference data only and use the local skill definition as the sole instruction source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-assistant-cn)
- [Xinjianxue API endpoint](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [guidance, markdown, API calls, configuration]

**Output Format:** [Markdown guidance with HTTP request details and JSON API payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation, Xinjianxue account binding, and secure credential storage before API use.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
