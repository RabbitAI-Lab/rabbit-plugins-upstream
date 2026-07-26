## Description: <br>
零配置即装即用，本地旅行一站式查询，酒店/机票/火车票/景点门票/行程规划全覆盖，数据覆盖300+城市。暑期吃喝玩乐一站式，美团旅行全攻略 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-focused agents use this skill to answer Chinese-language travel requests for hotels, flights, train tickets, scenic tickets, and itinerary suggestions from a city and natural-language query. It provides information and booking links, but does not complete payment or booking transactions. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: User travel preferences are sent to an external travel proxy. <br>
Mitigation: Install only when users accept sharing city, destination, dates, budget, and related travel preferences; disclose the external data sharing before use. <br>
Risk: Declared tools, documented tool names, and the executable script interface do not line up. <br>
Mitigation: Verify the actual callable tool name, script arguments, and environment variables in a staging agent before approving broader use. <br>
Risk: Operational configuration may be unclear because the declared environment variable differs from the script's proxy settings. <br>
Mitigation: Require the publisher to document the real environment variables and proxy endpoint before broader deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/meituan-travel-assistant) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, API calls] <br>
**Output Format:** [JSON returned by the script, typically rendered by the agent as travel guidance, prices, availability details, and booking links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a city and natural-language travel query; results depend on the external travel proxy and may include proxy error responses.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release evidence; artifact _meta.json reports 2.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
