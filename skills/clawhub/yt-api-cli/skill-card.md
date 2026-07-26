## Description: <br>
Manage YouTube account operations from the command line with a CLI for the YouTube Data API v3, including listing, searching, uploads, playlists, and channel updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nerveband](https://clawhub.ai/user/nerveband) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and automation users use this skill to install, configure, and operate a YouTube Data API CLI for account management tasks such as listing videos, searching, uploading, playlist management, and channel updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish videos, change thumbnails, edit playlists, and update channel content on an authenticated YouTube account. <br>
Mitigation: Install only if the referenced CLI is trusted, pin and verify the installed version where possible, and require explicit approval before any upload, thumbnail, playlist, channel update, or other account-changing command. <br>
Risk: OAuth client secrets, OAuth tokens, and service-account credentials can grant access to YouTube account data and publishing capabilities. <br>
Mitigation: Protect credentials, store tokens with restrictive permissions, avoid exposing service-account JSON files, and rotate credentials if they may have been shared or logged. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nerveband/skills/yt-api-cli) <br>
- [Google Cloud Console](https://console.cloud.google.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, API calls, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; CLI output is JSON by default and can also be YAML, CSV, or table.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires YouTube Data API credentials and explicit approval for account-changing operations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
