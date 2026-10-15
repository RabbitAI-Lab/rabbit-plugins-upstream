## Description:

Provides flight tracking, airport information, schedules, aircraft ownership lookups, and flight alert management through FlightAware AeroAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers, aviation enthusiasts, and developers use this skill to check flight status, positions, airport activity, schedules, and aircraft ownership, or to manage flight alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unverified package could expose the user's environment or API key.

Mitigation: Verify the npm/GitHub package provenance before installation and use an AeroAPI key with only the privileges needed.

Risk: Alert writes can change FlightAware account alert settings and endpoints.

Mitigation: Keep alert creation, updates, deletion, and endpoint changes subject to explicit user confirmation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [npm package (linked in skill)](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [Text, JSON, PNG images]

**Output Format:** [Flight and airport data, alert receipts, and optional flight-map PNGs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flight maps can be saved locally or returned inline; live requests use the user's AeroAPI quota.]

## Skill Version(s):

1.3.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
