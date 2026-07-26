## Description: <br>
Searches Westin hotels under Marriott, returns current prices and booking links, and helps retrieve hotel details and package offers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and travel-planning agents use this skill to search Westin hotel availability, compare prices and locations, inspect hotel details, and find package offers before following external booking links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel search terms, dates, and keywords are sent to the publisher cloud proxy and downstream travel APIs. <br>
Mitigation: Avoid entering sensitive personal details in search keywords and review the disclosed data flow before deployment. <br>
Risk: The artifact uses a configurable proxy endpoint and a hardcoded fallback token. <br>
Mitigation: Use a trusted PROXY_URL and PROXY_TOKEN from the environment, and prefer a version that validates the proxy endpoint and removes the fallback token. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/westin-hotel-booking) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API Calls, guidance] <br>
**Output Format:** [Markdown text with hotel results, prices, details, package summaries, and booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns search results and guidance only; it does not complete bookings directly.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
