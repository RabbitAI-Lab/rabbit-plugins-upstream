## Description: <br>
Google Drive API integration with managed OAuth for listing, searching, creating, uploading, exporting, updating, deleting, and sharing files and folders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to work with a user-authorized Google Drive account through Maton, including file discovery, downloads, exports, uploads, metadata updates, deletion, and sharing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Google Drive requests are routed through Maton and require Google OAuth permissions for the connected account. <br>
Mitigation: Install only if that routing and permission model is acceptable, and verify the intended Google account before use. <br>
Risk: Write operations can create, update, delete, move, upload, or share Drive resources. <br>
Mitigation: Confirm the connection, target file or folder, sharing recipient, and intended effect before approving any write operation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-drive) <br>
- [Google Drive API Reference](https://developers.google.com/drive/api/reference/rest/v3) <br>
- [Google Drive Uploads Guide](https://developers.google.com/drive/api/guides/manage-uploads) <br>
- [Google Drive Search Query Syntax](https://developers.google.com/drive/api/guides/search-files) <br>
- [Maton CLI Manual](https://cli.maton.ai/manual) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, HTTP endpoints, and Python or JavaScript code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY and a user-authorized Google Drive connection.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
