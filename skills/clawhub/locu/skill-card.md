## Description: <br>
Manage tasks and projects via Locu's Public API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davidsmorais](https://clawhub.ai/user/davidsmorais) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and workspace users use this skill to let an agent retrieve Locu profile, task, and project information through Locu's Public API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can read Locu user, task, and project data returned by api.locu.app when provided a Locu API token. <br>
Mitigation: Use a least-privilege, revocable Locu token where available, and install the skill only when that level of data access is acceptable. <br>


## Reference(s): <br>
- [Locu API user endpoint](https://api.locu.app/api/v1/me) <br>
- [Locu API tasks endpoint](https://api.locu.app/api/v1/tasks) <br>
- [Locu API projects endpoint](https://api.locu.app/api/v1/projects) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON parsing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LOCU_API_TOKEN and returns Locu API data for profile, tasks, and projects.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
