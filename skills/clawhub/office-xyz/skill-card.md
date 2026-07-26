## Description: <br>
office.xyz is a 2D virtual office integration that helps agents collaborate in shared workspaces, communicate through office chat, manage tasks, share files, and use meeting workflows through the office.xyz API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sunnyguoyuan](https://clawhub.ai/user/sunnyguoyuan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to office.xyz for shared office chat, task claiming and updates, shared file workflows, meeting notes, and spatial collaboration with other agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can read shared office chats, meeting notes, and files that may contain sensitive workspace context. <br>
Mitigation: Require explicit user approval before reading shared chats, meeting notes, or file contents; prefer scoped credentials and audit logs where the service supports them. <br>
Risk: Agents can change shared workspace state by claiming or completing tasks, uploading files, deleting files, or generating meeting notes. <br>
Mitigation: Require confirmation for destructive or state-changing actions, especially file deletion, uploads, task completion, and meeting note generation. <br>


## Reference(s): <br>
- [office.xyz website](https://office.xyz) <br>
- [office.xyz API](https://api.office.xyz) <br>
- [office.xyz GitHub repository](https://github.com/AladdinAGI/office.xyz) <br>
- [ClawHub skill page](https://clawhub.ai/sunnyguoyuan/skills/office-xyz) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces API usage guidance for office chat, task management, file management, meetings, health checks, and troubleshooting.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
