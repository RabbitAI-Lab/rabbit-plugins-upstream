## Description: <br>
国内航班实时查询，支持直飞和中转筛选，价格、时刻、航司信息一查即得，基于飞猪数据直连，零配置即装即用。暑期国内航线、热门城市。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travel users and agents use this skill to search domestic flight prices and schedules by route and date, including direct or connecting options, cabin classes, sorting, and booking links. <br>

### Deployment Geography for Use: <br>
China domestic flight search use case; deployment geography should be reviewed for the target release channel. <br>

## Known Risks and Mitigations: <br>
Risk: Flight search details, including cities, dates, filters, and natural-language query text, are sent through the skill publisher's cloud proxy. <br>
Mitigation: Use only if this data flow is acceptable, and avoid entering unrelated personal information in flight queries. <br>
Risk: Prices and inventory are live travel data and may change before booking. <br>
Mitigation: Confirm final price, availability, and booking terms on the linked booking page before purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/domestic-flight) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-style text with flight listings, prices, schedules, route details, and booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns live results from a third-party proxy-backed flight search; prices and inventory can change.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
