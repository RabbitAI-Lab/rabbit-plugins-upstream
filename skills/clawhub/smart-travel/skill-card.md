## Description: <br>
A one-stop AI travel assistant that helps agents plan trips and search flights, hotels, trains, attractions, food, weather, taxi links, buses, tours, cruises, and vacation products using travel and map service data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer travel-planning and booking-search questions, including itinerary planning, transport options, lodging, attractions, dining, weather, and packaged travel products. It is suited for travel discovery and comparison workflows where final booking details should be confirmed with the linked provider. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel-related queries, such as cities, routes, dates, hotel preferences, and nearby-place requests, are sent through the publisher's cloud proxy to travel and map services. <br>
Mitigation: Avoid entering sensitive personal details that are not needed for the search, and install only if this proxy-based data flow is acceptable. <br>
Risk: Prices, availability, schedules, routes, and weather results can change after the skill returns them. <br>
Mitigation: Confirm important details on the linked provider page or an authoritative source before booking or traveling. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/travel-skills/skills/smart-travel) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain text travel results with prices, schedules, routes, weather summaries, tips, and booking links when available.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include real-time provider data and links; prices, availability, schedules, and weather can change.] <br>

## Skill Version(s): <br>
3.2.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
