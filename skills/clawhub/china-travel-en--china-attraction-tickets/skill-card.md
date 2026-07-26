## Description: <br>
China Attraction Tickets helps inbound tourists discover China attractions with ticket prices, opening hours, Trip.com booking links, and related hotel, flight, itinerary, and travel-tip support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-en](https://clawhub.ai/user/china-travel-en) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to search China attraction tickets, opening hours, prices, booking links, hotels, flights, itineraries, and travel tips. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel searches, dates, locations, preferences, and itinerary questions are sent to the publisher's Tencent SCF proxy and TripGenie/Trip.com-related services. <br>
Mitigation: Use the skill only for queries acceptable to share with those services; avoid passport numbers, payment details, account passwords, and other sensitive personal information. <br>
Risk: Travel availability, prices, opening hours, booking links, and travel tips can be incomplete or change after retrieval. <br>
Mitigation: Treat results as planning guidance and verify booking, schedule, visa, payment, and transport details with official or booking-provider sources before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/china-travel-en/skills/china-attraction-tickets) <br>
- [Publisher profile](https://clawhub.ai/user/china-travel-en) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [JSON from the helper script with Markdown travel results in the response field] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PROXY_URL and PROXY_TOKEN; supports attraction, hotel, flight, itinerary, and tips modes with optional locale selection.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
