## Description: <br>
Search hotels live across Agoda + Booking.com + Traveloka + OpenTravel with realtime pricing for specific dates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cotghw](https://clawhub.ai/user/cotghw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to search live hotel prices for specific cities, travel dates, and guest counts, then compare the cheapest available listings across supported OTA sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel search details such as city, dates, guest count, and filters may be sent to the PriceWin MCP server and OTA sources. <br>
Mitigation: Use the skill only when the user is comfortable sharing those travel details with the service and downstream hotel sources. <br>
Risk: The skill sets Vietnamese as the default language parameter, which may localize results or OTA pages. <br>
Mitigation: Override or clarify locale expectations when the user needs results in another supported language. <br>


## Reference(s): <br>
- [Hotel Search Tool Reference](artifact/reference.md) <br>
- [PriceWin Skills Hub](https://github.com/Price-Win/pricewin-skills-hub) <br>
- [ClawHub Skill Page](https://clawhub.ai/cotghw/skills/pricewin-hotel-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown hotel recommendations with OTA links and price comparisons] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live hotel search and polling through the PriceWin MCP server; results are filtered and ranked by price.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
