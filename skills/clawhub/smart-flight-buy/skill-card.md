## Description:

多旅游平台机票比价与购票决策助手，帮你找到最便宜的机票并告诉你该买还是再等等，含低价日历和降价监控，多旅游平台数据直连。暑期机票省钱攻略。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to compare domestic flight prices, scan low-price travel dates, and receive buy-or-wait guidance. It can also generate a monitoring request for a host agent to check price drops.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Release security evidence reports a reusable backend proxy token in shipped source while the skill claims no hardcoded secret exists.

Mitigation: Rotate the exposed proxy token, remove it from source, and correct the security statement before treating this as a normal benign install.

Risk: Route and travel-date query parameters are sent to the publisher's proxy service.

Mitigation: Install only when users accept that data flow, and avoid entering itinerary details that should not be shared with the publisher-operated proxy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/smart-flight-buy)
- [Publisher profile](https://clawhub.ai/user/travel-skills)
- [Skill homepage](https://rollinggo.store)

## Skill Output:

**Output Type(s):** [JSON, guidance, shell commands]

**Output Format:** [JSON objects with flight results, low-price calendar entries, monitoring requests, and buy-or-wait recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search output is capped at 20 flights; calendar scans are capped at 30 days.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
