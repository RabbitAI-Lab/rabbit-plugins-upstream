## Description: <br>
Upload, download, and manage files in Dropbox with automatic OAuth token refresh. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thekie](https://clawhub.ai/user/thekie) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and automation users use this skill to let an agent list, search, upload, download, and create folders in Dropbox from Linux, macOS, Windows, or headless environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dropbox app keys, app secrets, refresh tokens, and refreshed access tokens are stored locally in ~/.config/atlas/dropbox.env. <br>
Mitigation: Keep the token file private with restrictive permissions such as chmod 600, never commit or share it, and revoke the Dropbox app if the file may have been exposed. <br>
Risk: The skill can upload local files to Dropbox and download Dropbox files to agent-selected local paths. <br>
Mitigation: Review upload and download paths before running commands, and prefer an App Folder-scoped Dropbox app when broad account access is unnecessary. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thekie/skills/dropbox-lite) <br>
- [Dropbox Developers](https://www.dropbox.com/developers) <br>
- [Dropbox OAuth Guide](https://developers.dropbox.com/oauth-guide) <br>
- [Dropbox API Explorer](https://dropbox.github.io/dropbox-api-v2-explorer/) <br>
- [Dropbox API Documentation](https://www.dropbox.com/developers/documentation) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, Files, Configuration instructions] <br>
**Output Format:** [Plain text CLI output, local file writes for downloads, Dropbox file writes for uploads, and Markdown setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Dropbox app credentials and an OAuth refresh token stored in a local environment file.] <br>

## Skill Version(s): <br>
1.0.1 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
