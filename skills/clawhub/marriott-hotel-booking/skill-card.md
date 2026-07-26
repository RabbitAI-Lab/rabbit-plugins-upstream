## Description: <br>
Searches Marriott-family hotels by destination, brand keyword, and price, returning hotel prices, ratings, addresses, detail links, and package offers through travel-platform APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and booking assistants use this skill to search Marriott-brand hotels, review hotel details, and find package offers before completing booking on external travel links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel search terms, locations, dates, and hotel identifiers are sent to the skill's cloud proxy and travel API providers. <br>
Mitigation: Install only when that data sharing is acceptable, and avoid entering sensitive travel details unless the publisher documents the proxy and provider handling clearly. <br>
Risk: The artifact includes transparency and credential-handling caveats, including a hardcoded default proxy token noted by security evidence. <br>
Mitigation: Publisher should document the exact proxy endpoint and replace the hardcoded default token with a deployment-specific secret. <br>
Risk: Returned prices and booking availability depend on external travel-platform data and may change. <br>
Mitigation: Confirm final price, policies, and availability on the linked booking page before making travel decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/marriott-hotel-booking) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown-formatted text with hotel listings, prices, addresses, hotel identifiers, and booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results depend on external travel-platform data and live pricing availability.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release evidence; artifact frontmatter lists 1.1.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
