## Description: <br>
Track time with Toggl via the toggl CLI, including starting and stopping timers, checking current work, viewing reports, listing entries, and managing time entries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clvrobj](https://clawhub.ai/user/clvrobj) <br>

### License/Terms of Use: <br>


## Use Case: <br>
People who track work time use this skill to have an agent prepare Toggl CLI commands for starting, stopping, reviewing, adding, editing, and deleting time entries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Toggl API token and CLI configuration can expose access to the user's Toggl account. <br>
Mitigation: Keep the token private, avoid pasting or logging config contents, and restrict the local config file permissions. <br>
Risk: Deleting a time entry can remove user time-tracking data. <br>
Mitigation: Preview the target entry and require clear user confirmation before running a delete command. <br>


## Reference(s): <br>
- [Toggl Track profile](https://track.toggl.com/profile) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may require a local toggl CLI installation and a private Toggl API token.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
