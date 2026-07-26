## Description: <br>
MTA system train departures (NYC Subway, LIRR, Metro-North). Use when the user wants train times, schedules, or service alerts for MTA transit. Covers MTA Subway, LIRR, and Metro-North across the greater New York area. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gumadeiras](https://clawhub.ai/user/gumadeiras) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve MTA train departures, station search results, service alerts, and saved-station favorites through the gotrain CLI. <br>

### Deployment Geography for Use: <br>
Global use; transit coverage is focused on the greater New York MTA system. <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the external gotrain npm package for transit lookups. <br>
Mitigation: Install only if you are comfortable trusting that package, and review or scan it before deployment. <br>


## Reference(s): <br>
- [gotrain ClawHub Skill](https://clawhub.ai/gumadeiras/skills/gotrain) <br>
- [gotrain npm package](https://www.npmjs.com/package/gotrain) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Text] <br>
**Output Format:** [Markdown with inline shell commands and CLI text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the external gotrain npm package and gotrain binary for live transit lookups.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
