## Description: <br>
Create and manage YouTube playlists when a user wants to create a playlist, add videos to playlists, or manage their YouTube playlists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[matejmicek](https://clawhub.ai/user/matejmicek) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to authenticate with YouTube and create, list, populate, and update playlists from video IDs or YouTube URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad YouTube account access and can access account data beyond playlist creation. <br>
Mitigation: Install only when the user trusts the skill with YouTube access and understands the scope before authenticating. <br>
Risk: A reusable OAuth token is cached locally in token.pickle. <br>
Mitigation: Delete token.pickle or revoke the Google OAuth grant when the task is complete or when access is no longer needed. <br>
Risk: The script can modify playlists, remove playlist items, and run commands that print liked videos and subscriptions. <br>
Mitigation: Review the exact command before execution and avoid undocumented commands unless the user explicitly requests that account data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/matejmicek/skills/youtube-playlists) <br>
- [Publisher profile](https://clawhub.ai/user/matejmicek) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, text, guidance, configuration] <br>
**Output Format:** [Markdown with inline shell commands and terminal text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local Python execution, browser-based Google OAuth, a credentials.json file, and a cached token.pickle for repeat use.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
