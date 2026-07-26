## Description: <br>
중국의顶级 관광명소를 티켓 요금, 영업 시간, Trip.com 예약 링크로 발견합니다. 호텔, 항공권, 여행 계획, 여행 조언도 지원합니다. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-ko](https://clawhub.ai/user/china-travel-ko) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to find Chinese attractions, ticket details, opening hours, hotels, flights, itineraries, and travel advice with Korean-language results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel queries are sent to a remote TripGenie/Tencent SCF proxy and may return affiliate booking links. <br>
Mitigation: Use the skill only for travel-search data you are comfortable sending to that proxy, and avoid entering sensitive personal details beyond what is needed for the search. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/china-travel-ko/skills/china-attraction-tickets) <br>
- [TripGenie proxy endpoint](https://1439498936-eu423jdjnd.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON from the helper script containing Markdown travel results or error text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Korean locale results are requested with --locale=ko; travel queries are sent to a remote TripGenie/Tencent SCF proxy.] <br>

## Skill Version(s): <br>
1.0.2 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
