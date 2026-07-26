## Description: <br>
Manage Plane.so projects and work items using the `plane` CLI, including project, issue, cycle, module, comment, member, state, and label workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vaguilera-jinko](https://clawhub.ai/user/vaguilera-jinko) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and teams using agent-assisted workflows use this skill to inspect and manage Plane.so workspace data from a CLI-backed agent interaction. It supports reading workspace information and making changes such as creating projects or issues, assigning members, adding comments, and updating or deleting work items. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs a GitHub-hosted plane script, which should be verified before local execution. <br>
Mitigation: Inspect the script before installing and prefer a pinned release or checksum when available. <br>
Risk: Plane commands can modify workspace data, including updates, assignments, comments, and deletes. <br>
Mitigation: Use a least-privileged Plane API token and verify project, issue, user, state, and label IDs before running write or delete commands. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vaguilera-jinko/skills/plane) <br>
- [Publisher Profile](https://clawhub.ai/user/vaguilera-jinko) <br>
- [Plane.so](https://plane.so) <br>
- [Plane Skill Homepage](https://github.com/JinkoLLC/plane-skill) <br>
- [Plane CLI Install Script](https://raw.githubusercontent.com/JinkoLLC/plane-skill/main/scripts/plane) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the plane CLI plus PLANE_API_KEY and PLANE_WORKSPACE; CLI output may be formatted tables or JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
