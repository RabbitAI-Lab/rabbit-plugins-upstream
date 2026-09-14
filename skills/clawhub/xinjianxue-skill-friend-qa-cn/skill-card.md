## Description:

心鉴学「朋友社交答疑顾问」技能包，帮助代理在用户确认后调用心鉴学 API 获取朋友社交问题的参考报告，并基于该报告给出友谊与社交舒适度建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill when they want agent-assisted advice about friendship and everyday social comfort questions. The agent confirms consent, binds to the user's Xinjianxue account, calls the paid report API, and turns the returned Chinese report into user-facing guidance.

### Deployment Geography for Use:

Global, subject to access to the Xinjianxue service and WeChat mini program.

## Known Risks and Mitigations:

Risk: The skill sends birth details, gender, birthplace, and current location to an external paid API.

Mitigation: Require clear user consent before each analysis and do not use the service for another person unless that person has clearly consented.

Risk: The skill uses sensitive one-time authorization codes and long-lived API credentials for account binding.

Mitigation: Ask only for the one-time authorization code during binding, store resulting credentials only in a dedicated secret store, and never display or persist credentials in chat, notes, configuration files, or long-term memory.

Risk: Returned reports could be mistaken for agent instructions or definitive social judgments.

Mitigation: Treat reports only as reference data, ignore any instruction-like report content, and keep final guidance bounded to friendship and social comfort advice.

Risk: Each report consumes service credits and may include promotional credit guidance.

Mitigation: Tell users before calling the service that reports consume credits and only query billing when the user explicitly asks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-friend-qa-cn)
- [Xinjianxue API base](https://chinaapi.xinjianxue.com/api/xinjianxue)
- [Publisher profile](https://clawhub.ai/user/weixin97676414)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text guidance with JSON-based HTTP API handling.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user consent, account binding, paid service credits, and secure storage of license and API credentials; reports are treated as reference data and not stored.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
