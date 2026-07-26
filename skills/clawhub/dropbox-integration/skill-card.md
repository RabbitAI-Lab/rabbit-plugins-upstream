## Description: <br>
Read-only Dropbox integration for browsing, searching, and downloading files from a Dropbox account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tirandagan](https://clawhub.ai/user/tirandagan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure Dropbox OAuth access, browse folders, search files, and download selected Dropbox content without granting write scopes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can grant broad read visibility into Dropbox data. <br>
Mitigation: Prefer Dropbox App Folder access unless whole-account search is required, and keep the requested Dropbox scopes read-only. <br>
Risk: Dropbox app credentials and long-lived refresh tokens are stored locally. <br>
Mitigation: Keep credentials.json and token.json out of git and backups, restrict file permissions, and revoke the Dropbox app if tokens may have leaked. <br>
Risk: Download commands write Dropbox content to local paths. <br>
Mitigation: Review every requested Dropbox path and local destination before allowing a download. <br>
Risk: OAuth setup may expose authorization details in shared or recorded terminals. <br>
Mitigation: Run setup in a private terminal session and avoid screen sharing or recording while authorizing the Dropbox app. <br>


## Reference(s): <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Dropbox API Documentation](https://www.dropbox.com/developers/documentation) <br>
- [Dropbox OAuth 2.0 Guide](https://www.dropbox.com/developers/reference/oauth-guide) <br>
- [Dropbox JavaScript SDK Documentation](https://dropbox.github.io/dropbox-sdk-js/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON credential examples, and command-line text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Download commands can write selected Dropbox files to user-specified local paths.] <br>

## Skill Version(s): <br>
1.0.1 (source: package.json and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
