## Description:

Flight Price Track helps agents compare real-time flight prices across multiple platforms, scan flexible-date price calendars, assess price levels, and prepare price-watch requests for a chosen route or flight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to compare flight prices by route, date, and flight number, identify cheaper travel dates, and prepare target-price monitoring requests. It is intended for decision support and does not book tickets directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The price-watch feature may provide a generated command that is unsafe if a host executes it through shell interpretation.

Mitigation: Treat monitor output as structured data, or execute checks with a fixed command and safe argument list instead of passing generated strings to a shell.

Risk: A reusable proxy token is shipped in the source code.

Mitigation: Rotate the exposed token and load credentials from a secure runtime setting before deployment.

Risk: Flight route, date, and flight query details are sent through the publisher's proxy service.

Mitigation: Use the skill only where sending those travel query details to the publisher's proxy is acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/travel-skills/skills/flight-price-track)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON command results and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses route, date, flight number, target price, and threshold inputs; live query parameters are sent to the publisher's proxy service.]

## Skill Version(s):

2.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
