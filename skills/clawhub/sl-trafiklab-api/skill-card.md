## Description:

Fetch real-time SL (Stockholm public transport) departures and deviation information using a Python CLI tool. Use when checking departures, querying transit delays, or saving favorite sites and routes for quick status checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patello](https://clawhub.ai/user/patello)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to query Stockholm public transport departures, route options, route safety buffers, and service deviations from SL public API endpoints. It also helps users maintain local favorite stops and routes for repeat checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transit queries may send stop names, stop IDs, route endpoints, times, and filters to SL public API endpoints.

Mitigation: Avoid submitting sensitive personal travel patterns when using the public API-backed commands.

Risk: Saved favorite stops and routes are stored locally in .sl/preferences.json in the workspace.

Mitigation: Review and remove local favorites when they are no longer needed or when sharing the workspace.

Risk: The included test dependency range allows pytest>=8.0.0.

Mitigation: Pin or update pytest deliberately before running tests in sensitive or controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/patello/skills/sl-trafiklab-api)
- [Publisher profile](https://clawhub.ai/user/patello)
- [SL Trafiklab CLI & API References](references/api.md)
- [SL Journey Planner v2 - Trips API Reference](references/journey_planner_v2_spec.md)
- [SL Deviations API Reference](references/sl_deviations_spec.md)
- [SL Transport API Reference](references/sl_transport_spec.md)
- [SL Transport API](https://transport.integration.sl.se/v1)
- [SL Deviations API](https://deviations.integration.sl.se/v1)
- [SL Journey Planner API](https://journeyplanner.integration.sl.se/v2)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with inline shell commands and CLI output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3; queries SL public API endpoints and may maintain favorites in .sl/preferences.json.]

## Skill Version(s):

3.6.0 (source: server release metadata and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
