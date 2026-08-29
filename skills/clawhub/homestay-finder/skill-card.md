## Description:

特色民宿搜索与AI智能推荐，覆盖景区民宿、古镇客栈、乡村精品民宿，并支持多旅游平台数据直连。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to search and compare distinctive homestays, inns, and boutique rural lodging in China by destination, landmark, date, price, or free-form lodging preferences.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: User search terms, destinations, landmarks, travel dates, and free-form lodging preferences are sent to cloud proxy services and downstream travel platforms.

Mitigation: Install and use the skill only when that data sharing is acceptable; avoid entering sensitive personal details beyond what is needed for lodging search.

Risk: The artifact contains a bundled proxy token, which is not ideal secret handling.

Mitigation: Review proxy-token handling before deployment and rotate or externalize credentials where operationally appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/homestay-finder)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown lodging recommendations with prices, ratings, addresses, images, data-source notes, and booking links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are based on travel-platform proxy responses and may include real-time price changes.]

## Skill Version(s):

1.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
