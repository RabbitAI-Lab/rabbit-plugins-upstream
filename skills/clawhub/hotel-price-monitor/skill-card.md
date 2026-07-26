## Description: <br>
酒店降价监控与多平台比价助手，同时搜索多个旅游平台实时价格帮你比价省钱，支持按酒店名称精确比价、按城市搜索酒店列表、创建降价监控任务，多旅游平台数据直连。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-shopping agents use this skill to search hotels by city and date, compare live prices across travel platforms for a named hotel, and prepare host-agent price watch requests for selected stays. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel names, cities, stay dates, and related search details are sent to the skill's proxy service for live pricing. <br>
Mitigation: Use the skill only when the user is comfortable sharing those travel search details with the proxy service. <br>
Risk: Some booking links may use commission channels, so link ordering or neutrality may require user attention. <br>
Mitigation: Present platform, price, cancellation policy, and link information transparently so the user can choose where to book. <br>
Risk: Persistent price monitoring depends on host-agent support and is not guaranteed by the skill alone. <br>
Mitigation: Confirm that the host agent has accepted and scheduled the monitoring request before promising ongoing alerts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/hotel-price-monitor) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON command output from hotel search and comparison scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hotel names, prices, cancellation-policy notes, booking links, and structured monitoring-request details for the host agent.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
