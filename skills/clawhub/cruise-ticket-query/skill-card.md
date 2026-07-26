## Description: <br>
长江三峡游轮和城市游船船票查询，含价格、航线方向和退改政策，附带去码头交通（地铁优先）、景点门票和住宿推荐，多旅游平台数据直连，零配置即装即用。暑假邮轮票查询比价，多平台对比省钱 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel planners use this skill to compare domestic river and city cruise tickets, plan transport to piers, and find nearby attractions or hotels before booking on linked travel platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send travel locations, route queries, and hotel-search text to external proxy and map services. <br>
Mitigation: Use it only when that data sharing is acceptable, avoid entering sensitive personal details, and review the publisher's data-flow disclosures before installation. <br>
Risk: The artifact includes an embedded proxy token. <br>
Mitigation: The publisher should remove embedded secrets, rotate exposed tokens, and use runtime configuration for service credentials. <br>
Risk: The security summary says external data sharing is under-disclosed. <br>
Mitigation: The publisher should document the network data flows and external services clearly in release materials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/cruise-ticket-query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown text with prices, route details, policies, recommendations, and booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results depend on external travel and map services; prices, availability, routes, and policies can change.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
