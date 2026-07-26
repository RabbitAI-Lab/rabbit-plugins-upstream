## Description: <br>
중국 여행을 위한 필수 가이드: 비자, 모바일 결제, 교통, 음식, 안전, 호텔, 항공권, 관광명소, 일정 계획을 지원합니다. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-ko](https://clawhub.ai/user/china-travel-ko) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and agents use this skill to answer China travel questions and produce Korean guidance for hotels, flights, attractions, itineraries, payment setup, visas, transportation, food, safety, and local etiquette. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel questions, dates, destinations, budgets, and preferences are sent to the publisher's Tencent SCF proxy and TripGenie API. <br>
Mitigation: Do not include passport numbers, payment details, or other sensitive personal information in prompts. <br>
Risk: Travel advice, prices, availability, visa requirements, and safety guidance may be incomplete or out of date. <br>
Mitigation: Confirm critical requirements, bookings, and safety information with official or primary providers before relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/china-travel-ko/skills/china-travel-tips) <br>
- [Disclosed Tencent SCF proxy endpoint](https://1439498936-eu423jdjnd.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [JSON from the travel script and Korean text or Markdown presented to the user] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documented usage requests Korean output with --locale=ko and sends travel queries through a disclosed external proxy.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
