## Description: <br>
Postiz is a tool to schedule social media and chat posts to 28+ channels X, LinkedIn, LinkedIn Page, Reddit, Instagram, Facebook Page, Threads, YouTube, Google My Business, TikTok, Pinterest, Dribbble, Discord, Slack, Kick, Twitch, Mastodon, Bluesky, Lemmy, Farcaster, Telegram, Nostr, VK, Medium, Dev.to, Hashnode, WordPress, ListMonk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nevo-david](https://clawhub.ai/user/nevo-david) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, operators, and AI-agent users use this skill to authenticate with Postiz, discover connected social integrations, schedule or draft social posts with media and platform-specific settings, and review post or platform analytics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable an agent to post, upload media, connect missing posts, and delete social content on real connected social accounts. <br>
Mitigation: Require review of the exact content, media files, target platform or account, integration IDs, schedule, and deletion target before any create, upload, connect, or delete command runs; prefer drafts or test accounts first. <br>
Risk: Postiz API keys or OAuth credentials may be exposed or left available longer than intended. <br>
Mitigation: Do not print secrets in terminals, avoid adding API keys to persistent shell profiles, and run `postiz auth:logout` when persistent OAuth access is not needed. <br>
Risk: Incorrect integration IDs or platform-specific settings can send content to the wrong account or channel. <br>
Mitigation: Use `postiz integrations:list`, `postiz integrations:settings`, and relevant integration trigger commands to confirm destination IDs and settings before scheduling or publishing. <br>


## Reference(s): <br>
- [ClawHub Postiz skill page](https://clawhub.ai/nevo-david/skills/postiz) <br>
- [Postiz public API introduction](https://docs.postiz.com/public-api/introduction) <br>
- [Postiz official website](https://postiz.com) <br>
- [Postiz npm package](https://www.npmjs.com/package/postiz) <br>
- [Postiz application repository linked by the skill](https://github.com/gitroomhq/postiz-app) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Postiz authentication through OAuth2 or POSTIZ_API_KEY; POSTIZ_API_URL is optional for custom API endpoints.] <br>

## Skill Version(s): <br>
1.0.15 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
