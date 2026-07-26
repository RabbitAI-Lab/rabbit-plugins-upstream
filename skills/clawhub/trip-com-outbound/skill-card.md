## Description: <br>
出境游一站式助手，支持搜索全球酒店、查询国际机票、购买境外景点门票。数据来自Trip.com（携程国际版），预订链接自动携带联盟推广。面向中国出境游用户。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users planning outbound travel from China use this skill to search overseas hotels, international flights, and attraction tickets, then review prices, ratings, and booking links from Trip.com-related results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel queries, including itinerary details, are sent to an external proxy or Trip.com-related service. <br>
Mitigation: Use the skill only for explicit travel search or booking tasks and avoid including unnecessary personal details. <br>
Risk: The skill may activate more broadly than users expect for travel-related questions. <br>
Mitigation: Confirm that the user is requesting hotel, flight, or attraction-ticket search before executing the outbound query. <br>
Risk: Outbound destinations, data handling, and consent expectations are under-disclosed. <br>
Mitigation: Review publisher documentation and environment configuration before deployment, and disclose the external proxy path to users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/trip-com-outbound) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text travel-search results with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include hotel names, flight details, prices, ratings, attraction descriptions, and Trip.com affiliate booking links.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
