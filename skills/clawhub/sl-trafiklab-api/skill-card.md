## Description: <br>
Fetch real-time SL (Stockholm public transport) departures and deviation information using a Python CLI tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[patello](https://clawhub.ai/user/patello) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to check Stockholm public transport departures, deviations, route options, and saved favorite stops or routes from an agent workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts SL public transit APIs to retrieve live departures, route options, and deviations. <br>
Mitigation: Use it only where outbound access to the listed SL API endpoints is acceptable. <br>
Risk: Favorite stop and route commands persist workspace state in .sl/preferences.json. <br>
Mitigation: Review saved favorites and use the provided save/remove commands for changes rather than editing the file manually. <br>
Risk: Transit data can be delayed, unavailable, or differ from conditions in the field. <br>
Mitigation: Treat results as planning assistance and verify critical travel decisions with official SL channels when needed. <br>
Risk: The test requirements include pytest and are not needed for normal runtime use. <br>
Mitigation: Install test dependencies only in development or validation environments where dependency versions are managed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/patello/skills/sl-trafiklab-api) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/patello) <br>
- [SL Trafiklab CLI & API References](references/api.md) <br>
- [SL Journey Planner v2 - Trips API Reference](references/journey_planner_v2_spec.md) <br>
- [SL Deviations API Reference](references/sl_deviations_spec.md) <br>
- [SL Transport API Reference](references/sl_transport_spec.md) <br>
- [SL Journey Planner API](https://journeyplanner.integration.sl.se/v2) <br>
- [SL Deviations API](https://deviations.integration.sl.se/v1) <br>
- [SL Transport API](https://transport.integration.sl.se/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI text or JSON results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update .sl/preferences.json when favorite stop or route commands are used.] <br>

## Skill Version(s): <br>
3.4.1 (source: release evidence, _meta.json, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
