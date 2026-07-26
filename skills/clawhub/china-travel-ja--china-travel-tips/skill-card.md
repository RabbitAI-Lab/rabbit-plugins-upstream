## Description: <br>
China Travel Tips helps agents answer China travel questions and support hotel, flight, attraction, and itinerary requests for foreign travelers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-ja](https://clawhub.ai/user/china-travel-ja) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-focused agents use this skill to answer China travel questions in Japanese and request practical help with hotels, flights, attractions, and multi-day itineraries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User travel questions, itinerary details, dates, and destinations are sent to an external proxy and TripGenie flow. <br>
Mitigation: Install only when users are comfortable sharing those travel details with that flow, and avoid sending sensitive personal data. <br>
Risk: Security evidence reports an embedded proxy token and conflicting environment-variable documentation. <br>
Mitigation: The publisher should move credentials to managed environment variables and resolve the documentation mismatch before broad trust. <br>
Risk: The authoritative scanner verdict is suspicious because of the external proxy and token handling. <br>
Mitigation: Review the source and expected network destination before execution, and limit use to the intended China travel workflows. <br>


## Reference(s): <br>
- [China Travel Tips on ClawHub](https://clawhub.ai/china-travel-ja/skills/china-travel-tips) <br>
- [Publisher profile](https://clawhub.ai/user/china-travel-ja) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text for users, with JSON returned by the helper script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses are tailored for Japanese-language China travel assistance; the helper script also supports hotel, flight, attraction, itinerary, and tips modes.] <br>

## Skill Version(s): <br>
2.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
