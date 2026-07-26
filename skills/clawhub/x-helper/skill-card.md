## Description: <br>
Full-featured X (Twitter) assistant for search, posting with media, threads, direct messages, Lists, bookmarks, trends, articles, block/mute actions, and related account workflows using Python standard library scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate X account workflows from an agent, including reading public content, posting tweets and threads, managing bookmarks and Lists, handling direct messages, and performing account actions such as follow, block, and mute. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform powerful X account actions, including posting, deleting, direct messaging, following, blocking, muting, publishing articles, and managing Lists or bookmarks. <br>
Mitigation: Use a least-privileged X token and confirm every write, delete, DM, follow, block, mute, and publish action before execution. <br>
Risk: Tweets, direct messages, media files, search queries, user information, and bearer tokens are sent to X API services during normal use. <br>
Mitigation: Avoid sensitive direct messages or media, and only use the skill when sending account data to X API endpoints is acceptable. <br>
Risk: OAuth authorization can create a local token cache under ~/.x-helper/auth.json. <br>
Mitigation: Clear the cache with auth logout when OAuth authorization is no longer needed. <br>


## Reference(s): <br>
- [X Helper on ClawHub](https://clawhub.ai/tobewin/skills/x-helper) <br>
- [Publisher Profile](https://clawhub.ai/user/tobewin) <br>
- [X Developer Portal](https://developer.x.com) <br>
- [X API v2 Base URL](https://api.x.com/2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON/text command output from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided X_CLIENT_ID and X_BEARER_TOKEN environment variables for authenticated X API actions.] <br>

## Skill Version(s): <br>
3.0.6 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
