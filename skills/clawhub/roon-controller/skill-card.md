## Description: <br>
Roon Controller lets an agent control a Roon music player through the Roon API, including Core discovery, zone selection, playback controls, current-track queries, and Chinese command support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[puterjam](https://clawhub.ai/user/puterjam) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent control playback on a Roon Core, select zones, and report current track details from a local or network-accessible Roon setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control Roon playback on the user's configured Roon Core. <br>
Mitigation: Install it only when agent-driven Roon playback control is intended, and revoke the extension in Roon when it is no longer needed. <br>
Risk: The skill stores a Roon authorization token in ~/clawd/roon_config.json. <br>
Mitigation: Keep that file private and use user-only file permissions for the configuration directory and token file. <br>
Risk: The skill depends on the roonapi Python package and a reachable Roon Core. <br>
Mitigation: Install dependencies from trusted package sources and run the skill only on the same trusted network as the intended Roon Core. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/puterjam/skills/roon-controller) <br>
- [Publisher profile](https://clawhub.ai/user/puterjam) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python examples, shell commands, and JSON-like result dictionaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may save local Roon connection settings and an authorization token in ~/clawd/roon_config.json.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
