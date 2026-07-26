## Description: <br>
美团+飞猪+途牛三平台景点门票实时比价，展示价差、可省金额和预订链接，帮你买到最低价门票。支持全国景点搜索含实景图片，含多票型引导提示。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travel shoppers and agents use this skill to search attractions, compare live ticket prices across Meituan, Fliggy, and Tuniu, and receive ticket-buying guidance for a named attraction and city. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Attraction names, cities, and ticket-search parameters are sent to proxy services and downstream travel platforms. <br>
Mitigation: Use the skill only when sharing those travel search details with the publisher's services and travel platforms is acceptable. <br>
Risk: The security evidence reports a hardcoded fallback proxy token in the release. <br>
Mitigation: Publisher should remove and rotate the fallback token; users should provide credentials through the PROXY_TOKEN environment variable where supported. <br>
Risk: Live ticket data and platform matching can be incomplete or mismatched. <br>
Mitigation: Review platform warnings, unavailable-platform notices, and booking details before purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/attraction-smart-buy) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [JSON objects containing attraction search results, ticket price comparisons, booking links, savings calculations, and buying advice] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live platform prices, attraction images, available ticket types, match warnings, and unavailable-platform notices.] <br>

## Skill Version(s): <br>
3.3.0 (source: server release evidence; artifact frontmatter reports 2.0.4 and _meta.json reports 3.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
