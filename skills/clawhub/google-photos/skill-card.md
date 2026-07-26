## Description: <br>
Manage Google Photos library. Upload photos, create albums, and list library content. Use when the user wants to backup, organize, or share images via Google Photos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jorgermp](https://clawhub.ai/user/jorgermp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and OpenClaw agents use this skill to upload photos, create albums, and inspect Google Photos albums through the user's own Google Photos account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Google Photos OAuth access and stores a reusable local token. <br>
Mitigation: Use your own OAuth client credentials, review the requested Google consent scopes, store token files privately, and revoke the app's Google access when it is no longer needed. <br>
Risk: Credential and token files can expose access to the user's Google Photos account if shared or checked into another system. <br>
Mitigation: Keep credentials.json and token.pickle outside shared workspaces and never reuse token files from other people. <br>


## Reference(s): <br>
- [Google Photos Library API](https://photoslibrary.googleapis.com) <br>
- [Google Photos albums endpoint](https://photoslibrary.googleapis.com/v1/albums) <br>
- [Google Photos uploads endpoint](https://photoslibrary.googleapis.com/v1/uploads) <br>
- [Google Photos media item creation endpoint](https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, API calls, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided Google OAuth credentials and a local token file.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
