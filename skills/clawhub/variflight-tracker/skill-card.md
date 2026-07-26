## Description: <br>
基于飞常准数据，提供航班实时动态、延误分析、舒适度评分、机场天气查询，覆盖全球航班，零配置即用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel assistants use this skill to check real-time flight status, route delays, comfort scores, and airport weather before or during trips. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Flight numbers, routes, dates, and airport/weather queries are sent through the publisher's proxy service and then to VariFlight. <br>
Mitigation: Avoid entering sensitive itinerary details unless the publisher's proxy is trusted, and review data-sharing expectations before deployment. <br>
Risk: The source includes a reusable fallback proxy token. <br>
Mitigation: Rotate and remove the embedded fallback token, and provide proxy credentials through the PROXY_TOKEN environment variable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/variflight-tracker) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown tables and summaries, with JSON error or empty-result objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include flight status, delay analysis, route summaries, comfort comparisons, airport weather, and flight-impact notes.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
