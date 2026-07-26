## Description: <br>
Query Dutch Railways (NS) for train departures, time-based trip planning, disruptions, and station search via the trein CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[timvandervoord](https://clawhub.ai/user/timvandervoord) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to answer train-travel questions in the Netherlands, including live departures, journey planning, disruptions, station lookup, and route-specific timing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on an external trein package or downloaded release and an NS API key. <br>
Mitigation: Install only from trusted upstream sources and prefer providing NS_API_KEY through the environment rather than embedding it in shared files. <br>
Risk: Local configuration and aliases may expose an API key or usual travel locations. <br>
Mitigation: Protect local trein configuration files and avoid sharing aliases or command output that reveal sensitive travel patterns. <br>
Risk: Results are limited to Dutch train travel and can be inappropriate for car, bus, or other transport questions. <br>
Mitigation: Confirm the user wants train travel before invoking the skill and do not use it for other transport modes. <br>


## Reference(s): <br>
- [trein project homepage](https://github.com/joelkuijper/trein) <br>
- [trein GitHub releases](https://github.com/joelkuijper/trein/releases) <br>
- [NS API Portal](https://apiportal.ns.nl/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and parsed JSON summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the trein CLI, prefers --json responses, and requires an NS_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
