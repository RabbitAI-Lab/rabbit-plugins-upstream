## Description:

先浏览再比价，飞猪+途牛+同程+美团+RollingGo五源并发比价，找出全网最低价。含评分、距离、早餐、取消政策等详细信息。暑期出行多平台比价，轻松找到最划算的住宿方案

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to browse hotels in Chinese cities, compare prices across multiple travel platforms, and review hotel details such as ratings, distance, breakfast, cancellation terms, and booking links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel search details such as city, dates, hotel names, POIs, and filters are sent through the publisher's cloud proxy and then to travel platforms.

Mitigation: Avoid sensitive travel plans unless the user is comfortable with that data flow; the publisher should document destination and retention controls.

Risk: Server security evidence reports a hardcoded authenticated cloud proxy token.

Mitigation: The publisher should remove the embedded token, rotate it, and use a documented secret-management approach before broad deployment.

Risk: Hotel prices and platform availability can change or be incomplete because external travel platforms may time out or return fewer results.

Mitigation: Treat returned prices as decision support and confirm price, room type, cancellation policy, and availability on the booking platform before purchase.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/china-hotel-price-compare)
- [ClawHub publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style hotel browsing and price-comparison results with prices, hotel details, warnings, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include live travel-platform prices, hotel images, platform availability notes, and reminders that prices can change before booking.]

## Skill Version(s):

4.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
