## Description: <br>
途牛旅行助手 helps agents search and book hotels, flights, trains, scenic tickets, cruises, and vacation products with formatted result summaries and images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can use this skill through an agent to search travel options, compare availability and prices, and initiate hotel, flight, train, scenic-ticket, cruise, or vacation booking workflows. Booking workflows may require personal travel and contact information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports under-disclosed cancellation and order-detail actions. <br>
Mitigation: Require explicit user confirmation before order-detail lookup or cancellation, including the exact tool name and affected order identifier. <br>
Risk: The security review reports a hard-coded fallback proxy token despite the artifact claiming no embedded key. <br>
Mitigation: Remove the fallback token and require PROXY_TOKEN to be supplied through the runtime environment before use. <br>
Risk: Travel booking flows can transmit personal information such as names, phone numbers, and identity document details to the proxy and travel platform. <br>
Mitigation: Use only with trusted publisher and proxy infrastructure, and collect booking personal information only after the user explicitly asks to place an order. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/tuniu-travel-assistant) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-formatted text with travel search results, prices, recommendations, booking prompts, and optional image links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return booking or order-management responses from a configured proxy service.] <br>

## Skill Version(s): <br>
2.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
