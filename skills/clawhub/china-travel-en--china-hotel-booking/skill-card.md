## Description: <br>
Search hotels across China with real-time pricing, ratings, and Trip.com booking links, with related support for flights, attractions, itinerary planning, and travel tips for inbound tourists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-en](https://clawhub.ai/user/china-travel-en) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to search hotels in Chinese cities by destination, dates, guest count, budget, and preferences. It can also return related flight, attraction, itinerary, and travel-tip results through the same travel-search workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel-search details are sent to the skill publisher's proxy and onward travel services. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and avoid entering passport numbers, payment details, account credentials, or other sensitive personal information. <br>
Risk: Returned booking links may lead users to third-party booking flows. <br>
Mitigation: Review booking links and destination details before opening or using them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/china-travel-en/skills/china-hotel-booking) <br>
- [Publisher profile](https://clawhub.ai/user/china-travel-en) <br>
- [Publisher proxy endpoint](https://1439498936-eu423jdjnd.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Structured Markdown travel-search results with hotel names, prices, ratings, features, and booking links; script responses are emitted as JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires travel-search inputs such as city, optional dates, guests, budget, preferences, and optional locale.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
