## Description: <br>
Radar (radar.com) connector skill for reading, creating, and updating Radar data through the OOMOL oo CLI instead of direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate Radar through an OOMOL-connected account for address autocomplete, geocoding, IP geocoding, reverse geocoding, and nearby place search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The first-time setup path installs the remote oo CLI, which executes an installer from cli.oomol.com. <br>
Mitigation: Review the remote installer before first-time setup, as recommended by ClawScan guidance. <br>
Risk: Actions marked write can change Radar state when run with an exact payload. <br>
Mitigation: Confirm the action payload and expected effect with the user before executing any write action. <br>
Risk: Connector schemas may change over time, causing stale payloads to be incorrect. <br>
Mitigation: Inspect the live Radar connector schema before constructing each action payload. <br>


## Reference(s): <br>
- [Radar homepage](https://radar.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before actions; Radar command responses include data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
