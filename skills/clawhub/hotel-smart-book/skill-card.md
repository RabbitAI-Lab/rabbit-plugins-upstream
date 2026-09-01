## Description:

多旅游平台酒店比价与订房决策助手，帮你找到最便宜的酒店并告诉你该订还是再等等，含低价日历和订房建议，多旅游平台数据直连。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to compare hotel prices across travel platforms, scan low-price date ranges, and get booking-timing advice before following a booking link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel search details are sent to the publisher's proxy service and then to travel-platform APIs.

Mitigation: Use only the travel details needed for search, avoid adding unrelated sensitive information, and review whether this data flow fits the user's privacy expectations.

Risk: The artifact includes an embedded proxy token, which is noted by the security summary as a user-limited concern.

Mitigation: Treat the token as publisher infrastructure, avoid reusing it outside the skill, and rotate or revoke it if the publisher observes misuse.

Risk: Booking advice, prices, policies, and booking links may change after the skill returns results.

Mitigation: Verify final prices, cancellation policies, room details, and platform terms on the booking platform before purchasing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/hotel-smart-book)
- [Publisher profile](https://clawhub.ai/user/travel-skills)
- [Skill homepage](https://rollinggo.store)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON responses containing hotel results, price calendar entries, booking links, and booking advice]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search parameters include city, check-in and check-out dates, optional keyword, hotel name, adults, rooms, nights, and scan days.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
