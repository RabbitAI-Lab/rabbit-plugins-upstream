## Description: <br>
搜索美团全国连锁品牌酒店特价套餐，支持按城市和品牌筛选，并按折扣或价格排序返回实时套餐信息和预订链接。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers use this skill to find Meituan hotel package deals by city, brand, discount, or price before completing booking on Meituan. It is useful for comparing limited domestic hotel deal results when the user is comfortable using Meituan links. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Hotel search terms such as city, brand, and sort order are sent to the skill's Tencent Cloud proxy. <br>
Mitigation: Use the skill only when sharing those limited search terms with the proxy is acceptable; avoid entering sensitive personal or booking details. <br>
Risk: The skill returns Meituan booking links and does not complete or validate purchases itself. <br>
Mitigation: Confirm price, inventory, terms, and cancellation details on Meituan before booking. <br>
Risk: The skill is focused on Meituan hotel deals and is not a neutral all-provider hotel comparison tool. <br>
Mitigation: Use additional sources when a broader market comparison or provider-neutral recommendation is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/meituan-hotel-deals) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-formatted hotel deal list with images, prices, city and brand details, validity information, and booking links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns up to 20 hotel package deals per request; prices and inventory may change on the Meituan booking page.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
