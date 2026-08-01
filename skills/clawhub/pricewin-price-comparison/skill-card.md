## Description: <br>
Compare live hotel room rates across Booking.com, Agoda, Traveloka, and OpenTravel for specific dates, including the cheapest OTA for the same property, per-room prices, and free-cancellation terms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cotghw](https://clawhub.ai/user/cotghw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel agents use this skill to compare live hotel prices for a city or named property across Booking.com, Agoda, Traveloka, and OpenTravel. It helps rank returned sources by price, identify savings, and surface cancellation terms when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel search details such as city, hotel name, travel dates, occupancy, and verbatim query text may be sent to the pricewin MCP server for live rate comparison. <br>
Mitigation: Use the skill only when sharing those travel search details with the pricewin MCP server is acceptable. <br>
Risk: Live hotel crawl results can be partial, delayed, unavailable, or different from final prices and cancellation terms shown by the booking source. <br>
Mitigation: Treat returned comparisons as decision support and verify prices, availability, and cancellation terms with the source before booking. <br>


## Reference(s): <br>
- [Price Comparison Tool Reference](artifact/reference.md) <br>
- [PriceWin Skills Hub](https://github.com/Price-Win/pricewin-skills-hub) <br>
- [ClawHub Skill Page](https://clawhub.ai/cotghw/skills/pricewin-price-comparison) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hotel rankings, source-by-source prices, savings calculations, room details, and cancellation summaries based on live MCP results.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
