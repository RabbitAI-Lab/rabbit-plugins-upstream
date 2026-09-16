## Description:

途牛全品类旅行查询预订技能，酒店/机票/火车票/景点门票/邮轮/度假17个工具一站式服务，含图片展示和跨品类推荐。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travel users and agents use this skill to search hotels, flights, trains, scenic tickets, cruises, and vacation packages, compare results, and initiate supported bookings after providing the required details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booking and cancellation tools can send personal booking data through a proxy with weak endpoint checks.

Mitigation: Use an exact HTTPS PROXY_URL and require explicit user confirmation before booking, cancellation, or submission of identity information.

Risk: The security scan reports a hard-coded fallback token.

Mitigation: Require a user-provided PROXY_TOKEN and do not rely on the bundled fallback token.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/tuniu-travel-assistant)
- [ClawHub publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [JSON responses containing formatted Markdown result summaries, error messages, or booking and order data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hotel and cruise results may include Markdown image links; booking and cancellation actions require user-provided order or identity details.]

## Skill Version(s):

2.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
