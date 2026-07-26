## Description: <br>
市内公交地铁路线查询，自动规划最优换乘方案，地铁优先展示，支持最快/少换乘/少步行三种策略，零配置即装即用。暑期城市出行导航。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to query same-city bus and metro routes, compare transfer options, and choose fastest, fewer-transfer, or shorter-walking transit plans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Route queries include origin, destination, and city and are sent through the publisher's cloud proxy. <br>
Mitigation: Use the skill only when that data sharing is acceptable for the intended users and environment. <br>
Risk: Transit times, fares, and operating details are estimates that may differ from current local service conditions. <br>
Mitigation: Confirm time-sensitive travel details with the local transit operator or a live maps application before relying on the result. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/transit-route-query) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown text with route summaries, transit segments, walking distances, estimated duration, and estimated fare] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns estimated same-city bus and metro route guidance; route results depend on the publisher cloud proxy and upstream map data.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
