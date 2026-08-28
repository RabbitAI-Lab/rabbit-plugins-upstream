## Description:

多旅游平台机票比价与购票决策助手，帮你找到最便宜的机票并告诉你该买还是再等等，含低价日历和降价监控，多旅游平台数据直连。暑期机票省钱攻略。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to compare domestic China flight prices across multiple travel sources, find lower-price dates, and generate buy-or-wait or monitoring guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Route and travel-date queries are sent to external proxy services.

Mitigation: Review the proxy service and data handling before deployment, and avoid sending sensitive or unnecessary personal information in route queries.

Risk: The security evidence reports an embedded proxy credential despite the skill text claiming there are no hardcoded secrets.

Mitigation: Prefer a release that removes the hardcoded token and requires PROXY_TOKEN to be configured explicitly by the deploying agent environment.

Risk: Flight prices and buy-or-wait recommendations can change quickly and do not constitute a booking guarantee.

Mitigation: Treat output as decision support only and verify the final fare, route, and booking terms on the travel provider before purchase.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/smart-flight-buy)
- [Skill homepage](https://rollinggo.store)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON command output with human-facing flight comparison and purchase guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are capped in the script output, calendar scans are capped at 30 days, and monitor output is a JSON request for the host agent to schedule.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
