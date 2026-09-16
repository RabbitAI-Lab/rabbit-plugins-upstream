## Description:

途牛+同程+美团+RollingGo五平台直飞航班实时比价，按航班号自动匹配同一航班跨平台报价，一次出结果含预订链接。暑期机票比价、出行省钱。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel assistants use this skill to compare direct mainland China flight prices across Tuniu, Tongcheng, Meituan, and RollingGo for a specified city pair and date. It returns matched flight options with platform-specific prices, timing details, caveats, and booking links.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Flight search details are sent to the publisher's Tencent Cloud proxy.

Mitigation: Install only when this data flow is acceptable, and avoid submitting sensitive itinerary details.

Risk: The artifact embeds a shared proxy token in source code.

Mitigation: Move the token to managed secret storage or environment configuration before production use and rotate the exposed token.

Risk: Prices and booking links from external travel platforms are unverified and may change or omit fees.

Mitigation: Verify fares, taxes, and booking domains on the destination platform before purchase.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/china-flight-price-compare)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with flight-price comparisons, caveats, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires fromCity, toCity, and date; optional time preference and sort mode affect displayed results.]

## Skill Version(s):

4.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
