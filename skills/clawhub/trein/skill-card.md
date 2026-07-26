## Description: <br>
Query Dutch Railways (NS) for train departures, trip planning, disruptions, and station search via the trein CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joehoel](https://clawhub.ai/user/joehoel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and agent users use Trein to retrieve Dutch Railways departures, trip plans, disruptions, and station matches through the trein CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on installing and running the third-party trein CLI before use. <br>
Mitigation: Install the CLI only from a trusted listed channel and review it before providing an NS API key. <br>
Risk: The NS API key may be exposed if stored insecurely in the optional local config file. <br>
Mitigation: Prefer a protected environment variable where practical, and treat the local trein config file as a secret-bearing file if used. <br>


## Reference(s): <br>
- [Trein ClawHub skill page](https://clawhub.ai/joehoel/skills/trein) <br>
- [Trein project homepage](https://github.com/joelkuijper/trein) <br>
- [Trein GitHub releases](https://github.com/joelkuijper/trein/releases) <br>
- [NS API portal](https://apiportal.ns.nl/) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the trein CLI and NS_API_KEY; optional aliases and API key configuration may be stored in the local trein config file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
