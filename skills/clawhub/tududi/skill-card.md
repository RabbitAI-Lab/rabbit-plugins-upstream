## Description: <br>
Manage tasks, projects, and notes in tududi (self-hosted task manager). Use for todo lists, task management, project organization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrisvel](https://clawhub.ai/user/chrisvel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users and agents use this skill to manage tasks, projects, inbox items, tags, and notes in a self-hosted tududi instance through the tududi API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An untrusted tududi server URL or over-broad API token could expose task-management data. <br>
Mitigation: Confirm TUDUDI_URL points to a tududi server you trust and use the least-privilege API token available. <br>
Risk: Delete operations can remove task or inbox items when the wrong UID is used. <br>
Mitigation: Ask the agent to list or fetch the item and repeat the UID before running delete operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrisvel/skills/tududi) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Configuration guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TUDUDI_URL and TUDUDI_API_TOKEN; update and delete operations use tududi UIDs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
