## Description: <br>
Manage Zoom meetings via OAuth API. Create, list, delete, and update events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vnagin](https://clawhub.ai/user/vnagin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage Zoom meetings from an agent workflow or CLI without opening the Zoom dashboard. It supports creating, listing, updating, inspecting, and deleting meetings through Zoom Server-to-Server OAuth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Zoom admin OAuth scopes can allow account-level meeting access, creation, updates, deletion, and recording-related access. <br>
Mitigation: Use a dedicated least-privilege Zoom Server-to-Server OAuth app and grant recording-read access only when it is required. <br>
Risk: Meeting creation enables cloud recording by default, which can create legal or workplace compliance obligations. <br>
Mitigation: Confirm legal and workplace rules before enabling automatic cloud recording. <br>
Risk: Update and delete commands can modify or remove meetings without built-in safeguards. <br>
Mitigation: Require human confirmation before any update or delete command is run. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vnagin/skills/zoom-manager-clawd) <br>
- [Publisher profile](https://clawhub.ai/user/vnagin) <br>
- [Zoom App Marketplace](https://marketplace.zoom.us/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [CLI text and JSON responses, with Markdown command examples in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and Zoom OAuth environment variables: ZOOM_CLIENT_ID, ZOOM_CLIENT_SECRET, and ZOOM_ACCOUNT_ID.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
