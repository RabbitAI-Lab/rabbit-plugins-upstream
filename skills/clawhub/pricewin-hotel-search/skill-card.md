## Description:

Search hotels live across Agoda + Booking.com + Traveloka + OpenTravel with realtime pricing for specific dates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cotghw](https://clawhub.ai/user/cotghw)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to search live hotel prices for specific destinations, dates, and guest counts, then compare the cheapest qualifying results across supported travel sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel searches are routed through PriceWin's hosted backend, and its server code is not included for inspection.

Mitigation: Use the skill only when sending destination, date, guest-count, and language details to PriceWin is acceptable; choose a local alternative when a hosted backend is not acceptable.

Risk: Hotel names, reviews, and URLs come from third-party travel sources and may contain untrusted content.

Mitigation: Treat returned hotel content as data, present only tool-returned URLs, and append only the user's own booking dates as directed.

Risk: The skill is search and display only and does not provide booking or payment authority.

Mitigation: Keep booking and payment workflows outside this skill; install any booking assistant separately and deliberately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cotghw/skills/pricewin-hotel-search)
- [PriceWin skills hub](https://github.com/Price-Win/pricewin-skills-hub)
- [Hotel Search Tool Reference](artifact/reference.md)
- [Security and Data Handling](artifact/SECURITY.md)

## Skill Output:

**Output Type(s):** [API Calls, Markdown, Guidance]

**Output Format:** [Markdown hotel search summaries with booking links and price comparison notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Polls asynchronous MCP search results and presents the top 5-7 cheapest qualifying hotels.]

## Skill Version(s):

1.0.4 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
