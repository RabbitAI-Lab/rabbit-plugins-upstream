## Description:

Uses the RollingGo CLI to search hotels, filter results, read hotel tags, and retrieve hotel room pricing and details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longcreat](https://clawhub.ai/user/longcreat)

### License/Terms of Use:

MIT-0

## Use Case:

External users, travel planners, and developers use this skill to find candidate hotels by destination, dates, budget, star rating, tags, brand, or distance, then inspect hotel details, room availability, real-time prices, and booking links. It is intended for hotel search and comparison workflows, not for flights, rail, car rental, or other travel booking categories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel searches may transmit trip details such as destination, dates, occupancy, budget, and preferences to RollingGo's external service.

Mitigation: Share only trip details needed for the search and avoid including unrelated personal or sensitive information in hotel queries.

Risk: The RollingGo API key could be exposed if pasted into command-line arguments, logs, or shared transcripts.

Mitigation: Configure the API key through an environment variable or scoped host secret, and do not place the key directly in command-line arguments.

Risk: The skill depends on an external CLI and service, so hotel availability, pricing, and network results can change or fail at execution time.

Mitigation: Check command exit status and re-run or relax filters when results are empty, unavailable, or affected by network/API errors.

## Reference(s):

- [RollingGo homepage](https://rollinggo.store)
- [RollingGo API key application](https://rollinggo.store/apply)
- [ClawHub skill page](https://clawhub.ai/longcreat/skills/search-hotel)
- [Claw host environment reference](references/claw-host-env.md)
- [RollingGo NPX reference](references/rollinggo-npx.md)
- [RollingGo UV reference](references/rollinggo-uv.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON-result interpretation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The RollingGo CLI normally returns hotel data on stdout as JSON, with errors on stderr and booking or hotel detail URLs when available.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
