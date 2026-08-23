## Description:

Fetch real-time SL (Stockholm public transport) departures and deviation information using a Python CLI tool. Use when checking departures, querying transit delays, or saving favorite sites and routes for quick status checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patello](https://clawhub.ai/user/patello)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query live Stockholm public transport departures, disruptions, route proposals, and saved favorite stops or routes through an agent-invoked Python CLI.

### Deployment Geography for Use:

Global, with transit data focused on Stockholm, Sweden.

## Known Risks and Mitigations:

Risk: The skill contacts SL/Trafiklab public APIs for live transit data.

Mitigation: Install and use it only in environments where outbound requests to those public transit APIs are acceptable.

Risk: Favorite stops and routes can be stored in `.sl/preferences.json` in the workspace.

Mitigation: Avoid saving sensitive travel patterns, and remove saved preferences when they are no longer needed.

Risk: The test dependency declaration may install vulnerable pytest versions if test requirements are installed without pinning.

Mitigation: Avoid installing test requirements unless needed, or pin or exclude vulnerable pytest versions first.

Risk: `route find` returns leg times in UTC while inputs are interpreted as Stockholm local time.

Mitigation: Convert returned times to Europe/Stockholm before presenting route timing to users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/patello/skills/sl-trafiklab-api)
- [SL Trafiklab CLI & API References](references/api.md)
- [SL Transport API Reference](references/sl_transport_spec.md)
- [SL Deviations API Reference](references/sl_deviations_spec.md)
- [SL Journey Planner v2 - Trips API Reference](references/journey_planner_v2_spec.md)
- [SL Transport API endpoint](https://transport.integration.sl.se/v1)
- [SL Deviations API endpoint](https://deviations.integration.sl.se/v1)
- [SL Journey Planner API endpoint](https://journeyplanner.integration.sl.se/v2)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with inline shell commands and JSON preference snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live public transit API results and workspace preference updates through the CLI.]

## Skill Version(s):

3.7.0 (source: server release evidence and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
