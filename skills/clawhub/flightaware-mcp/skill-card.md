## Description:

Connects an agent to FlightAware AeroAPI for flight tracking, airport information, schedules, aircraft lookups, and flight alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers, aviation enthusiasts, and developers use this skill to check live flight status, airport activity, schedules, and aircraft information, or manage flight alerts through their own AeroAPI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An untrusted package or exposed AeroAPI key could compromise the user's account.

Mitigation: Verify the npm package before installing and provide only your own AeroAPI key through the MCP configuration.

Risk: AeroAPI requests may consume quota or incur charges.

Mitigation: Check account limits and costs before making repeated or premium-tier requests.

Risk: Creating, updating, or deleting alerts changes account settings.

Mitigation: Review each proposed alert change and obtain user confirmation before submitting it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)
- [FlightAware MCP npm package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, PNG images]

**Output Format:** [MCP tool responses with flight and airport data; optional flight-map PNG]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact responses omit image and avatar URLs; full responses preserve AeroAPI data.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
