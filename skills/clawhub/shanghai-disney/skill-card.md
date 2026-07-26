## Description: <br>
上海迪士尼乐园游园助手，提供排队预估、路线规划、演出时间、餐厅推荐、门票价格和营业时间查询，用于辅助亲子、刺激或均衡路线的游园计划。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and planning assistants use this skill to estimate Shanghai Disney attraction waits, compare ticket and dining options, check park hours, and generate practical one-day route suggestions before or during a visit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queue times, show times, ticket prices, and route advice may be estimated, stale, or differ from real park conditions. <br>
Mitigation: Treat outputs as planning aids and verify official Shanghai Disney sources before purchasing tickets, making reservations, or relying on same-day schedules. <br>
Risk: Park-hours lookup uses a cloud proxy. <br>
Mitigation: Install only if this data flow is acceptable, avoid sharing sensitive personal information in planning queries, and confirm hours with official sources. <br>
Risk: The skill may suggest adjacent travel or hotel searches outside its implemented tools. <br>
Mitigation: Treat those suggestions as optional handoffs and validate travel, lodging, and transportation decisions separately. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/travel-skills/skills/shanghai-disney) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>
- [Park-hours proxy endpoint](https://1439498936-bl10af74fl.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-like plain text responses from tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are planning guidance and estimates; the schedule tool may call a cloud proxy, while route, wait, show, ticket, and dining responses primarily use bundled local data.] <br>

## Skill Version(s): <br>
1.2.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
