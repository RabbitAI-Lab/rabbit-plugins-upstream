## Description: <br>
Manage Asana tasks, projects, briefs, status updates, custom fields, dependencies, attachments, events, and timelines via Personal Access Token (PAT). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[l-u-c-k-y](https://clawhub.ai/user/l-u-c-k-y) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees, project managers, and developers use this skill to let an agent manage Asana workspaces, tasks, projects, briefs, status updates, custom fields, dependencies, attachments, events, and timelines through a PAT-backed CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make broad live changes to Asana data through a PAT, including writes, deletions, timeline shifts, comments/status updates, membership changes, and uploads. <br>
Mitigation: Use a least-privileged PAT where possible and require explicit approval before write, delete, timeline, comment/status, membership, or upload commands. <br>
Risk: Stored PAT configuration may expose account access if displayed or retained longer than needed. <br>
Mitigation: Avoid displaying stored config values that include the token, and rotate or revoke the PAT when the release or task is complete. <br>
Risk: Local file uploads can send unintended files to Asana. <br>
Mitigation: Confirm the target task or project and file path before running upload commands. <br>


## Reference(s): <br>
- [Asana personal access tokens](https://developers.asana.com/docs/personal-access-token) <br>
- [Asana authentication](https://developers.asana.com/docs/authentication) <br>
- [Asana rich text](https://developers.asana.com/docs/rich-text) <br>
- [Asana upload attachments](https://developers.asana.com/reference/createattachmentforobject) <br>
- [REFERENCE.md](references/REFERENCE.md) <br>
- [ClawHub skill page](https://clawhub.ai/l-u-c-k-y/skills/asana-agent-skill) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON on stdout with Markdown documentation examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+ and an Asana PAT exposed as ASANA_PAT or ASANA_TOKEN; commands may read from or write to live Asana resources.] <br>

## Skill Version(s): <br>
0.2.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
