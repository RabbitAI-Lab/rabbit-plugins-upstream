## Description:

Fetch real-time SL (Stockholm public transport) departures and deviation information using a Python CLI tool. Use when checking departures, querying transit delays, or saving favorite sites and routes for quick status checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patello](https://clawhub.ai/user/patello)

### License/Terms of Use:

MIT-0

## Use Case:

External OpenClaw users use this skill to query Stockholm public transport departures, deviations, journey proposals, and saved favorite stops or routes through a local Python CLI.

### Deployment Geography for Use:

Global use for Stockholm, Sweden public transport data.

## Known Risks and Mitigations:

Risk: Saved favorite stops and routes are stored locally in .sl/preferences.json and can reveal commute patterns or places the user visits.

Mitigation: Use save and remove commands deliberately, avoid storing sensitive routines in shared workspaces, and delete favorites that are no longer needed.

Risk: Queries send stop names, stop IDs, route endpoints, and timing options to public SL/Trafiklab endpoints.

Mitigation: Avoid querying sensitive location routines when privacy matters and review applicable public API terms before organizational use.

Risk: Preference-dependent commands resolve .sl/preferences.json relative to the current working directory, so running from the wrong directory can produce missing-favorite results.

Mitigation: Run the CLI from the intended workspace root or pass an explicit preferences path when checking or managing saved routes and sites.

## Reference(s):

- [SL Trafiklab API Skill on ClawHub](https://clawhub.ai/patello/skills/sl-trafiklab-api)
- [SL Trafiklab CLI & API References](references/api.md)
- [SL Transport API Reference](references/sl_transport_spec.md)
- [SL Deviations API Reference](references/sl_deviations_spec.md)
- [SL Journey Planner v2 Trips API Reference](references/journey_planner_v2_spec.md)
- [SL Transport API endpoint](https://transport.integration.sl.se/v1)
- [SL Deviations API endpoint](https://deviations.integration.sl.se/v1)
- [SL Journey Planner v2 endpoint](https://journeyplanner.integration.sl.se/v2)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI text output derived from JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, queries public SL/Trafiklab endpoints, and may write favorite stops and routes to .sl/preferences.json.]

## Skill Version(s):

3.5.0 (source: ClawHub release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
