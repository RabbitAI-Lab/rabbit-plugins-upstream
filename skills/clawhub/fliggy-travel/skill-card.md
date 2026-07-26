## Description: <br>
飞猪旅行 helps an agent plan trips and search Fliggy or Gaode-backed travel information across hotels, flights, trains, attractions, food, local transport, Marriott options, and itinerary planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to plan itineraries and search travel inventory such as hotels, flights, trains, attractions, food, local transport, and Marriott options. Booking and payment are completed outside the skill through returned provider links. <br>

### Deployment Geography for Use: <br>
Global, with results oriented toward destinations and services covered by Fliggy and Gaode. <br>

## Known Risks and Mitigations: <br>
Risk: Travel searches, destinations, dates, hotel interests, and route or address queries may be sent to external proxy and API services before results are returned. <br>
Mitigation: Avoid entering private home addresses or sensitive itinerary details unless the user is comfortable with that external processing. <br>
Risk: Travel prices, availability, route estimates, and booking links can change after the skill returns results. <br>
Mitigation: Verify final prices, availability, route details, and booking terms on the linked provider page before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page for 飞猪旅行](https://clawhub.ai/travel-skills/skills/fliggy-travel) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown text with travel recommendations, prices, routes, image links, and booking links when returned by upstream services.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include real-time prices, availability, route estimates, image URLs, and booking links; booking and payment happen outside the skill.] <br>

## Skill Version(s): <br>
1.3.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
