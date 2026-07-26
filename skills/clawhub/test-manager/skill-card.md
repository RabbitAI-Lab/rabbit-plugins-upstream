## Description: <br>
Manage ClickUp tasks by listing, creating, updating statuses, and retrieving details through the ClickUp API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[savelieve](https://clawhub.ai/user/savelieve) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and workspace operators use this skill to let an agent inspect ClickUp tasks, create new tasks, search workspaces, and update task statuses with supplied ClickUp credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create tasks and update task statuses in a connected ClickUp workspace. <br>
Mitigation: Require explicit confirmation before creating tasks or changing statuses in important workspaces. <br>
Risk: The skill reads a ClickUp API token from environment variables or local configuration. <br>
Mitigation: Use a least-privilege ClickUp token and avoid storing secrets in shared markdown when possible. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/savelieve/skills/test-manager) <br>
- [ClickUp API Base URL](https://api.clickup.com/api/v2) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API Calls, Guidance, Configuration] <br>
**Output Format:** [Text summaries with JSON task data and Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ClickUp API token and workspace identifiers supplied by the user or environment.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
