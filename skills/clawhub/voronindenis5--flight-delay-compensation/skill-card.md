## Description:

Check if a delayed, cancelled, or overbooked flight qualifies for cash compensation under EU261, UK261, US DOT, Canada APPR, Brazil ANAC, Turkey SHY, or India DGCA rules. Calculates exact amounts by distance tier, evaluates airline extraordinary-circumstances defenses, tracks claim deadlines, and generates ready-to-send claim letters. Use when a flight disruption occurred and the user wants to know their rights or file a claim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and their assisting agents use this skill to evaluate flight disruptions, estimate passenger-rights compensation, analyze airline defenses, track deadlines, and prepare a claim letter for eligible cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated letters or JSON exports may contain personal travel details, and user-selected output paths can overwrite existing local files.

Mitigation: Save exports only to trusted locations, review personal details before sharing, and avoid reusing existing paths with --letter or --json.

Risk: Flight-rights determinations depend on accurate route facts, jurisdiction, deadlines, and current compensation caps.

Mitigation: Verify itinerary facts, route distance, filing deadline, and any inflation-adjusted caps before sending a claim or relying on the result.

## Reference(s):

- [Passenger Rights by Jurisdiction](references/jurisdictions.md)
- [Claim Strategy: How to Actually Get Paid](references/claim-strategy.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/flight-delay-compensation)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown/plain text eligibility analysis with optional JSON export and local claim-letter file output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline rule-engine output; generated letters and JSON may contain personal travel details and should be reviewed before sharing.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
