## Description: <br>
京东精选 helps users search six JD shopping channels for self-operated products using channel, keyword, price, quality, sorting, and pagination filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and shopping assistants use this skill to discover JD self-operated product recommendations across subsidy, new-release, historical-low-price, flash-sale, 9.9 free-shipping, and real-time hot-sale channels. It supports product discovery and comparison, not purchasing or account actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shopping intent, keywords, price filters, and channel choices are sent through the publisher's Tencent Cloud proxy. <br>
Mitigation: Use the skill only when this proxy routing is acceptable, and avoid entering sensitive or personal shopping intent. <br>
Risk: The artifact contains a default proxy token and relies on publisher-operated proxy endpoints. <br>
Mitigation: Prefer publisher-managed secret rotation and documented proxy data handling before high-trust or enterprise use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/jd-selection) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/cn-shopping) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, markdown, guidance] <br>
**Output Format:** [JSON string containing a human-facing summary plus structured product results with names, prices, discounts, shop details, tags, image URLs, and buy URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results are paginated at 50 items per page and may include retry guidance when proxy data is warming or unavailable.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
