## Description: <br>
Google Workspace Admin SDK integration with managed OAuth for reading and managing users, groups, organizational units, roles, and domain settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Workspace administrators and operators use this skill to let an agent assist with Google Workspace directory administration through the Maton OAuth/API gateway. It is intended for tasks such as reviewing users and groups, managing organizational units, assigning roles, and making explicitly approved administrative changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can assist with high-impact Google Workspace administration, including account, group, role, organizational unit, and domain changes. <br>
Mitigation: Use a least-privileged admin account, restrict OAuth scopes to the task, start with read-only checks, and require explicit approval with the exact method, endpoint path, target identifier, and consequences before any write action. <br>
Risk: A request may target the wrong Google Workspace connection when multiple Maton connections exist. <br>
Mitigation: Include the intended `Maton-Connection` header on every request and verify the connection before making changes. <br>
Risk: The skill depends on Maton as the OAuth/API gateway and requires a Maton API key. <br>
Mitigation: Install only when Maton is trusted for the intended administration workflow, protect the `MATON_API_KEY`, and revoke or delete the OAuth connection when the work is complete. <br>


## Reference(s): <br>
- [Google Workspace Admin on ClawHub](https://clawhub.ai/byungkyu/skills/google-workspace-admin) <br>
- [Maton](https://maton.ai) <br>
- [Google Admin SDK Overview](https://developers.google.com/admin-sdk) <br>
- [Directory API Users](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users) <br>
- [Directory API Groups](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups) <br>
- [Directory API Org Units](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits) <br>
- [Directory API Roles](https://developers.google.com/admin-sdk/directory/reference/rest/v1/roles) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline Python, JavaScript, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce HTTP request examples against Maton endpoints; write actions require explicit approval before execution.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
