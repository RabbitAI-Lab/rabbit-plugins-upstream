## Description: <br>
Toggl Track API integration with managed OAuth for tracking time and managing projects, clients, tags, workspaces, and time entries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate Toggl Track through Maton-managed OAuth, including reading account and workspace data and creating, updating, stopping, or deleting time-tracking records with user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify Toggl Track resources through Maton-managed OAuth. <br>
Mitigation: Install only when Maton access to the connected Toggl Track account is acceptable. <br>
Risk: Write and delete requests can affect time entries, projects, clients, tags, or workspace data. <br>
Mitigation: Confirm the workspace, connection, target resource, and exact intended change before approving create, update, stop, archive, restore, or delete actions. <br>
Risk: The Maton API key can expose access if shown in shared terminals, prompts, or logs. <br>
Mitigation: Store MATON_API_KEY as an environment variable or secret and avoid echoing it or pasting it into shared contexts. <br>
Risk: Multiple Toggl Track connections may route requests to the wrong account. <br>
Mitigation: Use the Maton-Connection header when multiple active connections exist and verify the selected connection before taking action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/toggl-track) <br>
- [Maton homepage](https://maton.ai) <br>
- [Toggl Track API documentation](https://engineering.toggl.com/docs/) <br>
- [Toggl Track API authentication reference](https://engineering.toggl.com/docs/api/authentication) <br>
- [Time Entries API](https://engineering.toggl.com/docs/api/time_entries) <br>
- [Projects API](https://engineering.toggl.com/docs/api/projects) <br>
- [Clients API](https://engineering.toggl.com/docs/api/clients) <br>
- [Tags API](https://engineering.toggl.com/docs/api/tags) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline HTTP paths, JSON examples, Python examples, JavaScript examples, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, a MATON_API_KEY environment variable, and a connected Toggl Track account through Maton-managed OAuth.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
