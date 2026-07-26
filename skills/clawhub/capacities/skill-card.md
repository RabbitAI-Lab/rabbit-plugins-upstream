## Description: <br>
Manage Capacities notes, daily entries, and weblinks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davidsmorais](https://clawhub.ai/user/davidsmorais) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and knowledge workers use this skill to have an agent prepare Capacities API requests for adding daily notes, saving weblinks, looking up objects, and retrieving space information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Notes, URLs, search terms, and space requests may be sent to Capacities. <br>
Mitigation: Review selected content before execution and avoid sending secrets or regulated information unless appropriate for the Capacities account and workspace. <br>
Risk: The skill requires a Capacities API token. <br>
Mitigation: Store CAPACITIES_API_TOKEN carefully and provide it only in trusted agent sessions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/davidsmorais/skills/capacities) <br>
- [Capacities daily note API endpoint](https://api.capacities.io/save-to-daily-note) <br>
- [Capacities weblink API endpoint](https://api.capacities.io/save-weblink) <br>
- [Capacities lookup API endpoint](https://api.capacities.io/lookup) <br>
- [Capacities space info API endpoint](https://api.capacities.io/space-info?spaceid=$CAPACITIES_SPACE_ID) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CAPACITIES_API_TOKEN; CAPACITIES_SPACE_ID is optional.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
