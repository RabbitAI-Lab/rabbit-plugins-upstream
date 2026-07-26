## Description: <br>
Search flights to China and domestic routes with real-time prices, schedules and Trip.com booking links. Also supports hotels, attractions, itinerary planning and travel tips for inbound tourists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-en](https://clawhub.ai/user/china-travel-en) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and agents use this skill to search flights to and within China, with companion hotel, attraction, itinerary, and travel-tip searches. It runs a shell command that sends travel queries to the publisher's proxy and returns booking-oriented Markdown for presentation to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel searches, dates, preferences, and itinerary details are sent to the publisher's proxy and TripGenie. <br>
Mitigation: Use the skill only for travel details you are comfortable sharing with those services. <br>
Risk: The reviewed artifact contains a hardcoded proxy token. <br>
Mitigation: Publisher should rotate and move the token out of distributed artifacts before broader release. <br>


## Reference(s): <br>
- [China Flight Booking on ClawHub](https://clawhub.ai/china-travel-en/skills/china-flight-booking) <br>
- [china-travel-en publisher profile](https://clawhub.ai/user/china-travel-en) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown travel results with shell command invocations and JSON-wrapped script responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports flight, hotel, attraction, itinerary, and travel-tip modes with optional locale selection.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
