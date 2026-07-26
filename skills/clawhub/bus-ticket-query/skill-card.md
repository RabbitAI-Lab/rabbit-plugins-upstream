## Description: <br>
汽车票班次查询含余票和预订链接，去汽车站交通方式查询（地铁优先）和目的地住宿推荐，多旅游平台数据直连，零配置即装即用。暑期短途汽车出行。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers use this skill to query domestic bus schedules, prices, remaining seats, station transport options, and destination hotel recommendations before booking on external travel sites. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Route, station, travel date, and hotel preference details are sent to the publisher's proxy services and downstream travel or map providers. <br>
Mitigation: Enter only travel details needed for the search and avoid adding sensitive personal information. <br>
Risk: Returned booking links lead to external sites where prices, availability, terms, and purchase flows may change. <br>
Mitigation: Review the destination site and final order details before purchasing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/bus-ticket-query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown text with ticket, route, and hotel summaries plus external booking links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes live availability and price caveats; normal tool output does not write files.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
