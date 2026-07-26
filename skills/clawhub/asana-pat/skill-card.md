## Description: <br>
Manage Asana tasks, projects, briefs, status updates, custom fields, dependencies, attachments, events, and timelines via Personal Access Token (PAT). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[l-u-c-k-y](https://clawhub.ai/user/l-u-c-k-y) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, agents, and Asana users use this skill to manage personal tasks and project-manager workflows through a PAT-backed Asana CLI. It supports reading, searching, creating, updating, commenting on, attaching files to, and coordinating Asana tasks and projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Asana PAT lets the skill act with the token holder's Asana permissions. <br>
Mitigation: Use a dedicated, revocable PAT with the minimum Asana access needed for the agent run. <br>
Risk: Agent-initiated write actions can change tasks, project membership, comments, statuses, custom fields, dependencies, and timelines in shared workspaces. <br>
Mitigation: Review planned write actions before execution and use supported dry-run flows, such as timeline shifting dry runs, before applying broad changes. <br>
Risk: Attachment upload commands can share local files into Asana. <br>
Mitigation: Upload only files that are intended to be available in the target Asana task or project context. <br>
Risk: OpenClaw config and local event state can persist after the agent run. <br>
Mitigation: Remove stored PATs, workspace defaults, and event sync state when they are no longer needed. <br>


## Reference(s): <br>
- [Asana personal access token docs](https://developers.asana.com/docs/personal-access-token) <br>
- [Asana authentication overview](https://developers.asana.com/docs/authentication) <br>
- [Asana rich text guide](https://developers.asana.com/docs/rich-text) <br>
- [Asana upload attachment reference](https://developers.asana.com/reference/createattachmentforobject) <br>
- [Reference and implementation notes](references/REFERENCE.md) <br>
- [OpenClaw skills config](https://docs.openclaw.ai/tools/skills-config) <br>
- [ClawHub skill page](https://clawhub.ai/l-u-c-k-y/skills/asana-pat) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Configuration] <br>
**Output Format:** [JSON emitted by a Node.js CLI, with markdown guidance for command usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an Asana PAT through ASANA_PAT or ASANA_TOKEN; optional local config can store workspace defaults and event sync tokens.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
