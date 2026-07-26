## Description: <br>
Searches, compares, books, and fixes flights, including fares and fare rules, connections, baggage, seats, miles, delays, passenger rights, travel documents, special passenger needs, corporate travel, and flight data APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-focused agents use this skill to find, compare, monitor, book, change, and recover value from flights. It is also useful after ticketing for baggage, seats, disruptions, refunds, loyalty points, passenger rights, document checks, and travel recordkeeping. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically update local travel, booking, contact, finance, and project notes with sensitive travel details. <br>
Mitigation: Use it only where automatic local recordkeeping is wanted, and periodically review the affected Clawic files for accuracy and appropriate contents. <br>
Risk: Travel records may involve sensitive personal, loyalty, claim, and deadline information. <br>
Mitigation: Store credential pointers rather than secrets, and avoid saving passwords, card numbers, passport numbers, boarding-pass barcodes, programme PINs, or API secrets. <br>
Risk: Flight prices, fare rules, entry requirements, passenger-rights thresholds, and API pricing can change. <br>
Mitigation: Verify current airline, regulator, government, or provider sources before purchase decisions, compensation promises, entry guidance, or API design commitments. <br>
Risk: An agent could overstep by completing payment or committing to a risky booking channel. <br>
Mitigation: Keep the skill in advice-and-draft mode unless the user explicitly asks for action, and do not complete payment on the user's behalf. <br>


## Reference(s): <br>
- [ClawHub Flight Skill](https://clawhub.ai/ivangdavila/skills/flight) <br>
- [Clawic Flight Skill](https://clawic.com/skills/flight) <br>
- [Flight Data APIs](apis.md) <br>
- [Award Tickets](awards.md) <br>
- [Baggage](baggage.md) <br>
- [Buying The Ticket](booking.md) <br>
- [Connections, Layovers, and Two-Ticket Itineraries](connections.md) <br>
- [When It Breaks](disruptions.md) <br>
- [Passports, Visas, and Being Allowed To Board](documents.md) <br>
- [Fares, Fare Families, and Fare Rules](fares.md) <br>
- [Working File Templates](memory-template.md) <br>
- [Points, Miles, and Elite Status](points.md) <br>
- [Getting Money Back](refunds.md) <br>
- [Finding the Flight](search.md) <br>
- [Seats, Upgrades, and Sitting Together](seats.md) <br>
- [Prices Over Time, And Flights In The Air](tracking.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown or plain text with optional tables, checklists, drafts, local-file updates, and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local Clawic travel, booking, contact, finance, and project notes when the session produces durable travel information.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
