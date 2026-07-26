## Description: <br>
호텔, 관광명소, 식사, 팁이 포함된 중국 맞춤형複数日の 여행 일정을 생성합니다. 호텔 검색, 항공권, 관광지 티켓, 여행 Q&A도 지원합니다. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-ko](https://clawhub.ai/user/china-travel-ko) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to generate China itineraries and retrieve hotel, flight, attraction, ticket, and travel-advice results in Korean. The skill passes destination, dates, preferences, and related travel details to a third-party proxy-backed TripGenie workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel plans, dates, preferences, and booking-related details are sent to a third-party proxy. <br>
Mitigation: Review the external data flow before installation and avoid sending sensitive travel or booking details unless the proxy path is acceptable for the deployment. <br>
Risk: The distributed script embeds a proxy token while the documentation says credentials should be injected server-side. <br>
Mitigation: Move credentials out of the distributed artifact and document how proxy credentials are provided and rotated. <br>
Risk: Security evidence flags inconsistent documentation around proxy behavior and language handling. <br>
Mitigation: Clarify proxy behavior, data handling, and locale expectations before approving the release for routine use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/china-travel-ko/skills/china-travel-planner) <br>
- [Publisher profile: china-travel-ko](https://clawhub.ai/user/china-travel-ko) <br>
- [External proxy endpoint used by skill](https://1439498936-eu423jdjnd.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Structured Markdown travel plans and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include itinerary sections, hotel recommendations, flight search results, attraction details, travel tips, and booking links.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
