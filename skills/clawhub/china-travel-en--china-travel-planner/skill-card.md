## Description: <br>
Generate personalized multi-day itineraries for China with hotels, attractions, dining and tips, with support for hotel search, flights, attraction tickets, and travel Q&A for inbound tourists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-en](https://clawhub.ai/user/china-travel-en) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and travel-support agents use this skill to generate China trip itineraries, search hotels and flights, find attraction information, and answer practical travel questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel queries, dates, locations, preferences, and similar itinerary details are sent to the publisher's proxy and TripGenie. <br>
Mitigation: Install only if comfortable sharing those details, and avoid entering sensitive personal information into travel prompts. <br>
Risk: Generated itineraries, prices, policies, and booking links may be incomplete, outdated, or commercially influenced. <br>
Mitigation: Review travel recommendations and verify bookings, prices, entry rules, and schedules with the relevant provider before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/china-travel-en/skills/china-travel-planner) <br>
- [Publisher profile](https://clawhub.ai/user/china-travel-en) <br>
- [Disclosed travel proxy endpoint](https://1439498936-eu423jdjnd.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown travel guidance and JSON-formatted command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PROXY_URL and PROXY_TOKEN; sends travel requests to the publisher proxy for TripGenie responses.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
