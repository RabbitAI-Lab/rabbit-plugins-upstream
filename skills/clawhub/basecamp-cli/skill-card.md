## Description: <br>
Manage Basecamp projects, to-dos, messages, campfires, people, and account authentication from a TypeScript CLI using the Basecamp bc3 API and 37signals Launchpad OAuth. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[emredoganer](https://clawhub.ai/user/emredoganer) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, project operators, and agents use this skill to authenticate to Basecamp and automate project, to-do, message, campfire, people, and account workflows from the terminal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI can access and modify Basecamp account content through the authenticated account. <br>
Mitigation: Install and run it only for intended Basecamp workspaces, review OAuth app permissions, and use logout or revoke the Basecamp integration when access is no longer needed. <br>
Risk: OAuth client secrets and access tokens are sensitive. <br>
Mitigation: Keep BASECAMP_CLIENT_SECRET in the environment rather than config files, avoid committing local credentials, and clear or revoke tokens when access should end. <br>
Risk: Automation can create, update, archive, complete, or send content in the wrong Basecamp project if IDs are incorrect. <br>
Mitigation: Confirm the selected account and project IDs with read-only list or get commands before running mutating commands. <br>


## Reference(s): <br>
- [Basecamp bc3 API documentation](https://github.com/basecamp/bc3-api) <br>
- [37signals Launchpad integrations](https://launchpad.37signals.com/integrations) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text and optional JSON responses, with Markdown usage guidance in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands operate against the authenticated Basecamp account and selected account/project IDs; list and get commands can emit JSON with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
