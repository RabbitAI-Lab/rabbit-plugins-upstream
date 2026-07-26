## Description: <br>
중국행 항공편 및 국내선을 실시간 요금, 스케줄, Trip.com 예약 링크로 검색하고 호텔, 관광명소, 여행 계획, 여행 조언도 지원합니다. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-ko](https://clawhub.ai/user/china-travel-ko) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Korean-speaking external travelers and travel-planning agents use this skill to compare China-bound and domestic China flights by route, date, trip type, and cabin. It also supports related hotel search, attraction discovery, itinerary planning, and China travel advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel queries, dates, destinations, and preferences are sent to the disclosed TripGenie proxy service for processing. <br>
Mitigation: Avoid entering passport numbers, payment details, or other highly sensitive personal information in free-form travel prompts. <br>
Risk: Returned booking links and travel options may affect purchasing decisions. <br>
Mitigation: Review Trip.com booking links, prices, schedules, and terms before booking. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/china-travel-ko/skills/china-flight-booking) <br>
- [Publisher profile](https://clawhub.ai/user/china-travel-ko) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown travel results with JSON command status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Flight mode uses origin, destination, date, optional trip type, optional cabin, and --locale=ko for Korean results.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
