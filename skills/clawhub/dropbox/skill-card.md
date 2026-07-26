## Description: <br>
Dropbox Manager helps agents manage Dropbox files through a Swift-native MCP server and CLI for listing, searching, uploading, downloading, deleting, reading files, and account lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ryanlisse](https://clawhub.ai/user/ryanlisse) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to connect an MCP-capable agent or local CLI workflow to Dropbox for file browsing, search, transfer, and account operations. It is intended for environments where the user can grant and manage Dropbox credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dropbox credentials and file-operation tools can grant an agent read, write, delete, overwrite, download, upload, and sync authority over user files. <br>
Mitigation: Use the documented OAuth PKCE and Keychain flow when possible, grant only needed Dropbox scopes, and require user confirmation before uploads, downloads, deletes, overwrites, or rclone sync operations. <br>
Risk: The bundled MCP setup guide recommends running an unpinned npm MCP server while passing Dropbox credentials. <br>
Mitigation: Prefer the documented Swift Dropbook build path, or independently trust and pin any npm MCP package before using it with Dropbox credentials. <br>
Risk: Bulk rclone copy, sync, bisync, and mount commands can move or remove large amounts of Dropbox data. <br>
Mitigation: Preview bulk operations with dry runs, verify source and destination paths, keep backups, and use conservative rate limits for large transfers. <br>


## Reference(s): <br>
- [Dropbox Manager skill documentation](artifact/SKILL.md) <br>
- [MCP setup guide](artifact/references/mcp-setup.md) <br>
- [Dropbox API documentation](https://www.dropbox.com/developers/documentation) <br>
- [rclone Dropbox documentation](https://rclone.org/dropbox/) <br>
- [RFC 7636: Proof Key for Code Exchange](https://datatracker.ietf.org/doc/html/rfc7636) <br>
- [RFC 9700: OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/rfc9700) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON tool results, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, MCP configuration JSON, and text or JSON tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate Dropbox file operations through an MCP server or CLI when configured with Dropbox credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
