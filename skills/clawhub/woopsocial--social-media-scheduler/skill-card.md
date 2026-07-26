## Description: <br>
Schedule, publish, cross-post, and manage social media posts with text or media across Facebook, Instagram, Threads, LinkedIn, X/Twitter, TikTok, Pinterest, and YouTube through WoopSocial's remote MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woopsocial](https://clawhub.ai/user/woopsocial) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketing teams, and developers use this skill to connect an agent to WoopSocial, select connected social accounts, prepare platform-specific post details, upload or reuse media, and schedule or publish posts. It is suited for content calendars, cross-posting, bulk scheduling, and checking delivery status after a post is created. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent connected to WoopSocial can schedule or publish public social posts to connected accounts. <br>
Mitigation: Confirm the target account, platform, post content, media, and timing before creating posts, and distinguish created, scheduled, published, and failed delivery states. <br>
Risk: OAuth credentials or API keys used for the MCP connection could be exposed through shared logs, command history, or copied setup commands. <br>
Mitigation: Review authentication setup carefully, avoid sharing secrets in logs or command history, and prefer secure credential handling for WoopSocial access. <br>
Risk: Delete actions for posts, accounts, projects, media, or webhooks can remove useful or public-facing assets. <br>
Mitigation: Require explicit user intent before calling delete tools and identify the affected resource before deletion. <br>


## Reference(s): <br>
- [WoopSocial homepage](https://woopsocial.com) <br>
- [WoopSocial documentation](https://docs.woopsocial.com) <br>
- [ClawHub skill listing](https://clawhub.ai/woopsocial/skills/social-media-scheduler) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, setup steps, and social-post workflow instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include WoopSocial post IDs, requested schedules, and delivery states such as pending, scheduled, published, or failed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
