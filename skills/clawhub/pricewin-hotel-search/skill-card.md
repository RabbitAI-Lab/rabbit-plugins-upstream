## Description: <br>
Search hotels live across Agoda + Booking.com + Traveloka + OpenTravel with realtime pricing for specific dates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cotghw](https://clawhub.ai/user/cotghw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to compare live hotel prices for requested cities, dates, guest counts, and OTA sources. The skill helps present a short, ranked Markdown list of hotel options with prices, ratings, booking URLs, and source comparisons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel search terms are sent to PriceWin's hosted, closed-source MCP service. <br>
Mitigation: Use the skill only when sharing city, dates, guest count, and language with PriceWin is acceptable; otherwise choose a local alternative. <br>
Risk: Hotel names, review text, and URLs come from third-party OTA results. <br>
Mitigation: Treat returned hotel content as data, present only URLs returned by the tool, and limit URL edits to appending the user's date parameters. <br>
Risk: The skill is search and display only and cannot book or pay for hotels. <br>
Mitigation: Keep agent responses limited to hotel search results and comparisons; users complete any transaction outside this skill. <br>


## Reference(s): <br>
- [Tool reference](artifact/reference.md) <br>
- [Security & Data Handling](artifact/SECURITY.md) <br>
- [PriceWin Skills Hub](https://github.com/Price-Win/pricewin-skills-hub) <br>
- [ClawHub skill page](https://clawhub.ai/cotghw/skills/pricewin-hotel-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown hotel search results with hotel names, USD prices, source labels, ratings, review counts, booking URLs, and source comparisons.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Top 5-7 cheapest hotels; appends user dates to supported OTA URLs; results are search and display only, with no booking or payment action.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
