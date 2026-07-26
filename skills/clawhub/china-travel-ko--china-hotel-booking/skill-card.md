## Description: <br>
중국 도시의 호텔을 검색하고 실시간 추천, 요금, 예약 링크를 제공합니다. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-ko](https://clawhub.ai/user/china-travel-ko) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to find China hotel options by city, dates, guest count, budget, and location preferences, then present Korean Markdown results with rates, ratings, features, and booking links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends travel dates, destinations, budgets, and preferences to a disclosed proxy service. <br>
Mitigation: Use only when the user is comfortable sharing those travel details with the proxy service, and avoid sending sensitive personal information. <br>
Risk: Booking links may be affiliate-modified rather than purely direct Trip.com links. <br>
Mitigation: Review booking URLs before acting on them and disclose affiliate-link behavior where relevant. <br>
Risk: The artifact includes extra travel modes beyond the hotel-booking description. <br>
Mitigation: For this release, prefer hotel mode unless the user explicitly asks for broader travel lookup behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/china-travel-ko/skills/china-hotel-booking) <br>
- [Publisher profile](https://clawhub.ai/user/china-travel-ko) <br>
- [Disclosed proxy service endpoint](https://1439498936-eu423jdjnd.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Travel recommendations, Booking links] <br>
**Output Format:** [JSON containing Markdown travel results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Korean output is requested with --locale=ko; results may include hotel names, rates, ratings, features, and Trip.com booking links.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
