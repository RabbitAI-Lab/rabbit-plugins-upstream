## Description: <br>
Searches Google Flights through Scavio's v2 API and returns structured flight itinerary JSON including price, airline, duration, stops, and legs for round-trip, one-way, and multi-city requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and travel-planning agents use this skill to search and compare flights by route, dates, cabin, stops, airline filters, duration, and price. It is suited for producing structured flight-search results from Scavio rather than estimating or fabricating fares. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Flight searches send trip details such as airports, dates, passenger counts, cabin preferences, and airline filters to Scavio's API. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and avoid including unnecessary personal or sensitive information in search requests. <br>
Risk: The skill requires a Scavio API key. <br>
Mitigation: Use your own SCAVIO_API_KEY from the environment and avoid pasting, logging, or sharing the key. <br>
Risk: Flight prices, times, airlines, and durations can be incorrect if an agent invents values outside the API response. <br>
Mitigation: Return only values from Scavio API data, state the requested currency when quoting fares, and retry or adjust filters when the API returns no flights or an error. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-flights) <br>
- [Scavio Google Flights documentation](https://scavio.dev/docs/google-flights) <br>
- [Scavio rate limits](https://scavio.dev/docs/rate-limits) <br>
- [scavio-ai publisher profile](https://clawhub.ai/user/scavio-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell setup, API request examples, and structured JSON flight-search results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Scavio reports each Google Flights request as costing 1 credit.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
