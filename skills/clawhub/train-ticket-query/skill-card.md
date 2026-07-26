## Description: <br>
查询中国铁路 12306 火车票、高铁、动车和普快车次的余票、票价和时刻表，并返回可供用户查看的实时结果。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and travel-planning agents use this skill to check Chinese train availability, fares, schedules, seat inventory, and booking links before buying tickets through official or linked booking channels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends travel and location details to external proxy services. <br>
Mitigation: Use only when that data sharing is acceptable, and disclose the proxy/API data flow to users before deployment. <br>
Risk: The bundled script includes broader travel tools beyond the public train-ticket description. <br>
Mitigation: Limit exposed tools to the declared train-ticket function or clearly document the additional travel, food, hotel, flight, and transport capabilities. <br>
Risk: Security evidence recommends preferring a version without a hardcoded proxy token. <br>
Mitigation: Require proxy credentials to be supplied through deployment configuration and rotate any token that appeared in distributed source. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/train-ticket-query) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [JSON strings containing train-search results, disclaimers, and follow-up guidance; command-line usage is also supported by the bundled Python script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include origin, destination, date, train listings, availability notes, booking links, and reminders that prices and inventory can change.] <br>

## Skill Version(s): <br>
1.1.3 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
