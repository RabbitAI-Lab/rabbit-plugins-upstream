## Description: <br>
出境游旅行助手为出境游用户提供国际机票和酒店搜索、签证、安全、插头电压、退税、汇率、航班座位行李和紧急求助等一站式旅行查询。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers use this skill to plan outbound trips by checking flights, hotels, visa requirements, destination safety, plug and voltage standards, tax refunds, exchange rates, baggage details, seat information, and emergency contacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live flight, hotel, seat, baggage, room, and exchange-rate lookups send travel query details to external services. <br>
Mitigation: Use only the itinerary details needed for the query, avoid highly sensitive personal data, and review external-service handling before deployment. <br>
Risk: The skill relies on a shared embedded proxy token for proxy-backed lookups. <br>
Mitigation: Replace it with configurable per-deployment credentials or require the publisher to clarify token scope, rotation, and retention behavior before commercial use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/outbound-travel-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [JSON-formatted text and agent-readable Markdown summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include booking links, estimated prices, safety scores, tax-refund estimates, exchange-rate calculations, and emergency contact guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
