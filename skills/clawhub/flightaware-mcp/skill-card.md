## Description:

Provides live flight tracking, airport information, schedules, aircraft lookups, and flight-alert management through FlightAware AeroAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers, aviation enthusiasts, and developers use this skill to check flights and airport activity, look up aircraft and schedules, and manage FlightAware flight alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party MCP package receives the user's AeroAPI key.

Mitigation: Install only if comfortable trusting the package with the key.

Risk: AeroAPI requests consume the user's subscription quota.

Mitigation: Review expected API usage and quota before making repeated queries.

Risk: Flight-map PNGs may be saved in the working directory.

Mitigation: Request inline map output or set AEROAPI_OUTPUT_DIR to an appropriate location.

Risk: Alert operations can change the user's FlightAware account settings.

Mitigation: Review the proposed changes before confirming alert writes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)
- [FlightAware MCP package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)

## Skill Output:

**Output Type(s):** [Text, Images, Configuration guidance]

**Output Format:** [Structured flight and airport responses, with optional PNG flight maps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flight maps can be returned inline or written to disk; alert changes require user confirmation.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
