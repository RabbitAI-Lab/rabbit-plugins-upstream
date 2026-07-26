## Description: <br>
同程旅行助手 searches Tongcheng travel products across hotels, flights, trains, buses, attraction tickets, transport comparisons, and vacation packages, returning prices, availability details, and booking links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to search and compare Tongcheng travel options for lodging, tickets, routes, attractions, and vacation packages. The skill returns search results and booking links, but does not place orders, process payments, or manage existing bookings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel destinations, dates, routes, and preferences are sent to the skill publisher's cloud proxy before reaching Tongcheng services. <br>
Mitigation: Install only if this data flow is acceptable, and avoid entering account details, identity documents, payment data, or private booking records. <br>
Risk: Search results include real-time prices and booking links that may change after the skill returns them. <br>
Mitigation: Confirm price, availability, and terms on the final Tongcheng booking page before making travel decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/tongcheng-travel-assistant) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown search results with prices, availability details, and booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results are limited by category-specific caps in the artifact and prices may change before booking.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
