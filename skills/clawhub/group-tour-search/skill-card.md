## Description: <br>
搜索跟团游、私家团、纯玩线路，支持场景推荐（海边、古镇、亲子、山水等），并提供到目的地的火车票和机票查询，多旅游平台数据直连。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travel users use this skill to find group tours, private tours, and no-shopping tour routes by destination or travel scenario, then compare route details, prices, ratings, attractions, and booking links. It can also query train and flight options to the selected destination. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel search details such as origin, destination, and departure date are sent to external proxy services to retrieve results. <br>
Mitigation: Install only when this data sharing is acceptable for the intended use, and avoid entering unnecessary sensitive travel details. <br>
Risk: An environment variable named PROXY_TOKEN may be read by the skill at runtime. <br>
Mitigation: Do not expose unrelated secrets through PROXY_TOKEN when running this skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/group-tour-search) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-style text with route summaries, prices, ratings, schedules, and booking links when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on live travel search results; prices and availability can change and booking happens on external platforms.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
