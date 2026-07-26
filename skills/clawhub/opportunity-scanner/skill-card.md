## Description: <br>
Scans live GitHub and Hacker News signals to surface trending repositories, hiring posts, launches, and funding activity for developers and investors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[welove111](https://clawhub.ai/user/welove111) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, investors, freelancers, and job seekers use this skill to scan public GitHub and Hacker News activity for same-day opportunity signals, including emerging repositories, hiring threads, product launches, and funding chatter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill calls an external MCP service at the publisher's domain, which may receive scouting criteria or business context included in prompts. <br>
Mitigation: Avoid sending sensitive private business plans or confidential scouting criteria unless the publisher service is trusted for that data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/welove111/skills/opportunity-scanner) <br>
- [Opportunity Scanner MCP endpoint](https://www.aliensignalsystems.online/api/opportunity-scanner) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON objects and concise text summaries from MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public GitHub and Hacker News data; optional filters include topic, category, lookback window, and result limit.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
