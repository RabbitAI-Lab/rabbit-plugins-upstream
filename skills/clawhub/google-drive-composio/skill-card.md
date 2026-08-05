## Description: <br>
Browse, read, export, upload, share, and organize Google Drive files through Composio-managed OAuth without local Google client credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[berkgungor](https://clawhub.ai/user/berkgungor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when a user points to Google Drive files or folders and needs Drive content discovered, downloaded, exported, uploaded, organized, or shared. It is suited to Google accounts connected through Composio-managed OAuth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can share, move, trash, upload, and create Google Drive content through the connected account. <br>
Mitigation: Confirm exact file IDs, destination folders, recipients, domains, and write actions with the user before running those commands. <br>
Risk: Downloads and uploads can read from or write to local workspace paths. <br>
Mitigation: Keep --save-to and --from-file paths inside the intended workspace and inspect paths before execution. <br>
Risk: The agent can only operate within the permissions of the Composio-connected Google account, which may include sensitive personal or Workspace files. <br>
Mitigation: Install and run the skill only for accounts whose Drive contents and sharing powers are appropriate for agent access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/berkgungor/skills/google-drive-composio) <br>
- [Composio](https://composio.dev/) <br>
- [Composio dashboard](https://app.composio.dev/) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance, JSON, files] <br>
**Output Format:** [Markdown instructions, shell command examples, JSON command responses, and optional workspace files from download or export commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require COMPOSIO_API_KEY and COMPOSIO_USER_ID or TENANT_ID; download and export commands may write files to caller-provided local paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
