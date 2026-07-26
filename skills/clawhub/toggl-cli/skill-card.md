## Description: <br>
Toggl CLI helps an agent guide installation and use of a command-line tool for managing Toggl Track time entries, projects, clients, tags, tasks, workspaces, organizations, groups, and user profile data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[froemic](https://clawhub.ai/user/froemic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, coding agents, and external users can use this skill to install and operate a Toggl Track CLI workflow for starting, stopping, listing, creating, updating, and deleting time-tracking resources. It is useful when an agent needs to provide shell commands, configuration guidance, and API examples for Toggl Track workspaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install flow asks users to install unpinned external Node code. <br>
Mitigation: Review the repository and dependencies before installation, and pin a trusted commit when using the skill in a repeatable workflow. <br>
Risk: The workflow requires a persistent TOGGL_API_TOKEN for Toggl Track access. <br>
Mitigation: Store the token only in a restricted local secret or environment location, avoid logging it, and rotate it if exposed. <br>
Risk: Several commands can create, update, archive, restore, stop, start, or delete real Toggl workspace data. <br>
Mitigation: Require explicit user confirmation before executing commands that mutate Toggl data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/froemic/skills/toggl-cli) <br>
- [Toggl API base URL named in artifact](https://api.track.toggl.com/api/v9) <br>
- [Toggl profile settings named in artifact](https://track.toggl.com/profile) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, CLI examples, configuration snippets, and API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include commands that read or mutate Toggl Track workspace data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
