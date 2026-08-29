## Description:

一次调用完成搜索与推荐，含预订链接和退改政策解读，自动识别商务、亲子、度假、背包等场景并按价格档位推荐全球酒店。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to search hotels, compare price tiers, and produce concise recommendations with booking links and cancellation-policy summaries for business, family, vacation, budget, or general travel scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel searches, dates, occupancy, and free-text travel details are sent to a fixed third-party cloud proxy using an embedded token.

Mitigation: Review the data flow before installing, disclose the proxy route to users, and avoid entering sensitive travel details unless that routing is acceptable.

Risk: Users have limited control over the fixed proxy endpoint and embedded token used by the skill.

Mitigation: Install only after security review and apply organizational controls for network access, monitoring, or allowed use cases where needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/global-hotel-search-recommend)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown-style hotel recommendations with prices, booking links, hotel details, and cancellation-policy notes when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hotel image links and fallback-search notices; prices and availability can change at booking time.]

## Skill Version(s):

1.6.6 (source: server release evidence; artifact frontmatter reports 1.6.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
