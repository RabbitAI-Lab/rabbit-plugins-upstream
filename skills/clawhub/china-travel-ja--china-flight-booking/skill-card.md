## Description: <br>
Searches flights to and within China with real-time fares, schedules, and Trip.com booking links, and also supports hotels, attractions, itinerary planning, and travel advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-ja](https://clawhub.ai/user/china-travel-ja) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-support agents use this skill to search China flights, compare travel options, find hotels and attractions, generate itineraries, and answer practical travel questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel plans, dates, routes, or preferences may be sent to a third-party proxy. <br>
Mitigation: Review the skill before installation and avoid submitting sensitive travel or personal data unless the proxy destination and handling are acceptable. <br>
Risk: The fixed proxy and embedded reusable token make the backend destination and credential handling difficult for users to verify or control. <br>
Mitigation: Require runtime-configurable proxy and token handling before production deployment or restrict use to low-sensitivity travel searches. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/china-travel-ja/skills/china-flight-booking) <br>
- [Publisher profile](https://clawhub.ai/user/china-travel-ja) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [JSON response containing Markdown travel results, practical guidance, and booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports flight, hotel, attraction, itinerary, and tips modes with locale-specific responses.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
