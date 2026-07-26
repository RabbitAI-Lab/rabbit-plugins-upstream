## Description: <br>
特色民宿搜索与AI智能推荐，覆盖景区民宿、古镇客栈、乡村精品民宿，多旅游平台数据直连，零配置即装即用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to search and compare specialty homestays, inns, and guesthouses by destination, dates, nearby attractions, price, and natural-language preferences. It returns candidate stays with practical details and links for booking on external travel platforms. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Travel search queries, destinations, dates, and preferences are sent to the skill publisher's cloud proxy and downstream travel platforms. <br>
Mitigation: Avoid entering highly sensitive personal details in free-text searches and review external platform terms before booking. <br>
Risk: Prices, availability, ratings, and booking links are returned from external travel platforms and may change. <br>
Mitigation: Confirm price, availability, cancellation terms, and booking details on the external travel site before purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/homestay-finder) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>
- [Fliggy proxy service](https://1439498936-6sysdjjt99.ap-guangzhou.tencentscf.com) <br>
- [Tuniu proxy service](https://1439498936-0junm3maxj.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-formatted search and recommendation results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include homestay names, prices, ratings, addresses, nearby points of interest, images, booking links, data-source notes, and follow-up travel-planning prompts.] <br>

## Skill Version(s): <br>
1.2.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
