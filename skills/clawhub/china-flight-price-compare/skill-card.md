## Description:

飞猪+途牛+同程+美团+RollingGo五平台直飞航班实时比价，按航班号自动匹配同一航班跨平台报价，一次出结果含预订链接。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel assistants use this skill to compare direct domestic flight prices across multiple Chinese travel platforms for a specified route and departure date. It helps identify lower fares, platform price differences, flight times, and booking links before the user completes purchase on an external platform.

### Deployment Geography for Use:

Global use for China mainland domestic flight searches

## Known Risks and Mitigations:

Risk: Flight-search details such as origin city, destination city, date, and filters are sent through the publisher's cloud proxy and onward to travel platforms.

Mitigation: Use the skill only when that data flow is acceptable for the user or organization, and avoid entering sensitive travel details that should not leave the local environment.

Risk: The proxy endpoint and token are built into the script rather than fully configurable by the user.

Mitigation: Review the configured endpoint before deployment and monitor publisher updates when proxy routing or credential handling requirements change.

Risk: Flight prices and booking availability can change after the skill returns results.

Mitigation: Confirm price, taxes, cabin terms, and availability on the destination booking platform before purchase.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/china-flight-price-compare)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown flight comparison summary with prices, source labels, warnings, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns direct-flight comparisons for the requested route and date; prices are time-sensitive and may vary on booking platforms.]

## Skill Version(s):

4.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
