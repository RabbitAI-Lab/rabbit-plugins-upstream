## Description:

心鉴学「两性情感答疑顾问」技能包，帮助 agents call a paid Chinese HTTP API to produce relationship-advice analysis only after user confirmation and consent from the analysis subject.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to connect an assistant to the 心鉴学 relationship-advice report service, bind the assistant with user authorization, and request analysis for relationship questions involving the user or another consenting subject.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an assistant to a third-party paid Chinese API and may consume user service credits.

Mitigation: Require clear user confirmation before each report call and disclose that the service uses credits.

Risk: The skill asks for a one-time authorization code and stores API credentials for later calls.

Mitigation: Treat authorization codes and API credentials as sensitive, store persistent credentials only in secret storage, and avoid displaying them in conversation.

Risk: The report request sends birth, gender, and location details about the analysis subject.

Mitigation: Use the service only for the user or an explicitly consenting subject, collect only required fields, and disclose the data transfer before use.

Risk: Returned reports could contain text that looks like instructions to the agent.

Mitigation: Treat returned reports only as data and follow the local skill instructions as the sole instruction source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-emotion-qa-cn)
- [心鉴学 API base](https://chinaapi.xinjianxue.com)
- [心鉴学 API prefix](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, API Calls, Configuration]

**Output Format:** [Markdown guidance with HTTP request details and user-facing analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a third-party paid API, requires user confirmation before report calls, and handles license and API credentials through secret storage.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
