## Description: <br>
全球航班搜索与出境旅行一站式助手，11个工具覆盖国际机票、酒店、签证、安全、插头、退税、汇率、航班座位行李、紧急求助，零配置即装即用。暑假出境航班查询。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to search international flights and hotels, compare baggage and seat details, and check visa, safety, plug, tax-refund, exchange-rate, and emergency information for outbound trips. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Flight, hotel, flight-number, route, date, hotel ID, and currency-pair lookups may send travel-search details to the skill's cloud proxy or a public exchange-rate API. <br>
Mitigation: Avoid sensitive or confidential itineraries, and only override RG_PROXY or PROXY_TOKEN when the endpoint is controlled and trusted. <br>
Risk: Visa rules, safety conditions, booking availability, exchange rates, and refund amounts can change or differ from estimates. <br>
Mitigation: Confirm important travel, payment, visa, safety, and tax-refund decisions with the relevant airline, hotel, government, embassy, or refund provider before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/global-flight-search) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON strings and concise travel guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include booking URLs, prices, itinerary details, visa requirements, safety ratings, refund estimates, exchange-rate conversions, and emergency contact information.] <br>

## Skill Version(s): <br>
1.3.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
